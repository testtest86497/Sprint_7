import allure
from data import Urls
import requests

class CourierMethods:

    @staticmethod
    @allure.step('Создать курьера')
    def create(payload):
        return requests.post(Urls.COURIER, json=payload)

    @staticmethod
    @allure.step('Залогинить курьера')
    def login(payload):
        return requests.post(Urls.COURIER_LOGIN, json=payload)

    @staticmethod
    @allure.step('Удалить курьера')
    def delete(courier_id):
        return requests.delete(f'{Urls.COURIER}/{courier_id}')
    