import allure
import pytest
from data import ORDER_DATA
from methods.order_methods import OrderMethods


class TestCreateOrder:

    @allure.title('Создание заказа с цветом {color}')
    @pytest.mark.parametrize('color', [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    def test_create_order_with_different_colors(self, color):
        payload = {**ORDER_DATA, "color": color}

        response = OrderMethods.create(payload)

        assert response.status_code == 201
        assert "track" in response.json()