from datetime import datetime
from src.masks import get_mask_card_number, get_mask_account


def get_date(date_str: str) -> str:
    """
    Преобразование строки с датой в формат "ДД.ММ.ГГГГ".

    :param date_str: дата в формате "2024-03-11T02:26:18.671407"
    :return: дата в формате "ДД.ММ.ГГГГ" (например, "11.03.2024")
    """
    try:
        # Парсим строку в объект datetime
        date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
        # Форматируем объект datetime в строку в нужном формате
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError("Некорректный формат даты. Пожалуйста, предоставьте дату в формате 'YYYY-MM-DDTHH:MM:SS.ssssss'.")
    except Exception as e:
        raise Exception(f"Произошла ошибка при обработке даты: {str(e)}")


def mask_account_card(number: str) -> str:
    """
    Маскировка номера счёта или карты.

    :param number: номер счёта или номер карты
    :return: замаскированный номер
    """
    try:
        if "Счет" in number:
            # Предполагаем, что номер счёта идет после "Счет", и обрезаем его
            account_number = number[5:].strip()
            return get_mask_account(int(account_number))
        else:
            # Предполагаем, что номер карты последний элемент в строке
            card_number = number.split()[-1].strip()
            return get_mask_card_number(int(card_number))
    except ValueError:
        # Если не удается преобразовать строку в число
        raise ValueError("Некорректный номер. Пожалуйста, предоставьте валидный номер.")
    except Exception as e:
        # Общая обработка неожиданных ошибок
        raise Exception(f"Произошла ошибка: {str(e)}")