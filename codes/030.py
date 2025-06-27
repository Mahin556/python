marks=[]
for num in range(1,4):
    marks.append(int(input(f"Enter marks of subject{num}: ")))

total_marks=sum(marks)/3

if (total_marks >= 40 and marks[0]>=33 and marks[1]>=33 and marks[2]>=33):
    print("PASS")
else:
    print("FAIL")