"""

Enter password: **********
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 16
Server version: 8.0.46 MySQL Community Server - GPL

Copyright (c) 2000, 2026, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> create database alter_revision;
Query OK, 1 row affected (0.05 sec)

mysql> use alter_revision;
Database changed
mysql> create table department(dept_id int,
    -> dept_name varchar(30));
Query OK, 0 rows affected (0.10 sec)

mysql> insert into department values(1,"CS"),(2,"IT"),(3,"AI");
Query OK, 3 rows affected (0.04 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> select * from department;
+---------+-----------+
| dept_id | dept_name |
+---------+-----------+
|       1 | CS        |
|       2 | IT        |
|       3 | AI        |
+---------+-----------+
3 rows in set (0.00 sec)

mysql> alter table department
    -> add column dept_emp_no int;
Query OK, 0 rows affected (0.06 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> select * from department;
+---------+-----------+-------------+
| dept_id | dept_name | dept_emp_no |
+---------+-----------+-------------+
|       1 | CS        |        NULL |
|       2 | IT        |        NULL |
|       3 | AI        |        NULL |
+---------+-----------+-------------+
3 rows in set (0.00 sec)

mysql> update department
    -> set dept_emp_no=13
    -> where dept_id=1;
Query OK, 1 row affected (0.04 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from department;
+---------+-----------+-------------+
| dept_id | dept_name | dept_emp_no |
+---------+-----------+-------------+
|       1 | CS        |          13 |
|       2 | IT        |        NULL |
|       3 | AI        |        NULL |
+---------+-----------+-------------+
3 rows in set (0.00 sec)

mysql> alter table department
    -> drop column dept_emp_no;
Query OK, 0 rows affected (0.06 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> select * from department;
+---------+-----------+
| dept_id | dept_name |
+---------+-----------+
|       1 | CS        |
|       2 | IT        |
|       3 | AI        |
+---------+-----------+
3 rows in set (0.00 sec)

mysql> alter table department
    -> add column no_emp int;
Query OK, 0 rows affected (0.07 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> update department
    -> set no_emp=16
    -> where dept_id=2;
Query OK, 1 row affected (0.04 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from department;
+---------+-----------+--------+
| dept_id | dept_name | no_emp |
+---------+-----------+--------+
|       1 | CS        |   NULL |
|       2 | IT        |     16 |
|       3 | AI        |   NULL |
+---------+-----------+--------+
3 rows in set (0.00 sec)

mysql> alter table department
    -> modify column no_emp decimal(10,2);
Query OK, 3 rows affected (0.10 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> select * from department;
+---------+-----------+--------+
| dept_id | dept_name | no_emp |
+---------+-----------+--------+
|       1 | CS        |   NULL |
|       2 | IT        |  16.00 |
|       3 | AI        |   NULL |
+---------+-----------+--------+
3 rows in set (0.00 sec)

mysql> alter table department
    -> change no_emp dept_emp_snkhya int;
Query OK, 3 rows affected (0.15 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> select * from department;
+---------+-----------+-----------------+
| dept_id | dept_name | dept_emp_snkhya |
+---------+-----------+-----------------+
|       1 | CS        |            NULL |
|       2 | IT        |              16 |
|       3 | AI        |            NULL |
+---------+-----------+-----------------+
3 rows in set (0.04 sec)

mysql> alter table department
    -> modify column dept_emp_snkhya decimal(10,2);
Query OK, 3 rows affected (0.14 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> select * from department;
+---------+-----------+-----------------+
| dept_id | dept_name | dept_emp_snkhya |
+---------+-----------+-----------------+
|       1 | CS        |            NULL |
|       2 | IT        |           16.00 |
|       3 | AI        |            NULL |
+---------+-----------+-----------------+
3 rows in set (0.00 sec)

mysql> alter table department
    -> add primary key(dept_id);
Query OK, 0 rows affected (0.17 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> desc department;
+-----------------+---------------+------+-----+---------+-------+
| Field           | Type          | Null | Key | Default | Extra |
+-----------------+---------------+------+-----+---------+-------+
| dept_id         | int           | NO   | PRI | NULL    |       |
| dept_name       | varchar(30)   | YES  |     | NULL    |       |
| dept_emp_snkhya | decimal(10,2) | YES  |     | NULL    |       |
+-----------------+---------------+------+-----+---------+-------+
3 rows in set (0.05 sec)

mysql> alter table department
    -> modify column dept_emp_snkhya default 30000;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'default 30000' at line 2
mysql> modify column dept_emp_snkhya decimal(10,2) default 30000;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'modify column dept_emp_snkhya decimal(10,2) default 30000' at line 1
mysql> modify column dept_emp_snkhya int default 30000;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'modify column dept_emp_snkhya int default 30000' at line 1
mysql> alter table department
    -> modify column dept_emp_snkhya int default 30000;
Query OK, 3 rows affected (0.11 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> select * from department;
+---------+-----------+-----------------+
| dept_id | dept_name | dept_emp_snkhya |
+---------+-----------+-----------------+
|       1 | CS        |            NULL |
|       2 | IT        |              16 |
|       3 | AI        |            NULL |
+---------+-----------+-----------------+
3 rows in set (0.00 sec)

mysql> desc department;
+-----------------+-------------+------+-----+---------+-------+
| Field           | Type        | Null | Key | Default | Extra |
+-----------------+-------------+------+-----+---------+-------+
| dept_id         | int         | NO   | PRI | NULL    |       |
| dept_name       | varchar(30) | YES  |     | NULL    |       |
| dept_emp_snkhya | int         | YES  |     | 30000   |       |
+-----------------+-------------+------+-----+---------+-------+
3 rows in set (0.05 sec)

mysql> alter table department
    -> add constraints ck
    -> unique(dept_name);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'ck
unique(dept_name)' at line 2
mysql> alter table department
    -> add constraint ck
    -> unique (dept_name);
Query OK, 0 rows affected (0.08 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> desc department;
+-----------------+-------------+------+-----+---------+-------+
| Field           | Type        | Null | Key | Default | Extra |
+-----------------+-------------+------+-----+---------+-------+
| dept_id         | int         | NO   | PRI | NULL    |       |
| dept_name       | varchar(30) | YES  | UNI | NULL    |       |
| dept_emp_snkhya | int         | YES  |     | 30000   |       |
+-----------------+-------------+------+-----+---------+-------+
3 rows in set (0.00 sec)

mysql> alter table department
    -> modify dept_name varchar(50) not null;
Query OK, 0 rows affected (0.16 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> desc department;
+-----------------+-------------+------+-----+---------+-------+
| Field           | Type        | Null | Key | Default | Extra |
+-----------------+-------------+------+-----+---------+-------+
| dept_id         | int         | NO   | PRI | NULL    |       |
| dept_name       | varchar(50) | NO   | UNI | NULL    |       |
| dept_emp_snkhya | int         | YES  |     | 30000   |       |
+-----------------+-------------+------+-----+---------+-------+
3 rows in set (0.00 sec)

mysql> alter table department
    -> add constraint ch_k
    -> check (dept_id >0);
Query OK, 3 rows affected (0.16 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> desc department;
+-----------------+-------------+------+-----+---------+-------+
| Field           | Type        | Null | Key | Default | Extra |
+-----------------+-------------+------+-----+---------+-------+
| dept_id         | int         | NO   | PRI | NULL    |       |
| dept_name       | varchar(50) | NO   | UNI | NULL    |       |
| dept_emp_snkhya | int         | YES  |     | 30000   |       |
+-----------------+-------------+------+-----+---------+-------+
3 rows in set (0.00 sec)

mysql> create table employee(emp_id int,emp_name varchar(50),d_id int);
Query OK, 0 rows affected (0.07 sec)

mysql> insert into employee values(1,"PS",1),(2,"ms",2);
Query OK, 2 rows affected (0.05 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> select * from employee;
+--------+----------+------+
| emp_id | emp_name | d_id |
+--------+----------+------+
|      1 | PS       |    1 |
|      2 | ms       |    2 |
+--------+----------+------+
2 rows in set (0.00 sec)

mysql> alter table employee
    -> add constraint add_fk
    -> foreign key(d_id) references department(d_id);
ERROR 3734 (HY000): Failed to add the foreign key constraint. Missing column 'd_id' for constraint 'add_fk' in the referenced table 'department'
mysql> alter table employee
    -> add constraint add_fk
    -> foreign key(d_id) references department(dept_id);
Query OK, 2 rows affected (0.11 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> desc employee;
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| emp_id   | int         | YES  |     | NULL    |       |
| emp_name | varchar(50) | YES  |     | NULL    |       |
| d_id     | int         | YES  | MUL | NULL    |       |
+----------+-------------+------+-----+---------+-------+
3 rows in set (0.00 sec)

"""