spams_keywords=["Act now","Limited time offer","Don't miss out","Last chance","Hurry","While supplies last","Expires","Final call",
"Flash sale"]

string=input("Enter a email: ")

for spam in spams_keywords:
    if spam in string:
        print("This is spam email")
        break
else:
    print("This is genuine email")


