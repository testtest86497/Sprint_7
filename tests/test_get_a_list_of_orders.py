import requests
import allure

class TestListOfOrders:
    URL = 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Получение списка заказов')
    def test_get_list_of_orders(self):
        response = requests.get(self.URL + 'api/v1/orders')

        assert response.status_code == 200
        assert "orders" in response.json()
