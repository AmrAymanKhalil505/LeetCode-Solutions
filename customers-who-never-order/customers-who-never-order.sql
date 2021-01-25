/* Write your PL/SQL query statement below */
select  Name as "Customers"
​
​
 from Customers
 Left Join
(select Distinct(  CustomerId )
 from Orders)
ON id = Customerid 
where CustomerId is Null
order by id
