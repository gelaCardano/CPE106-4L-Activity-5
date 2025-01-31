import sqlite3

# Connect to the SQLite database
try:
    conn = sqlite3.connect("mydatabase.db")  # Change if your DB name is different
    cursor = conn.cursor()
except sqlite3.Error as e:
    print("❌ Database connection error:", e)
    exit()

# List available classes before asking for input
print("\nAvailable Classes:")
cursor.execute("SELECT CLASS_ID, CLASS_NAME FROM AdventureClass;")
available_classes = cursor.fetchall()
if available_classes:
    for c in available_classes:
        print(f" - CLASS_ID: {c[0]}, Name: {c[1]}")
else:
    print("❌ No classes found in the database.")

# Prompt user for Class ID
class_id = input("\nEnter the Class ID you want to view details for: ").strip()

# Debugging: Print user input
print(f"\n🔍 Searching for Class ID: {class_id}")

# SQL Query to fetch class details (with LEFT JOIN to ensure all classes are included)
query = """
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
WHERE ac.CLASS_ID = ?
GROUP BY ac.CLASS_ID;
"""

try:
    # Execute the query with the user-provided class_id
    cursor.execute(query, (class_id,))
    result = cursor.fetchone()

    # Display output in a formatted manner
    if result:
        print("\n" + "="*50)
        print(" " * 15 + "Class Details")
        print("="*50)
        print(f"Name of the class: {result[0]:<40} Class ID: {result[1]}")
        print(f"Schedule of the class: {result[2]}")
        print(f"Instructor of the class: {result[3]}")
        print("\nParticipants:\n" + "-"*50)
        print(result[4] if result[4] else "No participants enrolled yet.")
        print("="*50)
    else:
        print(f"❌ No class found with Class ID: {class_id}")

except sqlite3.Error as e:
    print("❌ Error executing query:", e)

# Close the database connection
finally:
    conn.close()
