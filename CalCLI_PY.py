def main():
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))

    while True:
        print("Choose method:")
        print("1: Add")
        print("2: Subtract")
        print("3: Multiply")
        print("4: Divide")
        print("5: Terminate")
        meth = int(input("Enter choice: "))

        if meth == 1:
            print(f"Answer (you selected: addition): = {num1 + num2}")
        elif meth == 2:
            print(f"Answer (you selected: subtraction): = {num1 - num2}")
        elif meth == 3:
            print(f"Answer (you selected: multiplication): = {num1 * num2}")
        elif meth == 4:
            if num2 != 0:
                print(f"Answer (you selected: division): = {num1 / num2}")
            else:
                print("Error: Division by zero")
        elif meth == 5:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

