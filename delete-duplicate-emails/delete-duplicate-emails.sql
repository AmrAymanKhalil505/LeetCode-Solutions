# Write your MySQL query statement below
​
delete from Person 
where id in (
select * from (select p1.id
from Person p0 ,Person P1
where p0.email = p1.email 
and p1.id> p0.id) x
)
​
​
