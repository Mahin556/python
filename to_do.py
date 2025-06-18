to_do_list=[]

while True:
    task=input("Enter a task(or 'done' to stop): ")
    if task.strip().lower() == 'done':
        break
    to_do_list.append(task)

print("Your TO-DO")
for i, task in enumerate(to_do_list):
    print(f"{i+1}. {task}")



