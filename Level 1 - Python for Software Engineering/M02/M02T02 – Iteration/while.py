total_sum = 0
count = 0

while True:
    try:
        number = float(input("Enter a number (-1 to stop, 0 is invalid): "))
        
        if number == -1:
            break
        
        if number == 0:
            print("0 is not a valid input. Please try again.")
            continue
            
        total_sum += number
        count += 1

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if count > 0:
    average = total_sum / count
    print(f"Average of entered numbers: {average:.2f}")
else:
    print("No valid numbers were entered.")