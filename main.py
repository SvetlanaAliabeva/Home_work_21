import capacity as capacity

from entity.courier import Courier
from entity.shop import Shop
from entity.store import Store
from entity.request import Request
from exceptions import BaseError

shop = Shop(
    items={
        "печенька": 3,
        "ноутбук": 2,
    },
)

store = Store(
    items={
        "печенька": 10,
        "ноутбук": 20,
    },
    capacity=100)


storages = {
    "магазин": shop,
    "склад": store,
}

def main():
    """
    :return:
    Выводит содержимое складов,
    запрашивает у пользователя строку,
    обрабатывает строку, проверяет на ошибки,
    определяет товар, количество, точки отправления и назначения
    """

    while True:
        for storage_name in storages:
            print(f"В {storage_name} храниться: {storages[storage_name].get_items()}")

        user_input = input(
            'Введите строку в формате "Доставить 3 печенька из склад в магазин". \n'
            'Введите "stop" или "стоп", чтобы остановить: \n',
        )

        if user_input in ('stop', 'стоп'):
            break

        try:
            request = Request(request_str=user_input, storages=storages)
        except BaseError as error:
            print(error.message)
            continue

        courier = Courier(request=request, storages=storages)

        try:
            courier.move()
        except BaseError as error:
            courier.cancel()
            print(error.message)




if __name__ == '__main__':
    main()
