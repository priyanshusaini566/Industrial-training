"""

create database subqueries;
use subqueries;


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


select c.customer_name,o.product_name
from customers as c
inner join orders as o
on c.customer_id=o.customer_id;

select c.city,o.amount
from customers as c
inner join orders as o
on c.customer_id=o.customer_id;

select c.customer_name,o.category
from customers as c
inner join orders as o
on c.customer_id=o.customer_id
where o.category="Electronics";

select c.customer_name,o.product_name,o.payment_mode
from customers as c
inner join orders as o
on c.customer_id=o.customer_id;

select c.customer_name,sum(o.amount) as c
from customers as c
inner join orders as o
on c.customer_id=o.customer_id
group by c.customer_name;

select c.* ,o.*
from customers as c
left join orders as o
on c.customer_id=o.customer_id;

select * from customers as c
left join orders as o
on c.customer_id=o.customer_id
where o.order_id is null;

select c.customer_name,count(o.customer_id)
from customers as c
left join orders as o
on c.customer_id=o.customer_id
group by c.customer_name;

select c.customer_name,sum(o.amount) as s
from customers as c
left join orders as o
on c.customer_id=o.customer_id
group by c.customer_name
having sum(o.amount)>50000;

select c.customer_name,max(o.order_date)
from customers as c
left join orders as o
on c.customer_id=o.customer_id
group by c.customer_name;

select *
from customers as c
right join orders as o
on c.customer_id=o.customer_id;

select sum(o.amount) from 
customers as c
right join orders as o
on c.customer_id=o.customer_id
where c.customer_id is null;

select * from customers as c
right join orders as o
on c.customer_id=o.customer_id;

-- Full outer join
select c.*,o.* from 
customers as c
left join orders as o
on c.customer_id=o.customer_id

union
select c.*,o.* from
customers as c
right join orders as o
on c.customer_id=o.customer_id;

select * 
from customers as c
left join orders as o
on c.customer_id=o.customer_id
where o.order_id is null

union
select * from customers as c
right join orders as o
on c.customer_id=o.customer_id
where c.customer_id is null;


select *
from customers as c
left join orders as o
on c.customer_id=o.customer_id
where o.order_id is not null
union
select c.*,o.* from
customers as c
right join orders as o
on c.customer_id=o.customer_id
where c.customer_id is not null;

select c.customer_name,o.order_id,
case  
when c.customer_name is null then 'order only'
when o.order_id is null then 'customer only'
else 'matched'
end as category
from customers as c
left join orders as o
on c.customer_id=o.customer_id
union
select c.customer_name,o.order_id,
case
 when c.customer_id is null then 'order only'
 when o.order_id is null then 'customer only'
else  'matched'
end as category
from customers as c
right join orders as o
on c.customer_id=o.customer_id;


select c.*,o.*
from customers as c
left join orders as o
on c.customer_id=o.customer_id

union
select c.*,o.*
from customers as c
right join orders as o
on c.customer_id=o.customer_id;

select c.*,o.*
from orders as o
cross join customers as c;

select count(*) as count_combinations
from customers as c
cross join orders as o;

select c.customer_name,c.city,o.product_name
from customers as c
cross join orders as o
where c.city='Delhi';

select c.customer_name,o.category
from customers as c
cross join (select distinct category
from orders) as o;


select c.customer_name,o.product_name
from customers as c
cross join (select distinct product_name
from orders)
as o;

select c1.customer_name,c1.city,c2.customer_name,c2.city 
from customers as c1
inner join customers as c2
on c1.customer_id!=c2.customer_id
and c1.city=c2.city;

SELECT c1.customer_name,
       c2.customer_name,
       c1.last_name
FROM customers AS c1
INNER JOIN customers AS c2
ON c1.last_name = c2.last_name
AND c1.customer_id < c2.customer_id;

select c1.customer_name,c2.customer_name,c1.last_name
from customers as c1
inner join customers as c2
on c1.last_name=c2.last_name
and c1.customer_id<c2.customer_id;

select c1.customer_name,c2.customer_name,c2.city
from customers as c1
inner join customers as c2
on c1.city=c2.city
and c1.city='Delhi'
and c1.customer_id<c2.customer_id;


select c1.customer_name,c2.customer_name, DATE_FORMAT(c1.signup_date, '%Y-%m') AS signup_month
from customers as c1
inner join customers as c2
on date_format(c1.signup_date,'%y-%m')=date_format(c2.signup_date,'%y-%m')
and c1.customer_id<c2.customer_id;

select c1.customer_name,c2.customer_name,c1.city
from customers as c1
inner join customers as c2
on c1.city=c2.city
and c1.customer_id<c2.customer_id;

"""