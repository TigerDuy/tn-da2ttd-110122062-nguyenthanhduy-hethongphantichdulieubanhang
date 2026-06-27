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

SELECT name FROM sys.databases;

SELECT TOP 10 * FROM DimCustomer;
SELECT TOP 10 * FROM DimProduct;
SELECT TOP 10 * FROM DimLocation;
SELECT TOP 10 * FROM DimTime;
SELECT COUNT(*) FROM FactSales;

SELECT TOP 10 * FROM FactSales;

DELETE FROM FactSales;
DELETE FROM DimCustomer;
DELETE FROM DimProduct;
DELETE FROM DimTime;
DELETE FROM DimLocation;

DBCC CHECKIDENT ('FactSales', RESEED, 0);
DBCC CHECKIDENT ('DimCustomer', RESEED, 0);
DBCC CHECKIDENT ('DimProduct', RESEED, 0);
DBCC CHECKIDENT ('DimTime', RESEED, 0);
DBCC CHECKIDENT ('DimLocation', RESEED, 0);