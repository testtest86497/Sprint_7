import requests
from data import generate_random_string_for_login
import allure

class TestLogin:
    URL = 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Курьер может авторизоваться с валидными данными')
    def test_login_with_valid_credentials(self):
        payload = {
            "login": generate_random_string_for_login(10),
            "password": generate_random_string_for_login(10)
        }

        create_response = requests.post(self.URL + 'api/v1/courier', data=payload)

        login_response = requests.post(self.URL + 'api/v1/courier/login', data=payload)

        assert login_response.status_code == 200
        assert "id" in login_response.json()
        

    @allure.title('Курьер не может авторизоваться с невалидными данными')
    def test_login_with_invalid_credentials(self):
        payload = {
            "login": generate_random_string_for_login(10),
            "password": generate_random_string_for_login(10)
        }

        response = requests.post(self.URL + 'api/v1/courier/login', data=payload)

        assert response.status_code == 404
        assert response.json() == {"code": 404, "message": "Учетная запись не найдена"}


    @allure.title('Курьер не может авторизоваться с отсутствующими полями')
    def test_login_with_missing_fields(self):
        payload = {
            "login": generate_random_string_for_login(10),
            "password": generate_random_string_for_login(10)
        }
        
        create_response = requests.post(self.URL + 'api/v1/courier', data=payload)

        login_response = requests.post(self.URL + 'api/v1/courier/login', data={"login": payload["login"]})

        assert login_response.status_code == 400
        assert login_response.json() == {"code": 400, "message": "Недостаточно данных для входа"}
        