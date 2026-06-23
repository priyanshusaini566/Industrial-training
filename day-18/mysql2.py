"""
create database constraints_db_9am;
use constraints_db_9am;
create table department
(dept_id int primary key,
dept_name varchar(20) not null);

insert into department values
(1, "IT"),
(2, "R&D"),
(3, "admin");
create table employees
(emp_id int primary key auto_increment,
name varchar(50) not null,
salary float default 30000,
age int check(age>=18),
email varchar(50) unique,
d_id int,
foreign key (d_id) references department(dept_id));

insert into employees values
(101, "Mohit", default, 22, "m@gmail.com",1);

select * from employees;

insert into employees values
(default, "Mohit", 12000, 21, "moh@gmail.com",1);


insert into employees values
(default, "aman", 42000, 21, "n@gmail.com",1),
(default, "naman", 52000, 25, "nam@gmail.com",2),
(default, "pooja", 62000, 26, "p@gmail.com",3),
(default, "oggy", 100000, 27, "oggy@gmail.com",2);

"""