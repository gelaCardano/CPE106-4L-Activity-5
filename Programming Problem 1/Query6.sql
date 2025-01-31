-- SQLite
SELECT 'AdventureClass' AS Table_Name, CLASS_ID FROM AdventureClass
UNION ALL
SELECT 'ClassAssignment', CLASS_ID FROM ClassAssignment
UNION ALL
SELECT 'Enrollment', CLASS_ID FROM Enrollment;