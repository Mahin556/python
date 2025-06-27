# reader DictReader
# writer DictWriter
from csv import DictReader, DictWriter

with open('demo.csv','r') as rf:
  with open('demo2.csv', 'w') as wf: 
    csv_reader = DictReader(rf)
    csv_writer = DictWriter(wf,fieldnames=['first_name', 'last_name','age'])
    csv_writer.writeheader()
    for row in csv_reader:
      fname, Lname, age = row['firstname'], row['lastname'], row['age'] 
      csv_writer.writerow({'first_name':fname.upper(), 'last_name':Lname.upper(),'age': age})