"""
create database joins;
use joins;

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50),
    city VARCHAR(50),
    gender VARCHAR(10),
    signup_date DATE
);

INSERT INTO customers VALUES
(101,'Aarav Sharma','Delhi','Male','2024-01-10'),
(102,'Priya Mehta','Mumbai','Female','2024-01-15'),
(103,'Rohan Verma','Pune','Male','2024-02-01'),
(104,'Sneha Kapoor','Jaipur','Female','2024-02-10'),
(105,'Kunal Singh','Bangalore','Male','2024-03-05'),
(106,'Anjali Gupta','Delhi','Female','2024-03-12'),
(107,'Rahul Jain','Mumbai','Male','2024-03-20'),
(108,'Neha Arora','Pune','Female','2024-04-01'),
(109,'Vikas Sharma','Delhi','Male','2024-04-10'),
(110,'Pooja Verma','Jaipur','Female','2024-04-15'),
(111,'Mohit Sharma','Delhi','Male','2024-05-01'),
(112,'Ritika Singh','Mumbai','Female','2024-05-08'),
(113,'Aman Gupta','Pune','Male','2024-05-15'),
(114,'Kriti Jain','Jaipur','Female','2024-05-20'),
(115,'Deepak Mehta','Bangalore','Male','2024-05-25');

select * from customers;

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_name VARCHAR(50),
    category VARCHAR(30),
    amount INT,
    order_date DATE,
    payment_mode VARCHAR(20)
);

INSERT INTO orders VALUES
(1001,101,'Laptop','Electronics',65000,'2025-01-05','UPI'),
(1002,102,'Headphones','Electronics',2500,'2025-01-06','Card'),
(1003,101,'Shoes','Fashion',3000,'2025-01-08','UPI'),
(1004,103,'Office Chair','Furniture',7000,'2025-01-10','Net Banking'),
(1005,105,'Television','Electronics',55000,'2025-01-12','Card'),
(1006,107,'Gaming Mouse','Electronics',2000,'2025-01-15','COD'),
(1007,108,'Study Table','Furniture',4500,'2025-01-18','UPI'),
(1008,109,'Microwave','Home Appliance',9000,'2025-01-20','Card'),
(1009,102,'Mobile Phone','Electronics',30000,'2025-01-22','UPI'),
(1010,110,'Washing Machine','Home Appliance',18000,'2025-01-25','Card'),
(1011,111,'Air Conditioner','Home Appliance',40000,'2025-01-27','UPI'),
(1012,112,'Smart Watch','Electronics',6000,'2025-01-29','COD'),
(1013,120,'Bluetooth Speaker','Electronics',3500,'2025-01-30','UPI'),
(1014,121,'Printer','Electronics',12000,'2025-02-01','Card'),
(1015,122,'Keyboard','Electronics',1500,'2025-02-03','UPI');

-- INNER JOIN (5 Questions)

-- 1. Display customer names and product names they purchased.
select c.customer_name,o.product_name
from customers as c
inner join orders as o
on c.customer_id=o.customer_id;

-- 2. Show customer city and order amount.
select c.city,o.amount
from customers as c
inner join orders as o
on c.customer_id=o.customer_id;

-- 3. Find customers who purchased Electronics products.
select c.customer_name,o.category
from customers as c
inner join orders as o
on c.customer_id=o.customer_id
where o.category='Electronics';

-- 4. Show customer name, product name, and payment mode
select c.customer_name,o.product_name,o.payment_mode
from customers as c
inner join orders as o
on c.customer_id=o.customer_id;

-- 5. Find the total amount spent by each customer.
select c.customer_name,sum(o.amount) as c
from customers as c
inner join orders as o
on c.customer_id=o.customer_id
group by c.customer_name;

-- LEFT JOIN (5 Questions)

-- 1. Show all customers and their orders.
select * 
from customers as c
left join orders as o
on c.customer_id = o.customer_id;

-- 2. Find customers who never placed an order.
select * 
from customers as c
left join orders as o
on c.customer_id = o.customer_id
where o.order_id is null;

-- 3. Count orders placed by each customer.
select c.customer_name,count(o.order_id)
from customers as c
left join orders as o
on c.customer_id = o.customer_id
group by c.customer_name;

-- 4. Find customers whose total spending is above ₹50,000.
select c.customer_name,sum(o.amount) as total_amount
from customers as c
left join orders as o
on c.customer_id=o.customer_id
group by c.customer_name
having total_amount>50000;

-- 5. Show customer names and latest order date.
select c.customer_name,max(o.order_date) as latest_order
from customers as c
left join orders as o
on c.customer_id=o.customer_id
group by c.customer_name;

-- RIGHT JOIN (5 Questions)

-- 1. Show all orders with customer names.
select * from customers as c
right join  orders as o
on c.customer_id = o.customer_id;

-- 2. Find orders that have no matching customer.
select * from customers as c
right join  orders as o
on c.customer_id = o.customer_id
where c.customer_id is null ;

-- 3. Count unmatched orders.
SELECT COUNT(o.order_id) AS unmatched_orders
FROM customers AS c
RIGHT JOIN orders AS o
ON c.customer_id = o.customer_id
WHERE c.customer_id IS NULL;

-- 4. Show revenue generated from unmatched orders.
SELECT SUM(o.amount) AS revenue
FROM customers AS c
RIGHT JOIN orders AS o
ON c.customer_id = o.customer_id
WHERE c.customer_id IS NULL;

-- 5. Display all orders regardless of customer availability.
SELECT *
FROM customers AS c
RIGHT JOIN orders AS o
ON c.customer_id = o.customer_id;

-- FULL OUTER JOIN (5 Questions)

-- 1. Show all customers and all orders.
select * from customers as c
left join  orders as o
on c.customer_id = o.customer_id
union
select * from customers as c
right join  orders as o
on c.customer_id = o.customer_id;

-- 2. Find unmatched customers and unmatched orders.
select * from customers as c
left join  orders as o
on c.customer_id = o.customer_id
where o.order_id is null
union
select * from customers as c
right join  orders as o
on c.customer_id = o.customer_id
where c.customer_id is null;

-- 3. Count matched records.
SELECT COUNT(*) AS matched_records
FROM customers AS c
INNER JOIN orders AS o
ON c.customer_id = o.customer_id;

-- 4. Categorize rows as Customer Only, Order Only, or Matched.
SELECT
    c.customer_name,
    o.order_id,
    CASE
        WHEN c.customer_id IS NULL THEN 'Order Only'
        WHEN o.order_id IS NULL THEN 'Customer Only'
        ELSE 'Matched'
    END AS status
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id

UNION

SELECT
    c.customer_name,
    o.order_id,
    CASE
        WHEN c.customer_id IS NULL THEN 'Order Only'
        WHEN o.order_id IS NULL THEN 'Customer Only'
        ELSE 'Matched'
    END
FROM customers c
RIGHT JOIN orders o
ON c.customer_id = o.customer_id
WHERE c.customer_id IS NULL;

-- 5. Display complete customer-order mapping.
SELECT *
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id

UNION

SELECT *
FROM customers c
RIGHT JOIN orders o
ON c.customer_id = o.customer_id
WHERE c.customer_id IS NULL;

-- CROSS JOIN (5 Questions)

-- 1. Generate all possible customer-product combinations.
select c.customer_name, o.product_name from customers as c
cross join  orders as o;

-- 2. Count total combinations.
select count(*) from customers as c
cross join  orders as o;

-- 3. Show every Delhi customer with every product.
SELECT c.customer_name,
       o.product_name
FROM customers AS c
CROSS JOIN orders AS o
WHERE c.city = 'Delhi';

-- 4. Generate promotional combinations.
SELECT c.customer_name,
       o.product_name
FROM customers AS c
CROSS JOIN orders AS o;

-- 5. Find all possible customer-category combinations.
SELECT c.customer_name,
       o.category
FROM customers AS c
CROSS JOIN
(
    SELECT DISTINCT category
    FROM orders
) AS o;

-- SELF JOIN (5 Questions)

-- 1. Find customers living in the same city.
select c1.customer_name, c1.city, c2.customer_name, c2.city from customers as c1
inner join customers as c2
on c1.customer_id != c2.customer_id
and c1.city=c2.city;

-- 2. Find customers with the same surname.
SELECT c1.customer_name,
       c2.customer_name
FROM customers AS c1
JOIN customers AS c2
ON SUBSTRING_INDEX(c1.customer_name,' ',-1)
 = SUBSTRING_INDEX(c2.customer_name,' ',-1)
AND c1.customer_id < c2.customer_id;

-- 3. Find pairs of customers from Delhi.
SELECT c1.customer_name,
       c2.customer_name,
       c1.city
FROM customers AS c1
JOIN customers AS c2
ON c1.city = c2.city
AND c1.customer_id < c2.customer_id
WHERE c1.city = 'Delhi';

-- 4. Compare customers who joined in the same month.
SELECT c1.customer_name,
       c2.customer_name,
       MONTH(c1.signup_date) AS signup_month
FROM customers AS c1
JOIN customers AS c2
ON MONTH(c1.signup_date) = MONTH(c2.signup_date)
AND c1.customer_id < c2.customer_id;

-- 5. Find all possible customer pairs from the same city.
SELECT c1.customer_name,
       c2.customer_name,
       c1.city
FROM customers AS c1
JOIN customers AS c2
ON c1.city = c2.city
AND c1.customer_id < c2.customer_id;

"""

