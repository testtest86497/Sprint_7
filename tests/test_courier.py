import requests
from data import generate_random_string_for_login
import allure


class TestCourier:  
    URL = 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Создание нового курьера')
    def test_create_new_courier(self):
        payload = {
            "login": generate_random_string_for_login(10),
            "password": generate_random_string_for_login(10),
            "firstName": generate_random_string_for_login(10)
            }

        response = requests.post(self.URL + 'api/v1/courier', data=payload)

        assert response.status_code == 201
        assert response.json() == {"ok": True}


    @allure.title('Создание дубликата курьера')
    def test_create_duplicate_courier(self):
        payload = {
            "login": generate_random_string_for_login(10),
            "password": generate_random_string_for_login(10),
            "firstName": generate_random_string_for_login(10)
            }

        response1 = requests.post(self.URL + 'api/v1/courier', data=payload)
        response2 = requests.post(self.URL + 'api/v1/courier', data=payload)

        assert response1.status_code == 201
        assert response2.status_code == 409
        assert response2.json() == {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."}


    @allure.title('Создание курьера без логина')
    def test_create_courier_without_login(self):
        payload = {
            "password": generate_random_string_for_login(10),
            "firstName": generate_random_string_for_login(10)
        }

        response = requests.post(self.URL + 'api/v1/courier', data=payload)

        assert response.status_code == 400
        assert response.json() == {"code": 400, "message": "Недостаточно данных для создания учетной записи"}
