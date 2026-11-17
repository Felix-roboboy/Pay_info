# ==========================================
# ROBO MONEY MANAGER
# ==========================================

money = 0.0
monthly_income = 0.0
yearly_income = 0.0
monthly_costs = 0.0
yearly_costs = 0.0


# ==========================================
# INPUT FUNCTION
# ==========================================

def get_amount():

    while True:

        try:
            amount = float(input("Enter amount (€): ").replace(",", "."))

            if amount < 0:
                print("Please enter a positive amount.")
                continue

            return amount

        except ValueError:
            print("Invalid number. Please try again.")


# ==========================================
# CALCULATE FINANCES
# ==========================================

def calculate_finances():

    # Monthly income including yearly income
    total_monthly_income = monthly_income + (yearly_income / 12)

    # Yearly income including monthly income
    total_yearly_income = (monthly_income * 12) + yearly_income

    # Monthly costs including yearly costs
    total_monthly_costs = monthly_costs + (yearly_costs / 12)

    # Yearly costs including monthly costs
    total_yearly_costs = (monthly_costs * 12) + yearly_costs

    # Income after costs
    monthly_profit = total_monthly_income - total_monthly_costs

    yearly_profit = total_yearly_income - total_yearly_costs

    return (
        total_monthly_income,
        total_yearly_income,
        total_monthly_costs,
        total_yearly_costs,
        monthly_profit,
        yearly_profit
    )


# ==========================================
# 1. SHOW INCOME
# ==========================================

def show_income():

    (
        total_monthly_income,
        total_yearly_income,
        total_monthly_costs,
        total_yearly_costs,
        monthly_profit,
        yearly_profit
    ) = calculate_finances()

    print("\n========== SHOW INCOME ==========")

    print("\n----- INCOME -----")

    print(f"Monthly Income: {monthly_income:.2f} €")
    print(f"Yearly Income: {yearly_income:.2f} €")

    print("\n----- COSTS -----")

    print(f"Monthly Costs: {monthly_costs:.2f} €")
    print(f"Yearly Costs: {yearly_costs:.2f} €")

    print("\n----- TOTAL INCOME -----")

    print(f"Total Monthly Income: {total_monthly_income:.2f} €")
    print(f"Total Yearly Income: {total_yearly_income:.2f} €")

    print("\n----- TOTAL COSTS -----")

    print(f"Total Monthly Costs: {total_monthly_costs:.2f} €")
    print(f"Total Yearly Costs: {total_yearly_costs:.2f} €")

    print("\n----- INCOME AFTER COSTS -----")

    print(f"Monthly Income After Costs: {monthly_profit:.2f} €")
    print(f"Yearly Income After Costs: {yearly_profit:.2f} €")

    print("\n----- MONEY -----")

    print(f"Current Money: {money:.2f} €")
    print(f"Money + Yearly Profit: {money + yearly_profit:.2f} €")

    print("=================================")


# ==========================================
# 2. ADD MONEY
# ==========================================

def add_money():

    global money

    amount = get_amount()

    money += amount

    print("\n========== ADD MONEY ==========")

    print(f"Added Money: {amount:.2f} €")
    print(f"Current Money: {money:.2f} €")

    print("================================")


# ==========================================
# 3. ADD MONTHLY INCOME
# ==========================================

def add_monthly_income():

    global monthly_income

    amount = get_amount()

    monthly_income += amount

    print("\n======= MONTHLY INCOME =======")

    print(f"Added Monthly Income: {amount:.2f} €")
    print(f"Total Monthly Income: {monthly_income:.2f} €")

    print("==============================")


# ==========================================
# 4. ADD YEARLY INCOME
# ==========================================

def add_yearly_income():

    global yearly_income

    amount = get_amount()

    yearly_income += amount

    print("\n======= YEARLY INCOME =======")

    print(f"Added Yearly Income: {amount:.2f} €")
    print(f"Total Yearly Income: {yearly_income:.2f} €")

    print("=============================")


# ==========================================
# 5. ADD MONTHLY COSTS
# ==========================================

def add_monthly_costs():

    global monthly_costs

    amount = get_amount()

    monthly_costs += amount

    print("\n======= MONTHLY COSTS =======")

    print(f"Added Monthly Costs: {amount:.2f} €")
    print(f"Total Monthly Costs: {monthly_costs:.2f} €")

    print("=============================")


# ==========================================
# 6. ADD YEARLY COSTS
# ==========================================

def add_yearly_costs():

    global yearly_costs

    amount = get_amount()

    yearly_costs += amount

    print("\n======= YEARLY COSTS =======")

    print(f"Added Yearly Costs: {amount:.2f} €")
    print(f"Total Yearly Costs: {yearly_costs:.2f} €")

    print("============================")


# ==========================================
# 7. SHOW ALL COSTS
# ==========================================

def show_all_costs():

    (
        total_monthly_income,
        total_yearly_income,
        total_monthly_costs,
        total_yearly_costs,
        monthly_profit,
        yearly_profit
    ) = calculate_finances()

    print("\n========== ALL COSTS ==========")

    print(f"Monthly Costs: {monthly_costs:.2f} €")
    print(f"Yearly Costs: {yearly_costs:.2f} €")

    print("--------------------------------")

    print(f"Total Monthly Costs: {total_monthly_costs:.2f} €")
    print(f"Total Yearly Costs: {total_yearly_costs:.2f} €")

    print("================================")


# ==========================================
# 8. SHOW SAVED MONEY
# ==========================================

def show_saved_money():

    (
        total_monthly_income,
        total_yearly_income,
        total_monthly_costs,
        total_yearly_costs,
        monthly_profit,
        yearly_profit
    ) = calculate_finances()

    print("\n========== SAVED MONEY ==========")

    print(f"Current Saved Money: {money:.2f} €")

    print("\n----- MONTHLY -----")

    print(f"Monthly Income: {total_monthly_income:.2f} €")
    print(f"Monthly Costs: {total_monthly_costs:.2f} €")
    print(f"Monthly Savings: {monthly_profit:.2f} €")

    print("\n----- YEARLY -----")

    print(f"Yearly Income: {total_yearly_income:.2f} €")
    print(f"Yearly Costs: {total_yearly_costs:.2f} €")
    print(f"Yearly Savings: {yearly_profit:.2f} €")

    print("\n----- TOTAL -----")

    print(f"Current Money: {money:.2f} €")
    print(f"Money After One Year: {money + yearly_profit:.2f} €")

    print("=================================")


# ==========================================
# MAIN MENU
# ==========================================

def main():

    while True:

        print("\n=================================")
        print("        ROBO MONEY MANAGER")
        print("=================================")

        print("1. Show Income")
        print("2. Add Money")
        print("3. Add Monthly Income")
        print("4. Add Yearly Income")
        print("5. Add Monthly Costs")
        print("6. Add Yearly Costs")
        print("7. Show All Costs")
        print("8. Show Saved Money")
        print("9. Exit")

        print("=================================")

        choice = input("Choose an option (1-9): ")

        if choice == "1":
            show_income()

        elif choice == "2":
            add_money()

        elif choice == "3":
            add_monthly_income()

        elif choice == "4":
            add_yearly_income()

        elif choice == "5":
            add_monthly_costs()

        elif choice == "6":
            add_yearly_costs()

        elif choice == "7":
            show_all_costs()

        elif choice == "8":
            show_saved_money()

        elif choice == "9":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid option. Please choose 1-9.")


# ==========================================
# START PROGRAM
# ==========================================

if __name__ == "__main__":
    main()