import json
import os
import requests

def read_transactions(file_path):

   """"(код функции read_transactions остается прежним)"""

def get_transaction_amount_rub(transaction):
    """
    Возвращает сумму транзакции в рублях.

    Args:
        transaction: Словарь с данными о транзакции.

    Returns:
        Сумма транзакции в рублях (float).
    """
    amount = transaction["amount"]
    currency = transaction.get("currency", "RUB")  # По умолчанию - рубли

    if currency != "RUB":
        # Получение курса валют с fixer.io (замените API_KEY на ваш ключ)
        response = requests.get(
            f"http://data.fixer.io/api/latest?access_key=YOUR_API_KEY&symbols=RUB,{currency}"
        )
        rates = response.json().get("rates", {})
        rub_rate = rates.get("RUB")
        currency_rate = rates.get(currency)
        if rub_rate and currency_rate:
            amount *= rub_rate / currency_rate
        else:
            raise ValueError("Не удалось получить курс валют")

    return amount
