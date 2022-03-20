import requests


class CarValidatorService:
    base_url = 'https://vpic.nhtsa.dot.gov/api/'

    def is_model_exist(self, make, model):
        url = self.base_url + f'vehicles/GetModelsForMake/{make}/?format=json'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for item in data['Results']:
                if item['Model_Name'] == model:
                    return True
        return False
