
while True:
    user_entry = input("Enter a number: ")
    try:
        user_entry = int(user_entry)
        break
    except:
        print("User entry must be a number.")


if user_entry < 50:
    user_entry +=50
    print(f"Answer: {user_entry}, and it was under 50")

else: 
    user_entry -= 50
    print(f"Answer: {user_entry}, and it was above 50")