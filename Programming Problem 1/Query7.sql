-- SQLite
SELECT 
    ac.CLASS_NAME AS "Class Name",
    ac.CLASS_ID AS "Class ID",
    IFNULL(e.CLASS_DATE, 'No schedule available') AS "Class Schedule",
    IFNULL(i.LAST_NAME || ', ' || i.FIRST_NAME, 'No Instructor Assigned') AS "Instructor",
    IFNULL(GROUP_CONCAT(p.LAST_NAME || ', ' || p.FIRST_NAME, '\n'), 'No Participants Enrolled') AS "Participants"
FROM AdventureClass ac
LEFT JOIN Enrollment e ON ac.CLASS_ID = e.CLASS_ID
LEFT JOIN ClassAssignment ca ON ac.CLASS_ID = ca.CLASS_ID
LEFT JOIN Instructor i ON ca.INSTRUCTOR_ID = i.INSTRUCTOR_ID
LEFT JOIN Participant p ON e.PARTICIPANT_ID = p.PARTICIPANT_ID
WHERE ac.CLASS_ID = 13
GROUP BY ac.CLASS_ID;
