import pytest


@pytest.fixture
def wrong_card_number() -> int:
    """Возвращает неверный номер карты"""
    return 1


@pytest.fixture
def wrong_account_number() -> int:
    """Возвращается неверный номер аккаунта"""
    return 1


@pytest.fixture
def date_iso() -> str:
    return "2026-06-21"
