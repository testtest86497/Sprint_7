import pytest
from helpers import generate_courier_data
from methods.courier_methods import CourierMethods


@pytest.fixture
def courier_data():
    """Генерирует данные курьера, но НЕ создаёт его.
    После теста удаляет курьера, если тот был создан."""
    payload = generate_courier_data()

    yield payload

    response = CourierMethods.login(payload)
    courier_id = response.json().get('id')
    if courier_id:
        CourierMethods.delete(courier_id)


@pytest.fixture
def courier(courier_data):
    """Создаёт курьера до теста. Удаление берёт на себя courier_data."""
    CourierMethods.create(courier_data)
    return courier_data