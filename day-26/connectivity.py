import mysql.connector

# Database se connect karna
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="my password",
    database="project_sql_latest"
)

cursor = conn.cursor()
# Aapki likhi hui query run karna
cursor.execute("SELECT ROUND(SUM(sales), 2) FROM fact_sales")
total_sales = cursor.fetchone()

print(f"Hey Manager! Hamari total sales hai: {total_sales[0]}")
conn.close()