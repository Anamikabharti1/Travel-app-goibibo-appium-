class HotelScreen:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        self.driver.find_element(by=locator['by'], value=locator['value']).click()

    def type(self, locator, value):
        self.driver.find_element(by=locator['by'], value=locator['value']).send_keys(value)

    def search_hotel(self, city):
        self.click({"by": "xpath", "value": "//element[@id='destination']"})
        self.type({"by": "xpath", "value": "//element[@id='searchtext']"}, city)
        self.click({"by": "xpath", "value": "//element[@id='selectlocation']"})
        self.click({"by": "xpath", "value": "//element[@id='searchbtn']"})
