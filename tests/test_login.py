import allure
import pytest
from data import Messages
from helpers import generate_courier_data
from methods.courier_methods import CourierMethods


class TestLogin:

    @allure.title('Курьер может авторизоваться')
    def test_login_with_valid_credentials(self, courier):
        response = CourierMethods.login({
            "login": courier["login"],
            "password": courier["password"]
        })

        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title('Авторизация несуществующего курьера возвращает 404')
    def test_login_with_invalid_credentials(self):
        payload = generate_courier_data()

        response = CourierMethods.login({
            "login": payload["login"],
            "password": payload["password"]
        })

        assert response.status_code == 404
        assert response.json()["message"] == Messages.ACCOUNT_NOT_FOUND

    @allure.title('Авторизация с пустым полем {empty_field} возвращает 400')
    @pytest.mark.parametrize('empty_field', ['login', 'password'])
    def test_login_with_empty_field(self, courier, empty_field):
        payload = {
            "login": courier["login"],
            "password": courier["password"]
        }
        payload[empty_field] = ''

        response = CourierMethods.login(payload)

        assert response.status_code == 400
        assert response.json()["message"] == Messages.NOT_ENOUGH_DATA_LOGIN
        