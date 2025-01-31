import sqlite3

# Connect to database
conn = sqlite3.connect("solmaris.db")
cursor = conn.cursor()

# Ask for confirmation
confirm = input("Are you sure you want to delete all data? (yes/no): ")
if confirm.lower() == "yes":
    # Delete all records from each table
    cursor.execute("DELETE FROM Rental_Agreements")
    cursor.execute("DELETE FROM Renters")
    cursor.execute("DELETE FROM Properties")
    conn.commit()

    print("All data has been deleted successfully!")

else:
    print("Operation canceled.")

# Close connection
conn.close()
