import HotelScreen

class HomeScreen:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        self.driver.find_element(by=locator['by'], value=locator['value']).click()

    def gotoHotels(self):
        self.click({"by": "xpath", "value": "//element[@id='hotels']"})
        return HotelScreen(self.driver)
