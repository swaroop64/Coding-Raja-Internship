import os

def load_data(filename):
    data = {}
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                key, value = line.strip().split(',')
                data[key] = float(value)
    return data

def save_data(data, filename):
    with open(filename, 'w') as file:
        for key, value in data.items():
            file.write(f"{key},{value}\n")

def add_income(data):
    income = float(input("Enter income amount: "))
    category = input("Enter income category: ")
    data[category] = data.get(category, 0) + income

def add_expense(data):
    expense = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")
    data[category] = data.get(category, 0) - expense

def calculate_budget(data):
    total_income = sum([value for value in data.values() if value > 0])
    total_expense = sum([value for value in data.values() if value < 0])
    return total_income + total_expense

def analyze_expenses(data):
    print("Expense Analysis:")
    for category, amount in data.items():
        if amount < 0:
            print(f"{category}: {abs(amount)}")

def main():
    filename = "budget_data.txt"
    data = load_data(filename)

    while True:
        print("\n1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Budget")
        print("4. Analyze Expenses")
        print("5. Exit")
        
        choice = input("\nEnter your choice: ")

        if choice == '1':
            add_income(data)
        elif choice == '2':
            add_expense(data)
        elif choice == '3':
            budget = calculate_budget(data)
            print(f"\nTotal Budget: {budget}")
        elif choice == '4':
            analyze_expenses(data)
        elif choice == '5':
            save_data(data, filename)
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
