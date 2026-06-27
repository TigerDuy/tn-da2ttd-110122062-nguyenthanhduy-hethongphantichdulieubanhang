CREATE DATABASE SalesDataWarehouse;
GO
USE SalesDataWarehouse;
GO

CREATE TABLE DimCustomer (
    CustomerKey INT IDENTITY(1,1) PRIMARY KEY,
    CustomerID NVARCHAR(50),
    CustomerName NVARCHAR(255),
    Segment NVARCHAR(100)
);

CREATE TABLE DimProduct (
    ProductKey INT IDENTITY(1,1) PRIMARY KEY,
    ProductID NVARCHAR(50),
    ProductName NVARCHAR(255),
    Category NVARCHAR(100),
    SubCategory NVARCHAR(100)
);

CREATE TABLE DimTime (
    TimeKey INT IDENTITY(1,1) PRIMARY KEY,
    OrderDate DATE,
    Day INT,
    Month INT,
    Quarter INT,
    Year INT
);

CREATE TABLE DimLocation (
    LocationKey INT IDENTITY(1,1) PRIMARY KEY,
    Country NVARCHAR(100),
    State NVARCHAR(100),
    City NVARCHAR(100),
    Region NVARCHAR(100)
);

CREATE TABLE FactSales (
    SalesKey INT IDENTITY(1,1) PRIMARY KEY,

    CustomerKey INT,
    ProductKey INT,
    TimeKey INT,
    LocationKey INT,

    Sales DECIMAL(18,2),

    FOREIGN KEY (CustomerKey)
        REFERENCES DimCustomer(CustomerKey),

    FOREIGN KEY (ProductKey)
        REFERENCES DimProduct(ProductKey),

    FOREIGN KEY (TimeKey)
        REFERENCES DimTime(TimeKey),

    FOREIGN KEY (LocationKey)
        REFERENCES DimLocation(LocationKey)
);
