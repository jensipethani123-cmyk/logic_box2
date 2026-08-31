print("Welcome To the Pattern Generator and Number Analyzer!")

while True:
    print("\nSelected The Number")
    print("1. Generate a patten")
    print("2. Number Analyzer")
    print("3. Exit")

    choice = int(input("Enter The Choice of number 1 to 3:::: "))

    if choice == 1:
        print("\n--- Pattern Create ---")
        rows = int(input("Enter the Number To create A pattern:-> "))
        
        if rows <= 0:
            print("Please Enter A Number Greater Than 0 (1 to 100)")
        else:
            print("--- Generated Pattern ---")
            for i in range(1, rows + 1):
                for j in range(i):
                    print("*", end="")
                print()
                
    elif choice == 2:
        print("\n--- Number Analyzer ---")
        start_num = int(input("Enter The Start Number To Start: "))
        End_num = int(input("Enter The End Number To Stop: "))

        total_sum = 0
        for i in range(start_num, End_num + 1):
            if i % 2 == 0:
                print(f"Number {i} is Even")
            else:
                print(f"Number {i} is Odd")
            total_sum += i

        print(f"Sum of all numbers from {start_num} to {End_num} is: {total_sum}")
        
    elif choice == 3:
        print("Good Byee")
        break
        
    else:
        print("please eneter the number of 1 to 3:")