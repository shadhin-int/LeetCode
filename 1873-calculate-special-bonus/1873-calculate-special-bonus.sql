# Write your MySQL query statement below
select employee_id, if(
    employee_id % 2 != 0 AND name NOT LIKE 'M%',salary, 0
) as bonus from Employees; 
