from faker import Faker
import csv

# Create an instance of Faker
fake = Faker()

# Use a context manager to handle file operations
with open('data.csv', mode='w', newline='') as output:
    mywriter = csv.writer(output)
    
    # Write the header
    header = ['name', 'age', 'street', 'city', 'state', 'zip', 'lng', 'lat']
    mywriter.writerow(header)
    
    # Generate and write 1000 fake records
    for _ in range(1000):
        mywriter.writerow([
            fake.name(),
            fake.random_int(min=18, max=80, step=1),
            fake.street_address(),
            fake.city(),
            fake.state(),
            fake.zipcode(),
            float(fake.longitude()),
            float(fake.latitude())
        ])

# No need to explicitly close the file; it's handled by the context manager
print("CSV file created successfully.")
