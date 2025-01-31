-- SQLite
INSERT INTO Participant (LAST_NAME, FIRST_NAME, ADDRESS, CITY, STATE, POSTAL_CODE, TELEPHONE_NO, DATE_OF_BIRTH)
VALUES 
    ('Taylor', 'Alice', '101 Pine St', 'Newville', 'FL', '24680', '555-1357', '1985-04-04'),
    ('White', 'Chris', '202 Maple St', 'Oldtown', 'WA', '98765', '555-9753', '1990-05-05'),
    ('Harris', 'Olivia', '303 Cedar St', 'Nexttown', 'IL', '56789', '555-8642', '1992-06-06'),
    ('Martin', 'David', '404 Birch St', 'Somewhere', 'CO', '54321', '555-7531', '1995-07-07'),
    ('Clark', 'Sophia', '505 Aspen St', 'Elsewhere', 'AZ', '12321', '555-1593', '1998-08-08');

INSERT INTO AdventureClass (CLASS_NAME, CLASS_DESCRIPTION, MAX_PAX, CLASS_FEE) 
VALUES 
    ('Mountain Biking', 'Learn the basics of mountain biking and tackle rough terrains.', 8, 80.00),
    ('Cave Exploration', 'Discover underground caves and learn cave navigation techniques.', 6, 90.00),
    ('Snorkeling', 'Explore marine life and learn snorkeling safety tips.', 15, 70.00),
    ('Survival Skills', 'Learn essential survival skills in the wilderness.', 10, 100.00),
    ('Trail Running', 'Improve your endurance and technique in off-road running.', 12, 65.00);

INSERT INTO Enrollment (PARTICIPANT_ID, CLASS_ID, CLASS_DATE) 
VALUES 
    (4, 4, '2020-04-04'),
    (5, 5, '2020-05-05'),
    (6, 6, '2020-06-06'),
    (1, 7, '2020-07-07'),
    (2, 8, '2020-08-08'),
    (3, 9, '2020-09-09'),
    (7, 10, '2020-10-10'),
    (8, 1, '2020-11-11'),
    (9, 2, '2020-12-12');

INSERT INTO Instructor (LAST_NAME, FIRST_NAME) 
VALUES 
    ('Robinson', 'Daniel'), 
    ('Lee', 'Jessica'), 
    ('Walker', 'Brian'), 
    ('Hall', 'Samantha'),
    ('Young', 'Andrew');

INSERT INTO ClassAssignment (CLASS_ID, INSTRUCTOR_ID)
VALUES 
    (4, 4),
    (5, 5),
    (6, 1),
    (7, 2),
    (8, 3),
    (9, 4),
    (10, 5);