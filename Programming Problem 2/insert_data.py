import sqlite3

# Connect to the database
def get_db_connection():
    try:
        conn = sqlite3.connect("solmaris.db")
        cursor = conn.cursor()
        return conn, cursor
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None, None

# Function to validate numeric input
def get_numeric_input(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        print("Invalid input. Please enter a numeric value.")

# Function to validate float input (e.g., for price)
def get_float_input(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to insert a new renter
def insert_renter():
    conn, cursor = get_db_connection()
    if not conn:
        return
    
    print("\nAdd a New Renter")
    first_name = input("First Name: ").strip()
    middle_initial = input("Middle Initial (leave blank if none): ").strip()
    last_name = input("Last Name: ").strip()
    address = input("Address: ").strip()
    city = input("City: ").strip()
    state = input("State (2-letter code): ").strip().upper()
    postal_code = input("Postal Code: ").strip()
    phone_number = input("Phone Number: ").strip()
    email = input("Email: ").strip()

    try:
        cursor.execute("""
            INSERT INTO Renters (first_name, middle_initial, last_name, address, city, state, postal_code, phone_number, email)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (first_name, middle_initial, last_name, address, city, state, postal_code, phone_number, email))

        conn.commit()
        print("Renter added successfully.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    
    conn.close()

# Function to insert a new property
def insert_property():
    conn, cursor = get_db_connection()
    if not conn:
        return

    print("\nAdd a New Property")
    location_number = get_numeric_input("Location Number: ")
    location_name = input("Location Name: ").strip()
    address = input("Address: ").strip()
    city = input("City: ").strip()
    state = input("State (2-letter code): ").strip().upper()
    postal_code = input("Postal Code: ").strip()
    unit_number = input("Unit Number: ").strip()
    square_footage = get_numeric_input("Square Footage: ")
    bedrooms = get_numeric_input("Number of Bedrooms: ")
    bathrooms = get_numeric_input("Number of Bathrooms: ")
    max_occupancy = get_numeric_input("Max Occupancy: ")
    base_weekly_rate = get_float_input("Base Weekly Rate: ")

    try:
        cursor.execute("""
            INSERT INTO Properties (location_number, location_name, address, city, state, postal_code, unit_number, square_footage, bedrooms, bathrooms, max_occupancy, base_weekly_rate)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (location_number, location_name, address, city, state, postal_code, unit_number, square_footage, bedrooms, bathrooms, max_occupancy, base_weekly_rate))

        conn.commit()
        print("Property added successfully.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")

    conn.close()

# Function to insert a new rental agreement
def insert_rental_agreement():
    conn, cursor = get_db_connection()
    if not conn:
        return

    print("\nAdd a New Rental Agreement")

    # Show available renters
    cursor.execute("SELECT renter_id, first_name, last_name FROM Renters")
    renters = cursor.fetchall()
    if not renters:
        print("No renters found. Add a renter first.")
        return
    for r in renters:
        print(f"{r[0]} - {r[1]} {r[2]}")

    renter_id = get_numeric_input("Enter Renter ID: ")

    # Show available properties
    cursor.execute("SELECT property_id, location_name FROM Properties")
    properties = cursor.fetchall()
    if not properties:
        print("No properties found. Add a property first.")
        return
    for p in properties:
        print(f"{p[0]} - {p[1]}")

    property_id = get_numeric_input("Enter Property ID: ")
    start_date = input("Start Date (YYYY-MM-DD): ").strip()
    end_date = input("End Date (YYYY-MM-DD): ").strip()
    weekly_rental_amount = get_float_input("Weekly Rental Amount: ")

    try:
        cursor.execute("""
            INSERT INTO Rental_Agreements (renter_id, property_id, start_date, end_date, weekly_rental_amount)
            VALUES (?, ?, ?, ?, ?)
        """, (renter_id, property_id, start_date, end_date, weekly_rental_amount))

        conn.commit()
        print("Rental agreement added successfully.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")

    conn.close()

# Function to delete a renter
def delete_renter():
    conn, cursor = get_db_connection()
    if not conn:
        return

    cursor.execute("SELECT renter_id, first_name, last_name FROM Renters")
    renters = cursor.fetchall()
    if not renters:
        print("No renters found.")
        return
    for r in renters:
        print(f"{r[0]} - {r[1]} {r[2]}")

    renter_id = get_numeric_input("Enter Renter ID to delete: ")
    cursor.execute("DELETE FROM Renters WHERE renter_id = ?", (renter_id,))
    conn.commit()
    print("Renter deleted successfully.")

    conn.close()

# Function to delete a property
def delete_property():
    conn, cursor = get_db_connection()
    if not conn:
        return

    cursor.execute("SELECT property_id, location_name FROM Properties")
    properties = cursor.fetchall()
    if not properties:
        print("No properties found.")
        return
    for p in properties:
        print(f"{p[0]} - {p[1]}")

    property_id = get_numeric_input("Enter Property ID to delete: ")
    cursor.execute("DELETE FROM Properties WHERE property_id = ?", (property_id,))
    conn.commit()
    print("Property deleted successfully.")

    conn.close()

# Function to delete a rental agreement
def delete_rental_agreement():
    conn, cursor = get_db_connection()
    if not conn:
        return

    cursor.execute("SELECT rental_id FROM Rental_Agreements")
    rentals = cursor.fetchall()
    if not rentals:
        print("No rental agreements found.")
        return
    for ra in rentals:
        print(f"Rental Agreement ID: {ra[0]}")

    rental_id = get_numeric_input("Enter Rental Agreement ID to delete: ")
    cursor.execute("DELETE FROM Rental_Agreements WHERE rental_id = ?", (rental_id,))
    conn.commit()
    print("Rental agreement deleted successfully.")

    conn.close()

# Menu for user input
while True:
    print("\nChoose an option:")
    print("1. Add a Renter")
    print("2. Add a Property")
    print("3. Add a Rental Agreement")
    print("4. Delete a Renter")
    print("5. Delete a Property")
    print("6. Delete a Rental Agreement")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        insert_renter()
    elif choice == "2":
        insert_property()
    elif choice == "3":
        insert_rental_agreement()
    elif choice == "4":
        delete_renter()
    elif choice == "5":
        delete_property()
    elif choice == "6":
        delete_rental_agreement()
    elif choice == "7":
        print("Exiting. Data saved.")
        break
    else:
        print("Invalid choice. Please try again.")
