--EX2
--1  In the dvdrental database write a query to select all the columns from the “customer” table.

--select *
--from customer

--2 Write a query to display the nameselect first_name + first_name as full_name
-- SELECT first_name || ' ' || last_name AS full_name
-- FROM customer;


--3 Lets get all the dates that accounts were created. Write a query to select all the create_date from the “customer” table (there should be no duplicates).
-- select distinct create_date
-- from customer

--4 Write a query to get all the customer details from the customer table, it should be displayed in descending order by their first name.
-- select *
-- from customer 
-- order by (first_name) desc
--5 Write a query to get the film ID, title, description, year of release and rental rate in ascending order according to their rental rate.
-- select film_id,tittle,description, release_year, rental_rate
-- from film
-- order by(rental_rate) asc
--6 Write a query to get the address, and the phone number of all customers living in the Texas district, these details can be found in the “address” table.

-- select cus.customer_id,cus.first_name,cus.last_name, ad.district
-- from customer as cus
-- left join address as ad
-- on cus.address_id=ad.address_id
-- where district ='Texas'

--7 Write a query to retrieve all movie details where the movie id is either 15 or 150.
-- select *
-- from film as f
-- left join film_category as fc 
-- on f.film_id=fc.film_id

--8 Write a query which should check if your favorite movie exists in the database. Have your query get the film ID, title, description, length and the rental rate, these details can be found in the “film” table.
-- SELECT film_id, title, description, length, rental_rate
-- FROM film
-- WHERE title ILIKE '%Shark%';

--9 Write a query to get the film ID, title, description, length and the rental rate of all the movies starting with the two first letters of your favorite movie.
-- SELECT *
-- FROM film
-- WHERE title ILIKE 'Sh%';
--10 Write a query which will find the 10 cheapest movies.
-- SELECT *
-- FROM film
-- order by (replacement_cost) asc
-- limit 10
--11 Write a query which will find the next 10 cheapest movies.
-- SELECT *
-- FROM film
-- ORDER BY replacement_cost ASC
-- OFFSET 10 ROWS FETCH NEXT 10 ROWS ONLY;

--12 Write a query which will join the data in the customer table and the payment table.
--  select c.first_name || ' ' || c.last_name AS full_name, p.amount, p.payment_date 
--  from customer as c
--  left join payment as p on c.customer_id=p.customer_id
--13  Write a query to get all the movies which are not in inventory.
-- select f.title, f.description 
-- from film as f
-- left join inventory as i on f.film_id = i.film_id
-- where i.film_id is null
--14 Write a query to find which city is in which country.
-- select c.city,co.country
-- from city as  c 
-- left join country as co on  c.country_id = co.country_id
--15 Write a query to get the customer’s id, names (first and last), the amount and the date of payment ordered by the id of the staff member who sold them the dvd.
SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    p.amount,
    p.payment_date,
    s.staff_id
FROM 
    customer c
JOIN 
    payment p ON c.customer_id = p.customer_id
JOIN 
    staff s ON p.staff_id = s.staff_id
ORDER BY 
    s.staff_id;





