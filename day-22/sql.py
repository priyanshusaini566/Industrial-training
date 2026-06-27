"""
drop database project_sql;

create database project_sql_latest;
use project_sql_latest;

create table dim_customer
(customer_key int primary key,
first_name varchar(50),
last_name varchar(50),
gender varchar(30),
city varchar(50),
state varchar(50),
email varchar(50),
phone varchar(50)
);

select * from dim_customer;

show global variables;
set global local_infile= 1;

load data local infile "C:/Users/LENOVO/OneDrive/Desktop/industrial training/day-21/Retail_SQL_Project/dim_customer.csv"
into table dim_customer
fields terminated by ","
enclosed by '"'
lines terminated by "\n"
ignore 1 lines;


create table dim_date
(date_key int primary key,
full_date date
);

select * from dim_date;

show global variables;
set global local_infile= 1;

load data local infile "C:/Users/LENOVO/OneDrive/Desktop/industrial training/day-21/Retail_SQL_Project/dim_date.csv"
into table dim_date
fields terminated by ","
enclosed by '"'
lines terminated by "\n"
ignore 1 lines;


create table dim_employee
(employee_key int primary key,
employee_name varchar(50),
designation varchar(50),
store_key int
);

select * from dim_employee;

show global variables;
set global local_infile= 1;

load data local infile "C:/Users/LENOVO/OneDrive/Desktop/industrial training/day-21/Retail_SQL_Project/dim_employee.csv"
into table dim_employee
fields terminated by ","
enclosed by '"'
lines terminated by "\n"
ignore 1 lines;

create table dim_product
(product_key int primary key,
product_name varchar(50),
brand varchar(50),
category varchar(50),
price double
);

select * from dim_product;

show global variables;
set global local_infile= 1;

load data local infile "C:/Users/LENOVO/OneDrive/Desktop/industrial training/day-21/Retail_SQL_Project/dim_product.csv"
into table dim_product
fields terminated by ","
enclosed by '"'
lines terminated by "\n"
ignore 1 lines;


create table dim_store
(store_key int primary key,
store_name varchar(50),
city varchar(50),
state varchar(50)
);

select * from dim_store;

show global variables;
set global local_infile= 1;

load data local infile "C:/Users/LENOVO/OneDrive/Desktop/industrial training/day-21/Retail_SQL_Project/dim_store.csv"
into table dim_store
fields terminated by ","
enclosed by '"'
lines terminated by "\n"
ignore 1 lines;

create table fact_sales
(sale_id int primary key,
date_key int,
customer_key int,
product_key int,
store_key int,
employee_key int,
quantity int,
sales double,

foreign key(date_key) references dim_date(date_key),
foreign key(customer_key) references dim_customer(customer_key),
foreign key(product_key) references dim_product(product_key),
foreign key(store_key) references dim_store(store_key),
foreign key(employee_key) references dim_employee(employee_key)
);

select * from fact_sales;

show global variables;
set global local_infile= 1;

load data local infile "C:/Users/LENOVO/OneDrive/Desktop/industrial training/day-21/Retail_SQL_Project/fact_sales.csv"
into table fact_sales
fields terminated by ","
enclosed by '"'
lines terminated by "\n"
ignore 1 lines;

"""