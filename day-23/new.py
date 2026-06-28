"""

Enter password: **********
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 14
Server version: 8.0.46 MySQL Community Server - GPL

Copyright (c) 2000, 2026, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> create database revision;
Query OK, 1 row affected (0.08 sec)

mysql> use revision;
Database changed
mysql> create table department(dept_id int primary key,dept_name varchar(30) not null);
Query OK, 0 rows affected (0.10 sec)

mysql> insert into department values(1,"CS"),(2,"IT"),(3,NULL);
ERROR 1048 (23000): Column 'dept_name' cannot be null
mysql> insert into department values(1,"CS"),(2,"IT"),(3,"AI");
Query OK, 3 rows affected (0.04 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> create table employee(emp_id int,
    -> emp_name varchar(40),
    -> age,
    -> sal
    ->
    -> ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ',
sal' at line 3
mysql> create table employee(emp_id int primary key,emp_name varchar(40) not null,emp_salary float default 30000,age int check(age>=18),email varchar(40) unique,d_id int
    -> foreign key(d_id) references department(dept_id));
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'foreign key(d_id) references department(dept_id))' at line 2
mysql> create table employee(emp_id int primary key,emp_name varchar(40) not null,emp_salary float default 30000,age int check(age>=18),email varchar(40) unique,d_id int,foreign key(d_id) references department(dept_id));
Query OK, 0 rows affected (0.12 sec)

mysql> select * from employees;
ERROR 1146 (42S02): Table 'revision.employees' doesn't exist
mysql> select * from employee;
Empty set (0.00 sec)

mysql> select * from department;
+---------+-----------+
| dept_id | dept_name |
+---------+-----------+
|       1 | CS        |
|       2 | IT        |
|       3 | AI        |
+---------+-----------+
3 rows in set (0.00 sec)

mysql> drop table employee;
Query OK, 0 rows affected (0.07 sec)

mysql> create table employee(emp_id int auto_increment,emp_name varchar(40) not null,emp_salary float default 30000,age int check(age>=18),email varchar(40) unique,d_id int,foreign key(d_id) references department(dept_id));
ERROR 1075 (42000): Incorrect table definition; there can be only one auto column and it must be defined as a key
mysql> create table employee(emp_id int primary key auto_increment,emp_name varchar(40) not null,emp_salary float default 30000,age int check(age>=18),email varchar(40) unique,d_id int,foreign key(d_id) references department(dept_id));
Query OK, 0 rows affected (0.10 sec)

mysql> insert into employee values(1,"PS",100000000,16,"ps@gmail.com",1);
ERROR 3819 (HY000): Check constraint 'employee_chk_1' is violated.
mysql> insert into employee values(1,"PS",100000000,20,"ps@gmail.com",1),(2,"MS",default,22,"ms@gmail.com",2;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' at line 1
mysql> insert into employee values(1,"PS",100000000,20,"ps@gmail.com",1),(2,"MS",default,22,"ms@gmail.com",2);
Query OK, 2 rows affected (0.04 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> select * from employee;
+--------+----------+------------+------+--------------+------+
| emp_id | emp_name | emp_salary | age  | email        | d_id |
+--------+----------+------------+------+--------------+------+
|      1 | PS       |  100000000 |   20 | ps@gmail.com |    1 |
|      2 | MS       |      30000 |   22 | ms@gmail.com |    2 |
+--------+----------+------------+------+--------------+------+
2 rows in set (0.00 sec)


"""