import requests
import pprint
import random
import json
import time

from optparse import OptionParser
from random_words import RandomWords

pp = pprint.PrettyPrinter()
rw = RandomWords()

requests.packages.urllib3.disable_warnings(
    requests.packages.urllib3.connectionpool.InsecureRequestWarning)

required = ['apikey', 'hostname']

parser = OptionParser()
parser.add_option("-a", "--apikey", dest="apikey", help="[REQUIRED]")
parser.add_option("-H", "--hostname", dest="hostname", help="[REQUIRED]")
parser.add_option("-n", "--number", dest="number_detections")
parser.add_option("-o", "--ongoing", dest="all_ongoing")

(options, args) = parser.parse_args()

for r in required:
    if options.__dict__[r] is None:
        parser.error("Parameter {} required".format(r))

if not options.number_detections:
    number_detections = 5
else:
    number_detections = int(options.number_detections)
    assert number_detections > 0, "-n takes positive values"

headers = {'Content-Type': 'application/json',
           'Accept': 'application/json',
           'Authorization': 'ExtraHop apikey={}'.format(options.apikey)}


url = 'https://{hostname}/api/v1/'.format(hostname=options.hostname)

current_time_ms = int(round(time.time(), -3)) * 1000

stat_length = 60 * 60 * 1000

earliest_start = current_time_ms - 10 * stat_length
latest_end = current_time_ms - stat_length


get_devices_url = url + "devices?search_type=activity&" \
    "value=extrahop.device.dns_client&active_from={}" \
    "&active_until={}".format(str(earliest_start), str(latest_end))

limit = 100
offset = 0
advanced_analysis_devices = []

while True:
    print("Requesting devices...")
    tmp_url = get_devices_url + "&limit={limit}&offset={offset}".format(
        limit=str(limit), offset=str(offset))

    devices_rsp = requests.get(tmp_url, headers=headers, verify=False)

    assert devices_rsp.status_code == 200, "/devices failed with "\
        "status code" + str(devices_rsp.status_code)

    if not devices_rsp.json():
        break

    advanced_analysis_devices.extend(list(filter(
        lambda x: x["analysis"] == "advanced", devices_rsp.json())))

    offset = limit
    limit = offset + 100

assert advanced_analysis_devices, advanced_analysis_devices

device_ids = [device["id"] for device in advanced_analysis_devices]

assert device_ids, "Device IDs not empty"

CATEGORIES = {
    "sec": ["sec.command", "sec.recon", "sec.lateral",
            "sec.exploit", "sec.action"],
    "perf": ["perf.storage", "perf.service", "perf.auth", "perf.db",
             "perf.network"]
}

detection_options = [
    {
        "sources": [
            {
                "protocol": "dns",
                "role": "client",
                "object_type": "device"
            }
        ]
    },
    {
        "metrics":  [
            {
                "stat_name": "dhcp_server",
                "field_name": "rsp_msg_type",
                "key1": "{\"key_type\": \"string\", \"str\": \"DHCPNAK\"}",
                "stat_cycle": "1hr",
                "object_type": "device",
                "anomaly_metadata": {
                        "baseline_min": 0,
                        "peak_deviation": random.randint(0, 100000),
                        "peak_value": random.randint(0, 100000),
                        "baseline_max": 1.0
                }
            },
            {
                "stat_name": "dhcp_server",
                "field_name": "rsp_error",
                "stat_cycle": "30sec",
                "object_type": "device",
                "anomaly_metadata": {
                    "baseline_min": 2.0,
                    "peak_deviation": random.randint(0, 19999),
                    "peak_value": random.randint(0, 100000),
                    "baseline_max": 4.0
                }
            }
        ]
    },
    {
        "metrics":  [
            {
                "stat_name": "cifs_client_detail",
                "field_name": "error_type",
                "key1": "{\"key_type\": \"string\", \"str\": \"STATUS_LOGON_FAILURE\"}",
                "stat_cycle": "1hr",
                "object_type": "device",
                "anomaly_metadata": {
                        "baseline_min": 0,
                        "peak_deviation": random.randint(0, 100000),
                        "peak_value": random.randint(0, 100000),
                        "baseline_max": 1.0
                }
            }
        ]
    },
    {
        "metrics":  [
            {
                "stat_name": "http_server",
                "field_name": "rsp",
                "stat_cycle": "1hr",
                "object_type": "device",
                "anomaly_metadata": {
                    "baseline_min": 0,
                    "peak_deviation": random.randint(0, 100000),
                    "peak_value": random.randint(0, 100000),
                    "baseline_max": 1.0
                }
            }
        ]
    },
    {
        "metrics":  [
            {
                "stat_name": "telnet_server",
                "field_name": "sessions",
                "stat_cycle": "1hr",
                "object_type": "device",
                "anomaly_metadata": {
                    "baseline_min": 0,
                    "peak_deviation": random.randint(0, 100000),
                    "peak_value": random.randint(0, 100000),
                    "baseline_max": 1.0
                }
            }
        ]
    },
    {
        "metrics":  [
            {
                "stat_name": "ssh_client",
                "field_name": "sessions",
                "stat_cycle": "1hr",
                "object_type": "device",
                "anomaly_metadata": {
                    "baseline_min": 0,
                    "peak_deviation": random.randint(0, 100000),
                    "peak_value": random.randint(0, 100000),
                    "baseline_max": 1.0
                }
            }
        ]
    },
    {
        "metrics":  [
            {
                "stat_name": "net",
                "field_name": "external_bytes_out",
                "stat_cycle": "1hr",
                "object_type": "device",
                "anomaly_metadata": {
                    "baseline_min": 0,
                    "peak_deviation": random.randint(0, 100000),
                    "peak_value": random.randint(0, 100000),
                    "baseline_max": 1.0
                }
            }
        ]
    },
    {
        "sources": [
            {
                "protocol": "udp",
                "role": None,
                "object_type": "device"
            }
        ]
    },
    {
        "sources": [
            {
                "protocol": "tcp",
                "role": None,
                "object_type": "device"
            }
        ]
    }
]

for i in range(number_detections):

    start_hours_ago = random.randint(2, 10)

    while True:
        duration_hours = random.randint(1, 8)

        if start_hours_ago - duration_hours > 0:
            break

    start_time_ms = current_time_ms - start_hours_ago * stat_length

    if random.randint(0, 100) < 25 or options.all_ongoing:
        end_time_ms = None
        print("START: {}\tEND: ONGOING".format(
            time.strftime('%m/%d/%Y %H:%M:%S',
                          time.localtime(start_time_ms/1000))))
    else:
        end_time_ms = start_time_ms + duration_hours * stat_length
        assert end_time_ms < current_time_ms

        print("START: {}\tEND: {}".format(
            time.strftime('%m/%d/%Y %H:%M:%S',
                          time.localtime(start_time_ms/1000)),
            time.strftime('%m/%d/%Y %H:%M:%S',
                          time.localtime(end_time_ms/1000))))

    if random.randint(0, 100) < 25:
        score = None
    else:
        score = random.randint(1, 99)

    device_id = random.choice(device_ids)

    top_category = random.choice(list(CATEGORIES.keys()))

    body = {
        "categories": [top_category, random.choice(CATEGORIES[top_category])],
        "description": [
            ' '.join(word for word in rw.random_words(count=30)),
            "\n* ",
            {
                "key_type": "object",
                "object_type": "device",
                "oid": random.choice(device_ids)
            },
            "\n* ",
            {
                "key_type": "object",
                "object_type": "device",
                "oid": random.choice(device_ids)
            },
            "\n* ",
            {
                "key_type": "object",
                "object_type": "device",
                "oid": random.choice(device_ids)
            }
        ],
        "update_time": current_time_ms,
        "end_time": end_time_ms,
        "title": rw.random_word(),
        "start_time": start_time_ms,
        "hopcloud_id": str(random.randint(0, 1000000000)),
        "type": "source_metrics_anomaly",
        "risk_score": score,
        "detail": random.choice(detection_options)
    }

    # provide missing fields
    try:
        for item in body['detail']['sources']:
            item['update_time'] = current_time_ms
            item['start_time'] = start_time_ms
            item['end_time'] = end_time_ms
            item['object_id'] = device_id
    except KeyError:
        pass

    try:
        for item in body['detail']['metrics']:
            item['update_time'] = current_time_ms
            item['start_time'] = start_time_ms
            item['end_time'] = end_time_ms
            item['object_id'] = device_id
    except KeyError:
        pass

    rsp = requests.post(url + "events", headers=headers,
                        data=json.dumps(body), verify=False)
    if rsp.status_code != 201:
        print(rsp.status_code, rsp.text)
    else:
        print(rsp.status_code, "Event created")


rsp = requests.post(url + "events/time", headers=headers,
                    data=json.dumps({"anomaly_time": current_time_ms}),
                    verify=False)
print(rsp.status_code)
