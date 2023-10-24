DROP TABLE students;

CREATE TABLE students(
 student_id SERIAL PRIMARY KEY,
 student_lname VARCHAR (50) NOT NULL,
 student_fname VARCHAR (50) NOT NULL,
 student_bdate DATE
);

INSERT INTO students (student_fname, student_lname, student_bdate)
VALUES
('Marc', 'Benichou', '1998-11-02'), 
('Yoan', 'Cohen', '2010-12-03'), 
('Lea', 'Benichou', '1987-07-27'), 
('Amelia', 'Dux', '1996-04-07'), 
('David', 'Grez', '2003-06-14'), 
('Omer', 'Simpson', '1980-10-03'), 
('Nathaniel', 'Hully', '1979-11-13');

-- Fetch all of the data from the table.
SELECT * FROM students;

-- Fetch the student which id is equal to 2.
SELECT student_fname, student_lname FROM students
WHERE student_id = 2;

-- Fetch the student whose last_name is Benichou AND first_name is Marc.
SELECT student_fname, student_lname FROM students
WHERE student_lname = 'Benichou' AND student_fname = 'Marc';

-- Fetch the students whose last_names are Benichou OR first_names are Marc.
SELECT student_fname, student_lname FROM students
WHERE student_lname = 'Benichou' OR student_fname = 'Marc';

-- Fetch the students whose first_names contain the letter a.
SELECT student_fname, student_lname FROM students
WHERE student_fname LIKE '%a%';

-- Fetch the students whose first_names start with the letter a.
SELECT student_fname, student_lname FROM students
WHERE student_fname LIKE 'A%';

-- Fetch the students whose first_names end with the letter a.
SELECT student_fname, student_lname FROM students
WHERE student_fname LIKE '%a';

-- Fetch the students whose second to last letter of their first_names are a (Example: Leah).
SELECT student_fname, student_lname FROM students
WHERE SUBSTRING(student_fname, LENGTH(student_fname)-1, 1) = 'a';

-- Fetch the students whose id’s are equal to 1 AND 3 .
SELECT student_fname, student_lname FROM students
WHERE student_id = 1 AND student_id = 3;

-- Fetch the students whose birth_dates are equal to or come after 1/01/2000. (show all their info).
SELECT * FROM students WHERE student_bdate >= '2000-01-01';