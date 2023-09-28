# Write your MySQL query statement below
SELECT * FROM Cinema 
WHERE MOD(id,2) =1 and description <> 'boring'
order by rating DESC;