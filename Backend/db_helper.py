import mysql.connector
from contextlib import contextmanager


@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="killua@555",
        database="expense_manager"
    )

    cursor = connection.cursor(dictionary=True)
    try:
        yield cursor
        if commit:
            connection.commit()
    finally:

        cursor.close()
        connection.close()


def fetch_expenses(expense_date):
    with get_db_cursor() as cursor:

        query = "SELECT * FROM expenses WHERE expense_date = %s"
        cursor.execute(query, (expense_date,))
        expenses = cursor.fetchall()
        return expenses


def delete_expenses(expense_date):
    with get_db_cursor(commit=True) as cursor:
        # Changed 'date' to 'expense_date' to match the schema
        query = "DELETE FROM expenses WHERE expense_date = %s"
        cursor.execute(query, (expense_date,))


def insert_expenses(expense_date, amount, category, notes):
    with get_db_cursor(commit=True) as cursor:
        # Fixed the double 'VALUES' syntax error from your original script
        query = """
                INSERT INTO expenses (expense_date, amount, category, notes)
                VALUES (%s, %s, %s, %s) \
                """
        cursor.execute(query, (expense_date, amount, category, notes))

def fetch_expense_summary(start_date, end_date):
    with get_db_cursor() as cursor:
        cursor.execute(
            '''
            SELECT category,SUM(amount) as total FROM expenses WHERE expense_date
                BETWEEN %s and %s
                Group By category
            ''',
            (start_date, end_date)
        )
        data = cursor.fetchall()
        return data


if __name__ == "__main__":

    # expenses = fetch_expenses("2024-08-01")
    # print("Expenses found:", expenses)

    insert_expenses("2024-08-25",40,"Food","Ate a Sandwich")
    delete_expenses("2024-08-25")


    summary = fetch_expense_summary("2024-08-01","2024-08-05")
    for record in summary:
        print(record)



