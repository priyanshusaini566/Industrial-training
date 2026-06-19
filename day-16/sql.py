"""

Enter password: **********
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 32
Server version: 8.0.46 MySQL Community Server - GPL

Copyright (c) 2000, 2026, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| college            |
| company_re_9am     |
| information_schema |
| mysql              |
| new                |
| performance_schema |
| sakila             |
| sys                |
| world              |
+--------------------+
9 rows in set (0.00 sec)

mysql> create database student;
Query OK, 1 row affected (0.01 sec)

mysql> use student;
Database changed
mysql> create table s_details(name varchar(30),age int,class int,marks int);
Query OK, 0 rows affected (0.03 sec)

mysql> insert into s_details values("priyanshu",20,12,96),("muskan",22,14,99);
Query OK, 2 rows affected (0.01 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> select * from s_details;
+-----------+------+-------+-------+
| name      | age  | class | marks |
+-----------+------+-------+-------+
| priyanshu |   20 |    12 |    96 |
| muskan    |   22 |    14 |    99 |
+-----------+------+-------+-------+
2 rows in set (0.00 sec)

mysql> update s_details
    -> set name="sushil"
    -> where age=20;
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from s_details;
+--------+------+-------+-------+
| name   | age  | class | marks |
+--------+------+-------+-------+
| sushil |   20 |    12 |    96 |
| muskan |   22 |    14 |    99 |
+--------+------+-------+-------+
2 rows in set (0.00 sec)

mysql>

"""
