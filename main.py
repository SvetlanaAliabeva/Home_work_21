from entity.shop import Shop
from entity.store import Store

shop = Shop(
    items={
        "печенька": 3,
        "ноутбук": 2,
    }
)

store = Store(
    items={
        "печенька": 10,
        "ноутбук": 20,
    }
)


storages = {
    "магазин": shop,
    "склад": store,
}

def main():

    while True:
        for storage_name in storages:
            print(f"В {storage_name} храниться: {storages[storage_name].get_items()}")

        user_input = input(
            'Введите строку в формате "Доставить 3 печенька в магазин". \n'
            'Введите "stop" или "стоп", чтобы продолжить',
        )

        if user_input in ('stop', 'стоп'):
            break





if __name__ == '__main__':
    main()
