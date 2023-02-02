class BaseError(Exception):
    message = "Неизвестная ошибка"


class NotEnoughtSpaceError(BaseError):
    message = "Недостаточно места"

class UnknownProductError(BaseError):
    message = "Неизвестный товар"


class NotEnoughtProductError:
    message = "Недостаточно товара"


class InvalidRequestError(BaseError):
    message = "Неправильный запрос"


class UnknownStorageError(BaseError):
    message = "Неизвестный склад"


class TooManyDifferentProductsError(BaseError):
    message = "Слишком много разных товаров"




