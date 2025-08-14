def kilometers_Converter():
    kilometers=float(input("Enter kilometers:"))
    miles=kilometers*0.621371
    print(f"{kilometers} km ={miles:.2f} miles")

def temperature_Converter():
    temp_c=float(input("Enter Celcious:"))
    temp_f=(temp_c*9/5)+32

    print(f"{temp_c} C ={temp_f:.2f} F")



def calculate_discount():
    cost=float(input("Enter the cost:"))
    if cost > 100:
        final=cost * 0.8
    elif cost >= 50:
        final=cost * 0.9

    else:
        final=cost

    print(f"Discount cost: MK{final:.2f}")


def main():
    print("Welcome to smart tools!")
    print("1. Kilometers to Miles converter")
    print("2. Temperature converter (C to F)")
    print("3. Shop Discount Calculator")

    choice = input("choose an option (1-3):")
    if choice == "1":
        kilometers_Converter()
    elif choice == "2":
        temperature_Converter()
    elif choice == "3":
        calculate_discount()
    else:
        print("Invalid choice. Try again.") 
main()