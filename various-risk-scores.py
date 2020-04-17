import requests
import random
import json
import time

from optparse import OptionParser

requests.packages.urllib3.disable_warnings()

parser = OptionParser()
parser.add_option("-a", "--apikey", dest="apikey")
parser.add_option("-H", "--hostname", dest="hostname")
parser.add_option("-i", "--deviceid", dest="device_id")

(options, args) = parser.parse_args()

headers = {'Content-Type': 'application/json',
           'Accept': 'application/json',
           'Authorization': 'ExtraHop apikey={}'.format(options.apikey)}


url = 'https://{hostname}/api/v1/'.format(hostname=options.hostname)

get_device_url = url + "devices/{id}".format(id=options.device_id)

check_for_device = requests.get(get_device_url, headers=headers, verify=False)

if check_for_device.status_code == 200:
    print('device with id={} found.'.format(options.device_id))

    current_time_ms = int(round(time.time(), -3)) * 1000
    start_time_ms = current_time_ms - 3600*2 * 1000

    risk_scores = [random.randint(1,30),
                   random.randint(31,79),
                   random.randint(80, 100),
                   0,
                   None]
    NAMES = ["RISK SCORE YELLOW", "RISK SCORE ORANGE", 
             "RISK SCORE RED", "0 RISK SCORE",
             "NO RISK SCORE"]

    for i, score in enumerate(risk_scores):

        body = {
            "categories": ["sec", "sec.recon"],
            "description": "markdown!",
            "update_time": current_time_ms,
            "end_time": None,
            "title": NAMES[i],
            "start_time": start_time_ms,
            "hopcloud_id": str(random.randint(0,1000000000)),
            "type": "source_metrics_anomaly",
            "risk_score": score,
            "detail": {
                "metrics": [
                    {
                        "update_time": current_time_ms,
                        "end_time": None,
                        "stat_name": "http_server",
                        "field_name": "rsp",
                        "stat_cycle": "1hr",
                        "start_time": start_time_ms,
                        "object_type": "device",
                        "field_name": "rsp",
                        "object_id": int(options.device_id),
                        "anomaly_metadata": {
                            "baseline_min": 0,
                            "peak_deviation": 128005,
                            "peak_value": 128006,
                            "baseline_max": 1.0
                        }
                    }
                ]

            }
        }

        rsp = requests.post(url + "events", headers=headers,
                            data=json.dumps(body), verify=False)
        if rsp.status_code != 201:
            print(rsp.status_code, rsp.text)
        else:
            print(rsp.status_code, "Event created")

else:
    print("Device with supplied ID does not exist")
    print(check_for_device.status_code)
