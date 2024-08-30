import pytest
import HomeScreen
import BaseTest


class Test_SearchHotel(BaseTest):
    @pytest.mark.parametrize("city", ["Delhi"])
    def test_search_hotel(self, city):
        logger = self.get_logger()
        logger.info(f"Starting test for city: {city}")

        home = HomeScreen(self.driver)
        home.gotoHotels().searchHotel(city)

        logger.info(f"Test completed for city: {city}")
