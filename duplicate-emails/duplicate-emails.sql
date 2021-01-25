/* Write your PL/SQL query statement below */
select DISTINCT(E1.Email) 
from Person E1,Person E2
where E1.Id!=E2.Id 
and E1.Email=E2.Email
