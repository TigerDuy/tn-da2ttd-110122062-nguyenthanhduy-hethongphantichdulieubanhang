import pandas as pd
import pyodbc

# =========================
# CONNECT SQL SERVER
# =========================
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=SalesDataWarehouse;'
    'Trusted_Connection=yes;'
)

cursor = conn.cursor()

# =========================
# READ CSV
# =========================
df = pd.read_csv(
    'dataset/train.csv',
    encoding='latin1'
)

# =========================
# CLEAN DATA
# =========================
df.columns = df.columns.str.strip()

# =========================
# DIM CUSTOMER
# =========================
customers = df[
    ['Customer ID', 'Customer Name', 'Segment']
].drop_duplicates()

for index, row in customers.iterrows():

    cursor.execute("""
        INSERT INTO DimCustomer
        (CustomerID, CustomerName, Segment)
        VALUES (?, ?, ?)
    """,
    row['Customer ID'],
    row['Customer Name'],
    row['Segment']
    )

print("DimCustomer inserted successfully!")

# =========================
# DIM PRODUCT
# =========================
products = df[
    ['Product ID', 'Product Name', 'Category', 'Sub-Category']
].drop_duplicates()

for index, row in products.iterrows():

    cursor.execute("""
        INSERT INTO DimProduct
        (ProductID, ProductName, Category, SubCategory)
        VALUES (?, ?, ?, ?)
    """,
    row['Product ID'],
    row['Product Name'],
    row['Category'],
    row['Sub-Category']
    )

print("DimProduct inserted successfully!")

# =========================
# DIM TIME
# =========================
df['Order Date'] = pd.to_datetime(
    df['Order Date'],
    dayfirst=True
)

times = df[['Order Date']].drop_duplicates()

for index, row in times.iterrows():

    order_date = row['Order Date']

    day = order_date.day
    month = order_date.month
    quarter = (month - 1) // 3 + 1
    year = order_date.year

    cursor.execute("""
        INSERT INTO DimTime
        (OrderDate, Day, Month, Quarter, Year)
        VALUES (?, ?, ?, ?, ?)
    """,
    order_date,
    day,
    month,
    quarter,
    year
    )

print("DimTime inserted successfully!")

# =========================
# DIM LOCATION
# =========================
locations = df[
    ['Country', 'State', 'City', 'Region']
].drop_duplicates()

# =========================
# INSERT DIM LOCATION
# =========================
for index, row in locations.iterrows():

    cursor.execute("""
        INSERT INTO DimLocation
        (Country, State, City, Region)
        VALUES (?, ?, ?, ?)
    """,
    row['Country'],
    row['State'],
    row['City'],
    row['Region']
    )

print("DimLocation inserted successfully!")


# =========================
# FACT SALES
# =========================

for index, row in df.iterrows():

    # CUSTOMER KEY
    cursor.execute("""
        SELECT CustomerKey
        FROM DimCustomer
        WHERE CustomerID = ?
    """,
    row['Customer ID']
    )

    customer_key = cursor.fetchone()[0]

    # PRODUCT KEY
    cursor.execute("""
        SELECT ProductKey
        FROM DimProduct
        WHERE ProductID = ?
    """,
    row['Product ID']
    )

    product_key = cursor.fetchone()[0]

    # TIME KEY
    cursor.execute("""
        SELECT TimeKey
        FROM DimTime
        WHERE OrderDate = ?
    """,
    row['Order Date']
    )

    time_key = cursor.fetchone()[0]

    # LOCATION KEY
    cursor.execute("""
        SELECT LocationKey
        FROM DimLocation
        WHERE Country = ?
        AND State = ?
        AND City = ?
        AND Region = ?
    """,
    row['Country'],
    row['State'],
    row['City'],
    row['Region']
    )

    location_key = cursor.fetchone()[0]

    # INSERT FACT SALES
    cursor.execute("""
        INSERT INTO FactSales
        (
            CustomerKey,
            ProductKey,
            TimeKey,
            LocationKey,
            Sales
        )
        VALUES (?, ?, ?, ?, ?)
    """,
    customer_key,
    product_key,
    time_key,
    location_key,
    row['Sales']
    )

print("FactSales inserted successfully!")


# =========================
# SAVE CHANGES
# =========================
conn.commit()

conn.close()

print("ETL completed successfully!")