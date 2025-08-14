def calculate_discount(cost):
    if cost > 100:
        return cost * 0.8
    elif cost >= 50:
        return cost * 0.9

    else:
        return cost
cost=float(input("Enter the cost:"))
print(calculate_discount(cost))



def kilometers_to_miles(kilometers):
    return kilometers*0.621371  
kilometers=float(input("Enter kilometers:")) 
miles=kilometers_to_miles(kilometers)
print(f"{kilometers} km ={miles:.2f} miles")



def temp_c_to_temp_f(f):
    temp_c=float(input("Enter Celcious:"))
    temp_f=(temp_c*9/5)+32

print(f"{temp_c} C ={temp_f:.2f} F")

def main(choice):
    print("Menu")
    print("Press '1' for calculate_discount")
    print("Press '2' for kilometers_to miles")
    print("Press '3' for temp_c to temp_f")
    choice=input("Enter your choice")
    if choice=="1":
        calculate_discount(cost)
    elif choice=="2":
        kilometers_to_miles(kilometers)
    elif choice=="3":
        temp_c_to_temp_f(f)
    else:
         print("Invalid choice")