/* Write your PL/SQL query statement below */
select FirstName, LastName, City, State
from  Person P Left Join Address A
ON P.PersonId = A.PersonId 
