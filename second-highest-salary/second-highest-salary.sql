/* Write your PL/SQL query statement below */
​
​
​
/*
select salary as "SecondHighestSalary" 
from(select rownum as r,salary 
from(select  e.salary
from Employee e
order by e.salary)
    )
where r =2 */
/*
select salary as "SecondHighestSalary" 
from(select rownum as r,salary 
from(select  e.salary
from Employee e
order by e.salary)
  )
where r =2
*/
​
select salary as "SecondHighestSalary"
​
from(
    select  rownum as r, salary
    from (select distinct (salary) from Employee order by salary desc)  
    union 
    select case  when count (*)>1 then -1 else 2 end  as r  , null as salary
    from (select distinct (salary) from Employee)  
    )
 
where r =2
​
​
​
