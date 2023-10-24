SELECT * FROM actors;

--  Count how many actors are in the table.
SELECT COUNT(*) FROM actors;

-- Try to add a new actor with some blank fields.

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES
('Daniel','Radcliff', Null, 2),
('Emma','Watson','06/05/1989', Null);