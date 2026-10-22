import allure
import pytest
from data import Messages
from methods.courier_methods import CourierMethods


class TestCourier:

    @allure.title('Курьера можно создать')
    def test_create_new_courier(self, courier_data):
        response = CourierMethods.create(courier_data)

        assert response.status_code == 201
        assert response.json() == {"ok": True}


    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_create_duplicate_courier(self, courier):
        response = CourierMethods.create(courier)

        assert response.status_code == 409
        assert response.json()["message"] == Messages.COURIER_EXISTS


    @allure.title('Нельзя создать курьера без поля {missing_field}')
    @pytest.mark.parametrize('missing_field', ['login', 'password'])
    def test_create_courier_without_required_field(self, courier_data, missing_field):
        payload = courier_data.copy()
        del payload[missing_field]

        response = CourierMethods.create(payload)

        assert response.status_code == 400
        assert response.json()["message"] == Messages.NOT_ENOUGH_DATA_CREATE
        