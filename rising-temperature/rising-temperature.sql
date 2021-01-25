/* Write your PL/SQL query statement below */
select w0.iD as "Id"
from Weather w0, Weather w1
where  to_date(w0.recordDate)-1 = to_date(w1.recordDate) and
to_number (w0.Temperature) > to_number (w1.Temperature)
​
/*select ID,to_date(recordDate-1)
from Weather*/
​
