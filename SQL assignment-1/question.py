"""

create database assignment;
use assignment;

CREATE TABLE orders (
order_id INT,
customer_name VARCHAR(50),
product VARCHAR(50),
category VARCHAR(50),
city VARCHAR(50),
quantity INT,
price INT,
order_date DATE
);
INSERT INTO orders VALUES
(1,'Amit','Laptop','Electronics','Delhi',1,60000,'2025-01-02'),
(2,'Riya','Phone','Electronics','Mumbai',2,30000,'2025-01-03'),
(3,'Rahul','Shoes','Fashion','Jaipur',3,2000,'2025-01-05'),
(4,'Sneha','Watch','Fashion','Delhi',1,5000,'2025-01-07'),
(5,'Karan','Tablet','Electronics','Pune',2,20000,'2025-01-10'),
(6,'Pooja','Bag','Fashion','Mumbai',4,1500,'2025-01-12'),
(7,'Arjun','Laptop','Electronics','Delhi',1,65000,'2025-01-13'),
(8,'Neha','Shoes','Fashion','Jaipur',2,2500,'2025-01-15'),
(9,'Rohit','Phone','Electronics','Delhi',1,28000,'2025-01-16'),
(10,'Simran','Bag','Fashion','Pune',3,1200,'2025-01-18'),
(11,'Vikas','Tablet','Electronics','Mumbai',1,22000,'2025-01-20'),
(12,'Anita','Watch','Fashion','Delhi',2,5500,'2025-01-22'),
(13,'Aman','Laptop','Electronics','Jaipur',1,62000,'2025-01-25'),
(14,'Meena','Shoes','Fashion','Mumbai',2,2100,'2025-01-26'),
(15,'Deepak','Phone','Electronics','Delhi',3,29000,'2025-01-28'),
(16,'Kavita','Bag','Fashion','Pune',1,1400,'2025-02-01'),
(17,'Manish','Tablet','Electronics','Delhi',2,21000,'2025-02-03'),
(18,'Nisha','Watch','Fashion','Jaipur',1,5200,'2025-02-05'),
(19,'Suresh','Laptop','Electronics','Mumbai',1,64000,'2025-02-07'),
(20,'Priya','Shoes','Fashion','Delhi',2,2300,'2025-02-09');

# SELECT
-- 1
select * from orders;
-- 2
select customer_name,product from orders;
-- 3
select order_id,product,price from orders;
-- 4
select * from orders
where city='Delhi';
-- 5
select product from orders;
-- 6
select order_date,customer_name from orders;
-- 7
select category,price from orders;
-- 8
select * from orders
where order_id<=5;
-- 9
select product,quantity from orders;
-- 10
select city,category from orders;

# WHERE
-- 1
select * from orders
where city='Delhi';

-- 2
select * from orders
where quantity>2;

-- 3
select product from orders
where price>30000;

-- 4
select * from orders
where city='Mumbai';

-- 5
select * from orders
where category='Fashion';

-- 6
select customer_name from orders
where product='Laptop';

-- 7
select * from orders
where price < 5000;

-- 8
select * from orders
where quantity=1;

-- 9
select * from orders
where city='Jaipur';

-- 10
select * from orders
where product='Phone';

# AGGREGATE FUCTION
-- 1
select count(*) as countorders from orders;

-- 2
select sum(quantity) as sumquantity from orders;

-- 3
select product,avg(price) as avgprice from orders group by product;

-- 4
select max(price) as maxprice from orders;

-- 5
select min(price) from orders;

-- 6
select sum(quantity*price) as totalsales from orders;

-- 7
select count(*) as countcustomers from orders;

-- 8
select max(quantity) as highest_quantity from orders;

-- 9
select avg(quantity) as avg_quantity from orders;

-- 10
select product,sum(price) as price_products from orders
group by product;

# GROUP BY
-- 1
select product,sum(quantity) as totalsold_quantity from 
orders group by product;

-- 2
select city,sum(quantity*price) as total_sales from orders
group by city;

-- 3
select category,count(*) as number_orders from orders
group by category;

-- 4
select product,avg(price) as avg_price from orders
group by product;

-- 5
select city,count(*) as count_bycity from orders
group by city;

-- 6
select category,sum(quantity) as total_quantity from orders
group by category;

-- 7
select product,sum(price) as ppp from orders 
group by product;

-- 8
select city,count(*) as customers from orders
group by city;

-- 9
select product,avg(quantity) as avg_quantity from orders
group by product;

-- 10
select category,count(*) as total_orders from orders
group by category;

# OFFSET
-- 1
select * from orders
limit 20 offset 2;

-- 2
select * from orders
limit 20 offset 5;

-- 3
select * from orders
limit 20 offset 10;

-- 4
select * from orders
limit 20 offset 3;

-- 5
select * from orders
limit 20 offset 7;

-- 6
select * from orders
limit 20 offset 4;

-- 7
select * from orders
limit 20 offset 6;

-- 8
select * from orders
limit 20 offset 8;

-- 9
select * from orders
limit 20 offset 1;

-- 10
select * from orders
limit 20 offset 9;

# LIMIT OFFSET
-- 1
select * from orders
limit 5;

-- 2
select * from orders
limit 3 offset 2;

-- 3
select * from orders
limit 5 offset 5;

-- 4
select * from orders
limit 4 offset 2;

-- 5
select * from orders
limit 2 offset 10;

-- 6
select * from orders
limit 6 offset 4;

-- 7
select * from orders
limit 3 offset 6;

-- 8
select * from orders
limit 5 offset 8;

-- 9
select * from orders
limit 2 offset 14;

-- 10
select * from orders
limit 4 offset 10;



"""