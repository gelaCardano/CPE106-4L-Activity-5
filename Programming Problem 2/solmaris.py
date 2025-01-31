import sqlite3

# Connect to SQLite database (Creates it if it doesn't exist)
conn = sqlite3.connect("solmaris.db")
cursor = conn.cursor()

# Create Renters Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Renters (
    renter_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    middle_initial TEXT,
    last_name TEXT NOT NULL,
    address TEXT,
    city TEXT,
    state TEXT,
    postal_code TEXT,
    phone_number TEXT,
    email TEXT UNIQUE
);
""")

# Create Properties Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Properties (
    property_id INTEGER PRIMARY KEY AUTOINCREMENT,
    location_number INTEGER NOT NULL,
    location_name TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT,
    state TEXT,
    postal_code TEXT,
    unit_number TEXT NOT NULL,
    square_footage INTEGER,
    bedrooms INTEGER,
    bathrooms INTEGER,
    max_occupancy INTEGER NOT NULL,
    base_weekly_rate REAL NOT NULL
);
""")

# Create Rental Agreements Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Rental_Agreements (
    rental_id INTEGER PRIMARY KEY AUTOINCREMENT,
    renter_id INTEGER,
    property_id INTEGER,
    start_date TEXT NOT NULL,
    end_date TEXT NOT NULL,
    weekly_rental_amount REAL NOT NULL,
    FOREIGN KEY (renter_id) REFERENCES Renters(renter_id),
    FOREIGN KEY (property_id) REFERENCES Properties(property_id)
);
""")

# Commit and close
conn.commit()
conn.close()

print("✅ Solmaris database and tables created successfully!")
