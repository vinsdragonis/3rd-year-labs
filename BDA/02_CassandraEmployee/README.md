1. Create a keyspace by name Employee

        create keyspace employee with replication={'class':'SimpleStrategy','replication_factor':'1'};
        use Employee;

2. Create a column family by name employee-Info with attributes Emp_Id Primary Key, Emp_Name, Designation, Date_of_Joining, Salary, Dept_Name

        create table employee_info(emp_id int, emp_name text,designation text, date_of_joining date,salary int, dept_name text,primary key((emp_id),salary))WITH CLUSTERING ORDER BY (salary ASC);

3. Insert the values into the table in batch.

        Begin batch 
        insert into employee_info(emp_id, emp_name, designation, date_of_joining,salary, dept_name) values(21,'Vineeth','Employee','2022-05-05',1500000,'Engineering');
        insert into employee_info(emp_id, emp_name, designation, date_of_joining,salary, dept_name) values(22,'Jahnavi','Employee','2022-06-07',1300000,'Testing');
        insert into employee_info(emp_id, emp_name, designation, date_of_joining,salary, dept_name) values(23,'Derek','Manager','2021-04-07',1400000,'Marketing');
        Apply batch;

        select * from employee_info;

4. Update Employee name and Department of Emp-Id 21

        update employee_Info Set emp_name='Vineeth' dept_name="Engineering" where emp_id=21;

5. Sort the details of Employee records based onsalary.

        select * from employee_info;

6. Alter the schema of the table Employee_Info  to add a column Projects which stores a set of Projects done by the corresponding Employee.

        alter table employee_info add projects set<text>;

7. Update the altered table to add project names.

        update employee_info set projects=projects+{'abc','xyz'} where emp_id=111 and salary=50000;
        update employee_info set projects=projects+{'std','yui'} where emp_id=121 and salary=100000;

8. Create a TTL of 15 seconds to display the values of Employees.

    	insert into employee_info(emp_id, emp_name,designation, date_of_joining,salary, dept_name) values(161,'Aishwarya','Employee','2022-05-05',50000,'design') using ttl 15;
