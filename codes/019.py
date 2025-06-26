name, char = input("enter comma separated name and character: ").split(",") 
print("length of your name is {len(name)}")
print (f"character count: {name.strip().lower().count(char.strip().lower())}") # case sensitive # Harshit
# harshit
# 5
# #H- h
# 5
# # "Harshit
# 7
# 3
# 9
#
# > "Harshit"
# H" ------->"H" -----------> "h" -> "harshit"

name.strip().lower().count(char.strip().lower())
char.strip().lower()