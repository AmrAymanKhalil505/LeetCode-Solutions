/* Write your PL/SQL query statement below */
select J.Name as "Employee"
from Employee J, Employee M
where J.ManagerId = M.Id
and J.Salary > M.Salary
