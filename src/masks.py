def get_mask_card_number(card_number: int) -> str:
    """
    Маскирует номер банковской карты по формату 'XXXX XX** **** XXXX'.

    Args:
        card_number (int): Номер карты в виде числа.

    Returns:
        str: Маскированный номер карты.
    """
    card_str = str(card_number)
    if len(card_str) != 16 or not card_str.isdigit():
        raise ValueError("Номер карты должен состоять из 16 цифр.")
    return (
        f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"
    )


def get_mask_account(account_number: int) -> str:
    """
    Маскирует номер банковского счета по формату '**XXXX'.

    Args:
        account_number (int): Номер счета в виде числа.

    Returns:
        str: Маскированный номер счета.
    """
    account_str = str(account_number)
    if len(account_str) < 4 or not account_str.isdigit():
        raise ValueError("Номер счета должен содержать хотя бы 4 цифры.")
    return f"**{account_str[-4:]}"
