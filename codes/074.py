from csv import reader,DictReader

with open("demo.csv","r") as f:
    csv_reader=reader(f)
    #iterator  --> iterable
    print(type(csv_reader))
    print(csv_reader)
    heading=next(csv_reader)
    print(heading)
    print("----------------------------------------------------------------------")
    for row in csv_reader:
        print(row)


with open('demo.csv', 'r') as f: 
    csv_reader = DictReader(f) 
    # if file is psv(| seperated file) csv_reader = DictReader(f,delimiter="|")
    for row in csv_reader:
        print(row)