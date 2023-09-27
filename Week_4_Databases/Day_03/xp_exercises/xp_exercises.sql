-- Get a list of all the languages, from the language table.

SELECT language_id, name FROM language;

-- Get a list of all films joined with their languages – select the following details : film title, description, and language name.

SELECT film.title, film.description, language.name 
FROM film
JOIN language
ON film.language_id = language.language_id;

-- Get all languages, even if there are no films in those languages – select the following details : film title, description, and language name.

SELECT film.title, film.description, language.name 
FROM film
RIGHT JOIN language
ON film.language_id = language.language_id;

-- Create a new table called new_film with the following columns : id, name.

CREATE TABLE new_film (
      new_film_id SERIAL PRIMARY KEY,
 	  new_film_name VARCHAR (50) NOT NULL
);

-- Add some new films to the table.

INSERT INTO new_film (new_film_name)
VALUES
('Barbie'), ('Oppenheimer'), ('Hannibal');

SELECT * FROM new_film;

-- Create a new table called customer_review, which will contain film reviews that customers will make.

CREATE TABLE customer_review (
    review_id SERIAL PRIMARY KEY,
    film_id INT REFERENCES new_film(new_film_id) ON DELETE CASCADE,
    language_id INT REFERENCES language(language_id),
    title VARCHAR(255),
    score INT CHECK (score >= 1 AND score <= 10),
    review_text TEXT,
    last_update TIMESTAMP
);

SELECT * FROM customer_review;

-- Add 2 movie reviews. Make sure you link them to valid objects in the other tables.

INSERT INTO customer_review (film_id, language_id, title, score, review_text, last_update)
VALUES
(1, 1, 'Barbie', 7, 'A cool movie about feminism, I really enjoyed it. It had a great storyline.', NOW()),
(2, 1, 'Oppenheimer', 9, 'Amazing movie, I am impressed by the acting and the plot! It kept me on the edge of my seat the entire time.', NOW())
;

-- Delete a film that has a review from the new_film table, what happens to the customer_review table?

DELETE FROM new_film
WHERE new_film_id = 1;

-- Use UPDATE to change the language of some films. Make sure that you use valid languages.

UPDATE film
SET language_id = 6
WHERE film_id = 2;

SELECT film.film_id, film.title, film.description, language.name, language.language_id 
FROM film
JOIN language
ON film.language_id = language.language_id
WHERE film.film_id = 2;

-- Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?
-- customer_address_id - is the foreign key, we must provide the corresponding address id when inserting

-- We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?
DROP TABLE customer_review;
-- That was easy, no extra checking.

-- Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
SELECT COUNT(*) FROM rental
WHERE return_date is Null;

-- Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
SELECT film.film_id, film.title, film.replacement_cost, rental.return_date
FROM film
JOIN inventory
ON film.film_id = inventory.film_id
JOIN rental
ON inventory.inventory_id = rental.inventory_id
WHERE return_date is Null
ORDER BY film.replacement_cost DESC
LIMIT 30;

-- Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he wants to rent?
-- The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.

SELECT film.title, film.description, actor.first_name, actor.last_name FROM film
JOIN film_actor
ON film.film_id = film_actor.film_id
JOIN actor
ON film_actor.actor_id = actor.actor_id
WHERE film.description LIKE '%Sumo%' AND actor.first_name = 'Penelope' AND actor.last_name = 'Monroe';

-- The 2nd film : A short documentary (less than 1 hour long), rated “R”.

SELECT film.title, film.length, film.rating, category.name FROM film
JOIN film_category
ON film.film_id = film_category.film_id
JOIN category
ON film_category.category_id = category.category_id
WHERE category.name = 'Documentary' AND film.rating = 'R' AND film.length < 60;

-- The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.

SELECT film.title, film.rental_rate, film.rating, rental.return_date, customer.first_name, customer.last_name FROM film
JOIN inventory
ON film.film_id = inventory.film_id
JOIN rental
ON inventory.inventory_id = rental.inventory_id
JOIN customer
ON rental.customer_id = customer.customer_id
WHERE customer.first_name = 'Matthew' 
AND customer.last_name = 'Mahan' 
AND film.rental_rate > 4
AND rental.return_date BETWEEN '2005-07-28' AND '2005-08-01';

-- The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.

SELECT film.title, film.description, film.replacement_cost, customer.first_name, customer.last_name FROM film
JOIN inventory
ON film.film_id = inventory.film_id
JOIN rental
ON inventory.inventory_id = rental.inventory_id
JOIN customer
ON rental.customer_id = customer.customer_id
WHERE customer.first_name = 'Matthew' 
AND customer.last_name = 'Mahan' 
AND (film.title LIKE '%oat%' OR film.description LIKE '%oat%')
ORDER BY film.replacement_cost DESC
;