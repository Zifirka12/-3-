import unittest

from utils import read_transactions, get_transaction_amount_rub

class TestUtils(unittest.TestCase):

    def test_read_transactions_empty_file(self):
        # Создаем пустой файл для теста
        with open("test_data.json", "w") as f:
            f.write("[]")
        self.assertEqual(read_transactions("test_data.json"), [])

    def test_read_transactions_invalid_json(self):
        # Создаем файл с невалидным JSON
        with open("test_data.json", "w") as f:
            f.write("{")
        self.assertEqual(read_transactions("test_data.json"), [])

    def test_read_transactions_file_not_found(self):
        self.assertEqual(read_transactions("nonexistent_file.json"), [])

    def test_get_transaction_amount_rub_usd(self):
        transaction = {"amount": 100, "currency": "USD"}
        self.assertEqual(get_transaction_amount_rub(transaction), 7500)

    def test_get_transaction_amount_rub_eur(self):
        # Добавьте в utils.py логику для конвертации EUR в RUB с фиксированным курсом
        # например:
        # elif currency == "EUR":
        #     amount *= 85  # Задаем фиксированный курс 1 EUR = 85 RUB
        transaction = {"amount": 50, "currency": "EUR"}
        self.assertEqual(get_transaction_amount_rub(transaction), 4250)  # Измените ожидаемое значение, если необходимо

    def test_get_transaction_amount_rub_rub(self):
        transaction = {"amount": 1000, "currency": "RUB"}
        self.assertEqual(get_transaction_amount_rub(transaction), 1000)
