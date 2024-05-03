import json
import os
from typing import List, Dict, Union

import requests


def read_transactions(file_path: str) -> List[Dict[str, Union[str, float]]]:
    """
    Читает данные о транзакциях из JSON-файла.

    Args:
        file_path: Путь к JSON-файлу.

    Returns:
        Список словарей с данными о транзакциях.
    """
    if not os.path.exists(file_path):
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
        except json.JSONDecodeError:
            return []


def get_transaction_amount_rub(transaction: Dict[str, Union[str, float]]) -> float:
    """
    Возвращает сумму транзакции в рублях.

    Args:
        transaction: Словарь с данными о транзакции.

    Returns:
        Сумма транзакции в рублях (float).
    """
    amount = transaction["amount"]
    currency = transaction.get("currency", "RUB")

    if currency != "RUB":
        # Используем Fixer.io API (замените YOUR_API_KEY на ваш ключ)
        response = requests.get(
            f"http://data.fixer.io/api/latest?access_key=YOUR_API_KEY&symbols=RUB,{currency}"
            #Ключи платные на сайте , есть бесплатный , но я ему не доверяю
        )
        if response.status_code != 200:
            raise requests.exceptions.RequestException(f"Ошибка API: {response.status_code}")

        rates = response.json().get("rates", {})
        rub_rate = rates.get("RUB")
        currency_rate = rates.get(currency)
        if rub_rate and currency_rate:
            amount *= rub_rate / currency_rate
        else:
            raise ValueError(f"Не удалось получить курс для валюты {currency}")

    return amount
