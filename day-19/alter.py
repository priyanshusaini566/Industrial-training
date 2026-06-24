"""
create database alter_db_9am;
use alter_db_9am;
create table department
(dept_id int ,
dept_name varchar(20));

insert into department values
(1, "IT"),
(2, "R&D"),
(3, "admin");
create table employees
(emp_id int ,
name varchar(50),
salary float,
age int ,
email varchar(50) ,
d_id int);

insert into employees values
(101, "Mohit", default, 22, "m@gmail.com",1);


insert into employees values
(102, "Mohit", 12000, 21, "moh@gmail.com",1);

select * from employees;
select * from department;

alter table employees
add column doj date;


alter table employees
drop column doj;

alter table employees
modify column salary decimal(10,2);

alter table employees
change column salary emp_salary decimal(10,2);


alter table employees
add primary key (emp_id);

alter table department
add primary key (dept_id);

alter table employees
add constraint fk_dept
foreign key(d_id) references department(dept_id);

"""