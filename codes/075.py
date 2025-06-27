from csv import writer,DictWriter

# methods ---> writerow writerows
with open("demo1.csv","w",newline="") as f:
    csv_writer=writer(f)
    csv_writer.writerow(["Name","Country"])
    csv_writer.writerow(["Mahin","Chine"])
    csv_writer.writerow(["Raza","Singapore"])

with open("demo1.csv","w",newline="") as f:
    csv_writer=writer(f)
    csv_writer.writerows([["Name","Country"],["Mahin","Chine"],["Rohan","Singapore"]])

with open('final.csv', 'w', newline='') as f:
    csv_writer = DictWriter(f, fieldnames=['firstname', 'lastname', 'age'])
    csv_writer.writeheader()

    csv_writer.writerow({
        'firstname': 'harshit',
        'lastname': 'vashistha',
        'age': 500
    })

    csv_writer.writerow({
        'firstname': 'mohit',
        'lastname': 'vashistha',
        'age': 500
    })

    #Other method
    csv_writer.writerows([
    {'firstname': 'harshit', 'lastname': 'vashistha', 'age': 500},
    {'firstname': 'harshit', 'lastname': 'vashistha', 'age': 500},
    {'firstname': 'harshit', 'lastname': 'vashistha', 'age': 500}
    ])
