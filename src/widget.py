from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """
    Функция маскирует номер счета или карты
    """
    number = ""
    account_card_data = ""

    for i in data:
        if i.isdigit():
            number += i
        else:
            account_card_data += i

    if len(number) == 16:
        masked_number = get_mask_card_number(number)
    else:
        masked_number = get_mask_account(number)

    return account_card_data + masked_number


def get_date(date: str) -> str:
    """
    Функция возвращает дату в формате ДД.ММ.ГГГГ
    """
    data_list = [date[8:10], date[5:7], date[:4]]
    return ".".join(data_list)
