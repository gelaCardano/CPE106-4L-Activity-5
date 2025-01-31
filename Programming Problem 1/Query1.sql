-- SQLite
CREATE TABLE Participant (
    PARTICIPANT_ID INTEGER PRIMARY KEY AUTOINCREMENT, 
    LAST_NAME TEXT NOT NULL, 
    FIRST_NAME TEXT NOT NULL, 
    ADDRESS TEXT, 
    CITY TEXT, 
    STATE TEXT, 
    POSTAL_CODE TEXT, 
    TELEPHONE_NO TEXT, 
    DATE_OF_BIRTH DATE 
); 

CREATE TABLE AdventureClass (
    CLASS_ID INTEGER PRIMARY KEY AUTOINCREMENT, 
    CLASS_NAME TEXT NOT NULL, 
    CLASS_DESCRIPTION TEXT NOT NULL, 
    MAX_PAX INTEGER NOT NULL, 
    CLASS_FEE INTEGER NOT NULL
); 

CREATE TABLE Enrollment (
    ENROLLMENT_ID INTEGER PRIMARY KEY AUTOINCREMENT, 
    PARTICIPANT_ID INTEGER NOT NULL, 
    CLASS_ID INTEGER NOT NULL, 
    CLASS_DATE DATE NOT NULL, 
    FOREIGN KEY (PARTICIPANT_ID) REFERENCES Participant(PARTICIPANT_ID),
    FOREIGN KEY (CLASS_ID) REFERENCES AdventureClass(CLASS_ID)
); 

CREATE TABLE Instructor (
    INSTRUCTOR_ID INTEGER PRIMARY KEY AUTOINCREMENT, 
    LAST_NAME TEXT NOT NULL,
    FIRST_NAME TEXT NOT NULL
); 

CREATE TABLE ClassAssignment (
    CLASS_ASSIGNMENT_ID INTEGER PRIMARY KEY AUTOINCREMENT, 
    INSTRUCTOR_ID INTEGER NOT NULL, 
    CLASS_ID INTEGER NOT NULL, 
    FOREIGN KEY (INSTRUCTOR_ID) REFERENCES Instructor(INSTRUCTOR_ID),
    FOREIGN KEY (CLASS_ID) REFERENCES AdventureClass(CLASS_ID)
); 