"""
# LIMIT OFFSET
select * from orders
limit 5;

select * from orders
limit 5 offset 2;

select * from orders
limit 5 offset 5;

select * from orders
limit 4 offset 2;

select * from orders
limit 2 offset 10;

select * from orders
limit 6 offset 4;

select * from orders
limit 3 offset 6;

select * from orders
limit 5 offset 8;

select * from orders
limit 2 offset 15;

select * from orders
limit 4 offset 10;

# OFFSET
select * from orders
limit 8 offset 2;

select * from orders
limit 8 offset 5;

select * from orders
limit 8 offset 10;

select * from orders
limit 8 offset 3;

select * from orders
limit 8 offset 7;

select * from orders
limit 8 offset 4;

select * from orders
limit 8 offset 6;

select * from orders
limit 8 offset 8;

select * from orders
limit 8 offset 1;

select * from orders
limit 8 offset 8;

# order by 
select * from orders
order by price;

update orders
set customer_name="nupur"
where order_id=4;

select * from orders;

select * from orders
order by price desc;

select * from orders
order by product;

select * from orders
order by order_date desc;

"""
