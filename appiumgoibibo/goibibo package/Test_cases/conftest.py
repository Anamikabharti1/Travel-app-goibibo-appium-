import pytest
from appium import webdriver

@pytest.fixture(scope="function")
def appium_driver(request):
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'Anamikadevice',
        'appPackage': 'com.goibibo',
        'appActivity': '.common.HomeActivity',
        'udid': 'XKFULNZXOJRKGICM',
        'noReset': True,
        'ignoreHiddenApiPolicyError': True
    }

    driver = webdriver.Remote('http://localhost:4723', options=desired_caps)
    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
