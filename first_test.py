from appium import webdriver

desired_cap = {
    "app": "C:\\Users\\kajal.t\\ApiDemos-debug.apk",
    "deviceName": "Android Emulator",
    "platformName": "Android",
    "appPackage": "io.appium.android.apis",
    "appActivity": "io.appium.android.apis.ApiDemos"
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)