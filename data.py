class Urls:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    COURIER = f'{BASE_URL}/api/v1/courier'
    COURIER_LOGIN = f'{BASE_URL}/api/v1/courier/login'
    ORDERS = f'{BASE_URL}/api/v1/orders'


class Messages:
    COURIER_EXISTS = 'Этот логин уже используется. Попробуйте другой.'
    NOT_ENOUGH_DATA_CREATE = 'Недостаточно данных для создания учетной записи'
    NOT_ENOUGH_DATA_LOGIN = 'Недостаточно данных для входа'
    ACCOUNT_NOT_FOUND = 'Учетная запись не найдена'


ORDER_DATA = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2026-12-01",
    "comment": "Saske, come back to Konoha"
}
