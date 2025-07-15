import pandas as pd
from faker import Faker

# Create object
fake=Faker()

# Generate data
fake.name()
fake.text()
fake.address()
fake.email()
fake.date()
fake.country()
fake.phone_number()
fake.random_number(digits=5)

fakedataframe=pd.DataFrame({
    'Date':[fake.date() for i in range(5)],
    'Name':[fake.name() for i in range(5)],
    'Email':[fake.email() for i in range(5)],
    'Text':[fake.text() for i in range(5)],
})

file_path = 'output.txt'
fakedataframe.to_csv(file_path, sep='\t', index=False, header=True)

