import pyodbc
from dbconfig import HOST_pf, USER_pf, PW_pf, DB_pf


def fetch_data():
    try:
        # Establish connection
        conn = pyodbc.connect(
            f'DRIVER={{SQL Server}};SERVER={HOST_pf};DATABASE={DB_pf};UID={USER_pf};PWD={PW_pf}'
        )
        cursor = conn.cursor()

        # Query the database
        query = "SELECT TOP 100 * FROM members"  # SQL Server uses TOP instead of LIMIT
        cursor.execute(query)

        # Fetch and print results
        columns = [column[0] for column in cursor.description]
        print(" | ".join(columns))  # Print column headers

        for row in cursor.fetchall():
            print(" | ".join(str(value) for value in row))

        # Close the connection
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    fetch_data()
