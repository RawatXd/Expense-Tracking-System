import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Backend import db_helper

def test_fetch_expense():
    expenses = db_helper.fetch_expenses("2024-08-15")

    assert len(expenses) == 1
    assert expenses[0]["amount"] == 10.0
    assert expenses[0]["category"] == "Shopping"
    assert expenses[0]["notes"] == "Buy Potatoes"

def test_fetch_expense_invalid():
    expenses = db_helper.fetch_expenses("15-08-9999")

    assert len(expenses) == 0

def test_fetch_expense_all():
    summary = db_helper.fetch_expense_summary("2099-01-01","2099-12-31")
    assert len(summary) == 0

