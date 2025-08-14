username= ["fabiola","michel","theopist","eric","dan","isaac"]
userlnput= input("Enter your Name to loin:")
password= 
valid=""
for i in username:
    if userlnput in username:
        valid+=f"Welcome..!{userlnput}"
        break
    else:
        valid+=f"{userlnput} Not recognised!"
        break
print(valid)