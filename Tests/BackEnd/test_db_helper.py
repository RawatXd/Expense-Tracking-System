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