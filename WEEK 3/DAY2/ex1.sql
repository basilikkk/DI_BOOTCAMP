--EX1
--1 All items, ordered by price (lowest to highest)
-- select *
-- from items
-- order by (price) asc
--2Items with a price above 80 (80 included), ordered by price (highest to lowest).
-- select *
-- from items 
-- where price>80 or price=80
-- order by (price) desc
--3The first 3 customers in alphabetical order of the first name (A-Z) – exclude the primary key column from the results.
-- select first_name,last_name,email
-- from customers
-- order by(first_name) asc 
-- limit 3
--4All last names (no other columns!), in reverse alphabetical order (Z-A)
-- select last_name
-- from customers
-- order by(last_name)desc




