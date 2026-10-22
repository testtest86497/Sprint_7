import allure
from data import Urls
import requests

class OrderMethods:

    @staticmethod
    @allure.step('Создать заказ')
    def create(payload):
        return requests.post(Urls.ORDERS, json=payload)

    @staticmethod
    @allure.step('Получить список заказов')
    def get_list_of_orders():
        return requests.get(Urls.ORDERS)

    