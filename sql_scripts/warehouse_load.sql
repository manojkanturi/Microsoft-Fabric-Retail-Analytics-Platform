


COPY INTO WH_UrbanThreads.dbo.FactSales
FROM "https://onelake.dfs.fabric.microsoft.com/UrbanThreads_Project/LH_UrbanThreads.Lakehouse/Tables/gold_fact_sales"
WITH
(
    FILE_TYPE = 'PARQUET'
);



COPY INTO dbo.Customer
FROM 'abfss://UrbanThreads_Project@onelake.dfs.fabric.microsoft.com/LH_UrbanThreads.Lakehouse/Tables/gold_dim_customer'
WITH
(
    FILE_TYPE = 'PARQUET'
);

gold_dim_date_df





-- This single command creates the table and loads the data.
CREATE TABLE dbo.Customer
AS
SELECT *
FROM
    OPENROWSET(
        BULK 'abfss://UrbanThreads_Project@onelake.dfs.fabric.microsoft.com/LH_UrbanThreads.Lakehouse/Tables/gold_dim_customer',
        FORMAT = 'DELTA'
    ) AS [rows];



-- This is the correct and worked for data loading from lakehouse to warehouse, simplified command for Fabric
CREATE TABLE dbo.Customer
AS
SELECT *
FROM LH_UrbanThreads.dbo.gold_dim_customer;


CREATE TABLE dbo.Date_WH
AS
SELECT *
FROM LH_UrbanThreads.dbo.gold_dim_date


CREATE TABLE dbo.Product
AS
SELECT *
FROM LH_UrbanThreads.dbo.gold_dim_product



CREATE TABLE dbo.Sales
AS
SELECT *
FROM LH_UrbanThreads.dbo.gold_fact_sales

DROP TABLE dbo.Date_WH;

DROP TABLE dbo.Sales

DROP TABLE dbo.Customer


SELECT * FROM dbo.Date_WH

SELECT * FROM dbo.Sales
