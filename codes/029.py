nums=[]
for num in range(1,5):
    nums.append(int(input(f"Enter number{num}: ")))

print(nums)

if (nums[0]>nums[1]) and (nums[0]>nums[2]) and (nums[0]>nums[3]):
    print(f"{nums[0]} is greater of all numbers")
elif (nums[1]>nums[2]) and (nums[1]>nums[3]):
    print(f"{nums[1]} is greater of all numbers")
elif (nums[2]>nums[3]):
    print(f"{nums[2]} is greater of all numbers")
else:
    print(f"{nums[3]} is greater of all numbers")


a = 33
b = 200
if b > a:
  pass



# check empty or not # important
name = "abc"
if name: # true if string is not empty
    print("string is n")
else:
    print("")

    