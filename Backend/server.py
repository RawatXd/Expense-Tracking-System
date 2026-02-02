from fastapi import FastAPI
from datetime import date
import db_helper
app = FastAPI()

@app.get("/expenses/{expense_date}")
def get_expense(expense_date: date):
    expenses =  db_helper.fetch_expenses(expense_date)

    return expenses

