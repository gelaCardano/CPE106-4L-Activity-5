import sqlite3

# Connect to database
conn = sqlite3.connect("solmaris.db")
cursor = conn.cursor()

# Retrieve all renters
cursor.execute("SELECT * FROM Renters")
renters = cursor.fetchall()

print("\nRenters List:")
for renter in renters:
    print(renter)

# Retrieve all properties
cursor.execute("SELECT * FROM Properties")
properties = cursor.fetchall()

print("\nProperties List:")
for property in properties:
    print(property)

# Retrieve rental agreements with renter & property details
cursor.execute("""
    SELECT 
        ra.rental_id,
        r.renter_id,
        r.first_name || ' ' || r.middle_initial || ' ' || r.last_name AS renter_name,
        r.address, r.city, r.state, r.postal_code, r.phone_number, r.email,
        p.location_number, p.location_name, p.unit_number,
        ra.start_date, ra.end_date,
        ra.weekly_rental_amount
    FROM Rental_Agreements ra
    JOIN Renters r ON ra.renter_id = r.renter_id
    JOIN Properties p ON ra.property_id = p.property_id;
""")
rental_agreements = cursor.fetchall()

print("\nRental Agreements:")
for rental in rental_agreements:
    print(rental)

# Close connection
conn.close()
