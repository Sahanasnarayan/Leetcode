# Write your MySQL query statement below
# distinct is to remove duplicates
select distinct author_id as id from Views
where author_id = viewer_id 
order by id;