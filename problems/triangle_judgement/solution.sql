# Write your MySQL query statement below
SELECT *, iF(x+y>z and y+z>x and z+x>y, "Yes", "No") as triangle FROM Triangle