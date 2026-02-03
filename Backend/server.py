from fastapi import FastAPI,HTTPException
from datetime import date
import db_helper
from pydantic import BaseModel

app = FastAPI()

class Expense(BaseModel):
    amount: float
    category: str
    notes: str

class DateRange(BaseModel):
    start_date: date
    end_date : date


@app.get("/expenses/{expense_date}",response_model=list[Expense])
def get_expense(expense_date: date):
    expenses =  db_helper.fetch_expenses(expense_date)
    if expenses is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expenses database")
    return expenses

@app.post("/expenses/{expense_date}")
def add_or_update_expense(expense_date: date,expenses:list[Expense]):
    db_helper.delete_expenses(expense_date)
    for expense in expenses :
        db_helper.insert_expenses(expense_date,expense.amount,expense.category,expense.notes)

    return {"message":"Expense updated successfully"}

@app.post("/analytics/")
def get_analytics(date_range :DateRange):
    data = db_helper.fetch_expense_summary(date_range.start_date,date_range.end_date)

    if data is None:
        raise HTTPException(status_code=500, detail="Data not available")

    total =  sum([row['total'] for row in data])

    breakdown = {}
    for row in data:
        percentage = (row['total']/total)*100 if total != 0 else 0
        breakdown[row['category']] = {
            "total": row['total'],
            "percentage": percentage,
        }

    return breakdown