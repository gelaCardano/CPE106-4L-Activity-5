-- SQLite
INSERT INTO Participant (LAST_NAME, FIRST_NAME, ADDRESS, CITY, STATE, POSTAL_CODE, TELEPHONE_NO, DATE_OF_BIRTH)
VALUES 
    ('Smith', 'John', '123 Main St', 'Anytown', 'CA', '12345', '555-1234', '1970-01-01'),
    ('Jones', 'Jane', '456 Elm St', 'Othertown', 'NY', '67890', '555-5678', '1975-02-02'),
    ('Doe', 'Joe', '789 Oak St', 'Thistown', 'TX', '13579', '555-2468', '1980-03-03');

INSERT INTO AdventureClass (CLASS_NAME, CLASS_DESCRIPTION, MAX_PAX, CLASS_FEE) 
VALUES 
    ('Hiking', 'Learn basic hiking skills and enjoy the great outdoors.', 10, 50.00),
    ('Rock Climbing', 'Learn basic rock climbing skills and enjoy the great outdoors.', 8, 75.00),
    ('Kayaking', 'Learn basic kayaking skills and enjoy the great outdoors.', 12, 60.00);

INSERT INTO Enrollment (PARTICIPANT_ID, CLASS_ID, CLASS_DATE) 
VALUES 
    (1, 1, '2020-01-01'),
    (2, 2, '2020-02-02'),
    (3, 3, '2020-03-03');

INSERT INTO Instructor (LAST_NAME, FIRST_NAME) 
VALUES 
    ('Brown', 'Emily'), 
    ('Wilson', 'Michael'), 
    ('Anderson', 'Laura');

INSERT INTO ClassAssignment (CLASS_ID, INSTRUCTOR_ID)
VALUES 
    (1, 1),
    (2, 2),
    (3, 3);