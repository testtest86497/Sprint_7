import requests
import pytest
import allure

class TestCreateOrder:

    @allure.title('Создание заказа с цветом {color}')
    @pytest.mark.parametrize("color", [
        (["BLACK"]),
        (["GREY"]),
        (["BLACK", "GREY"]),
        ([])
    ])
    def test_color_black(self, color):
        url = 'https://qa-scooter.praktikum-services.ru/'

        payload = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": color
}
        response = requests.post(url + 'api/v1/orders', json=payload)

        assert response.status_code == 201
        assert "track" in response.json()
