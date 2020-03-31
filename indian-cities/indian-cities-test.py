import unittest
import requests


class IndianCitiesTest(unittest.TestCase):
    service_url = "https://indian-cities-api-nocbegfhqg.now.sh"

    def test_for_endpoint_specific_city_inParams(self):
        responseBodyJson = requests.get(self.service_url + "/cities", params={"City": "SGM"}).json()
        args_ = responseBodyJson[0]
        assert args_["City"] == u"SGM"

    def test_For_Endpoint_Specific_District(self):
        responseBodyJson = requests.get(self.service_url + "/cities", params={"District": "Raigarh"}).json()
        args_ = responseBodyJson[0]
        assert args_["District"] == u"Raigarh"

    def test_For_Endpoint_Specific_State(self):
        responseBodyJson = requests.get(self.service_url + "/cities", params={"State": "Kerala"}).json()
        args_ = responseBodyJson[0]
        assert args_["State"] == u"Kerala"

    def test_For_Endpoint_search_State_like(self):
        responseBodyJson = requests.get(self.service_url + "/cities", params={"State_like": "Ker"}).json()
        for result in responseBodyJson:
            assert result["State"].startswith("Ker")

    def test_For_Endpoint_multiple_parameters_with_status_code(self):
        response = requests.get(self.service_url + "/cities", params={"State": "Rajasthan", "City": "SGM","District": "Ganganagar"})
        assert response.status_code == 200
        args_ = response.json()[0]
        assert args_["State"] == u"Rajasthan"
        assert args_["City"] == u"SGM"
        assert args_["District"] == u"Ganganagar"



