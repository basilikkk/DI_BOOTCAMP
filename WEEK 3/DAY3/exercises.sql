-- SELECT * FROM language;


-- SELECT f.title, f.description, l.name AS language_name
-- FROM film f
-- JOIN language l ON f.language_id = l.language_id;


-- SELECT f.title, f.description, l.name AS language_name
-- FROM language l
-- LEFT JOIN film f ON l.language_id = f.language_id;

-- CREATE TABLE new_film (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(50)
-- );

-- INSERT INTO new_film (name) VALUES ('New Film 1'), ('New Film 2'), ('New Film 3');



-- CREATE TABLE customer_review (
--     review_id SERIAL PRIMARY KEY,
--     film_id INTEGER REFERENCES new_film(id) ON DELETE CASCADE,
--     language_id INTEGER REFERENCES language(language_id),
--     title VARCHAR(100),
--     score INTEGER CHECK(score >= 1 AND score <= 10),
--     review_text TEXT,
--     last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );

-- INSERT INTO customer_review (film_id, language_id, title, score, review_text)
-- VALUES 
-- (1, 1, 'Great Movie!', 9, 'I loved this film! It was amazing.'),
-- (2, 2, 'Not Bad', 7, 'The film was good but could be better.');


-- INSERT INTO customer_review (film_id, language_id, title, score, review_text)
-- VALUES 
-- (1, 1, 'Great Movie!', 9, 'I loved this film! It was amazing.'),
-- (2, 2, 'Not Bad', 7, 'The film was good but could be better.');


-- #ex2
-- UPDATE film SET language_id = 2 WHERE film_id = 1;
-- UPDATE film SET language_id = 3 WHERE film_id = 2;


-- DROP TABLE customer_review;


-- -- SELECT COUNT(*)
-- -- FROM rental
-- -- WHERE return_date IS NULL;


-- -- SELECT f.title, f.rental_rate
-- -- FROM rental r
-- -- JOIN inventory i ON r.inventory_id = i.inventory_id
-- -- JOIN film f ON i.film_id = f.film_id
-- -- WHERE r.return_date IS NULL
-- -- ORDER BY f.rental_rate DESC
-- -- LIMIT 30;


-- SELECT f.title
-- FROM film f
-- JOIN film_actor fa ON f.film_id = fa.film_id
-- JOIN actor a ON fa.actor_id = a.actor_id
-- WHERE f.description ILIKE '%sumo%' AND a.first_name = 'Penelope' AND a.last_name = 'Monroe';


-- SELECT title
-- FROM film
-- WHERE length < 60 AND rating = 'R';


-- SELECT f.title
-- FROM rental r
-- JOIN inventory i ON r.inventory_id = i.inventory_id
-- JOIN film f ON i.film_id = f.film_id
-- JOIN customer c ON r.customer_id = c.customer_id
-- WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan'
-- AND r.return_date BETWEEN '2005-07-28' AND '2005-08-01'
-- AND r.amount > 4.00;


-- SELECT f.title
-- FROM rental r
-- JOIN inventory i ON r.inventory_id = i.inventory_id
-- JOIN film f ON i.film_id = f.film_id
-- JOIN customer c ON r.customer_id = c.customer_id
-- WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan'
-- AND (f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
-- ORDER BY f.replacement_cost DESC
-- LIMIT 1;

