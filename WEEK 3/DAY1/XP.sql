-- CREATE TABLE STUDENTS (
-- ID SERIAL PRIMARY KEY, 
-- LAST_NAME VARCHAR(20),
-- FIRST_NAME VARCHAR(20),
-- BIRTH_DATE DATE);
-- INSERT INTO STUDENTS (LAST_NAME, FIRST_NAME, BIRTH_DATE) VALUES 
-- ('Benichou', 'Marc', '1998-11-02'),
-- ('Cohen', 'Yoan', '2010-12-03'),
-- ('Benichou', 'Lea', '1987-07-27'),
-- ('Dux', 'Amelia', '1996-04-07'),
-- ('Grez', 'David', '2003-06-14'),
-- ('Simpson', 'Omer', '1980-10-03'),
-- ('Levinak', 'Vasili', '2000-04-21');
--1
-- SELECT * 
-- FROM STUDENTS
-- WHERE ID = 2
--2
-- SELECT *
-- FROM STUDENTS 
-- WHERE LAST_NAME = 'Benichou' and FIRST_NAME='Marc'
--3
-- SELECT *
-- FROM STUDENTS 
-- WHERE LAST_NAME = 'Benichou' or FIRST_NAME='Marc'
-- 4
-- SELECT * 
-- FROM STUDENTS
-- WHERE FIRST_NAME LIKE '%a%'
--5
-- SELECT * 
-- FROM STUDENTS
-- WHERE FIRST_NAME LIKE 'A%'
--6
-- SELECT * 
-- FROM STUDENTS
-- WHERE FIRST_NAME LIKE '%a'
--7
-- SELECT * 
--  FROM STUDENTS
--  WHERE FIRST_NAME LIKE '%a_'
--8 
-- SELECT *
-- FROM STUDENTS
-- WHERE ID=1 OR ID= 3
SELECT *
FROM STUDENTS
WHERE BIRTH_DATE ='01-01-2000' OR BIRTH_DATE >'01-01-2000'

 