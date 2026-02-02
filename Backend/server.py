from fastapi import FastAPI
from datetime import date
import db_helper
from pydantic import BaseModel

class Expense(BaseModel):
    amount: float
    category: str
    notes: str
app = FastAPI()

@app.get("/expenses/{expense_date}",response_model=list[Expense])
def get_expense(expense_date: date):
    expenses =  db_helper.fetch_expenses(expense_date)

    return expenses

@app.post("/expenses/{expense_date}")
def add_or_update_expense(expense_date: date,expenses:list[Expense]):
    db_helper.delete_expenses(expense_date)
    for expense in expenses :
        db_helper.insert_expenses(expense_date,expense.amount,expense.category,expense.notes)

    return {"message":"Expense updated successfully"}



