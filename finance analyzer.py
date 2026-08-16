import numpy as np
import matplotlib.pyplot as plt


# ==========================================
# Personal Finance Analyzer
# ==========================================

FILE_NAME = "data/expenses.csv"


# ==========================================
# 1. Read data from CSV
# ==========================================

days = []
incomes = []
foods = []
transports = []
shoppings = []
entertainments = []

with open(FILE_NAME, "r", encoding="utf-8") as file:

    reader = csv.DictReader(file)

    for row in reader:

        days.append(row["date"])

        incomes.append(float(row["income"]))
        foods.append(float(row["food"]))
        transports.append(float(row["transport"]))
        shoppings.append(float(row["shopping"]))
        entertainments.append(float(row["entertainment"]))


# Convert lists to NumPy arrays

income = np.array(incomes)

food = np.array(foods)
transport = np.array(transports)
shopping = np.array(shoppings)
entertainment = np.array(entertainments)


# ==========================================
# 2. Calculate total expenses
# ==========================================

expenses = (
    food
    + transport
    + shopping
    + entertainment
)


# ==========================================
# 3. Calculate savings
# ==========================================

saving = income - expenses


# ==========================================
# 4. Financial Statistics
# ==========================================

total_income = np.sum(income)
total_expenses = np.sum(expenses)
total_saving = np.sum(saving)

average_income = np.mean(income)
average_expenses = np.mean(expenses)
average_saving = np.mean(saving)

highest_expense = np.max(expenses)
lowest_expense = np.min(expenses)

highest_income = np.max(income)

best_saving_index = np.argmax(saving)
worst_saving_index = np.argmin(saving)


# ==========================================
# 5. Expense Categories
# ==========================================

category_names = np.array([
    "Food",
    "Transport",
    "Shopping",
    "Entertainment"
])

category_values = np.array([
    np.sum(food),
    np.sum(transport),
    np.sum(shopping),
    np.sum(entertainment)
])


# ==========================================
# 6. Expense Percentages
# ==========================================

category_percentages = (
    category_values / total_expenses
) * 100


# ==========================================
# 7. Financial Report
# ==========================================

print()
print("=" * 55)
print("             PERSONAL FINANCE ANALYZER")
print("=" * 55)

print()

print("Total Income       :", round(total_income, 2))
print("Total Expenses     :", round(total_expenses, 2))
print("Total Saving       :", round(total_saving, 2))

print()

print("Average Daily Income   :", round(average_income, 2))
print("Average Daily Expense  :", round(average_expenses, 2))
print("Average Daily Saving   :", round(average_saving, 2))

print()

print("Highest Daily Income   :", round(highest_income, 2))
print("Highest Daily Expense  :", round(highest_expense, 2))
print("Lowest Daily Expense   :", round(lowest_expense, 2))

print()

print(
    "Best Saving Day        :",
    days[best_saving_index]
)

print(
    "Best Saving Amount     :",
    round(saving[best_saving_index], 2)
)

print()

print(
    "Worst Saving Day       :",
    days[worst_saving_index]
)

print(
    "Worst Saving Amount    :",
    round(saving[worst_saving_index], 2)
)


# ==========================================
# 8. Expense Report
# ==========================================

print()
print("-" * 55)
print("                  EXPENSE REPORT")
print("-" * 55)

for i in range(len(category_names)):

    print(
        category_names[i],
        ":",
        round(category_values[i], 2),
        "(",
        round(category_percentages[i], 2),
        "%)"
    )


# ==========================================
# 9. Financial Health
# ==========================================

saving_rate = (
    total_saving / total_income
) * 100
print()
print("-" * 55)
print("                FINANCIAL HEALTH")
print("-" * 55)

print(
    "Saving Rate:",
    round(saving_rate, 2),
    "%"
)


if saving_rate >= 30:

    print("Status: Excellent")

elif saving_rate >= 20:

    print("Status: Good")

elif saving_rate >= 10:

    print("Status: Average")

else:

    print("Status: Needs Improvement")


# ==========================================
# 10. Find days with high expenses
# ==========================================

expense_limit = average_expenses * 1.5

high_expense_indices = np.where(
    expenses > expense_limit
)[0]


print()
print("-" * 55)
print("                HIGH EXPENSE DAYS")
print("-" * 55)

if len(high_expense_indices) == 0:

    print("No unusually expensive days.")

else:

    for index in high_expense_indices:

        print(
            days[index],
            "->",
            round(expenses[index], 2)
        )


# ==========================================
# 11. Find days with negative saving
# ==========================================

negative_saving_indices = np.where(
    saving < 0
)[0]


print()
print("-" * 55)
print("                NEGATIVE SAVING DAYS")
print("-" * 55)

if len(negative_saving_indices) == 0:

    print("No negative saving days.")

else:

    for index in negative_saving_indices:

        print(
            days[index],
            "->",
            round(saving[index], 2)
        )


# ==========================================
# 12. Visualization 1
# Income vs Expenses
# ==========================================

plt.figure(figsize=(12, 6))

plt.plot(
    days,
    income,
    marker="o",
    label="Income"
)

plt.plot(
    days,
    expenses,
    marker="o",
    label="Expenses"
)

plt.title("Daily Income vs Expenses")

plt.xlabel("Date")
plt.ylabel("Amount")

plt.xticks(rotation=45)

plt.legend()

plt.grid()

plt.tight_layout()

plt.show()


# ==========================================
# 13. Visualization 2
# Daily Saving
# ==========================================

plt.figure(figsize=(12, 6))

plt.bar(
    days,
    saving
)

plt.axhline(
    average_saving,
    linestyle="--",
    label="Average Saving"
)

plt.title("Daily Saving")

plt.xlabel("Date")
plt.ylabel("Saving")

plt.xticks(rotation=45)

plt.legend()

plt.grid(axis="y")

plt.tight_layout()

plt.show()


# ==========================================
# 14. Visualization 3
# Expense Distribution
# ==========================================

plt.figure(figsize=(8, 8))

plt.pie(
    category_values,
    labels=category_names,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Expense Distribution")

plt.show()


# ==========================================
# 15. Visualization 4
# Expense Categories
# ==========================================

plt.figure(figsize=(12, 6))

plt.plot(
    days,
    food,
    label="Food"
)

plt.plot(
    days,
    transport,
    label="Transport"
)

plt.plot(
    days,
    shopping,
    label="Shopping"
)

plt.plot(
    days,
    entertainment,
    label="Entertainment"
)

plt.title("Expense Categories Over Time")

plt.xlabel("Date")
plt.ylabel("Amount")

plt.xticks(rotation=45)

plt.legend()

plt.grid()

plt.tight_layout()

plt.show()


# ==========================================
# 16. Visualization 5
# Income / Expense / Saving
# ==========================================

plt.figure(figsize=(12, 6))

plt.plot(
    days,
    income,
    label="Income"
)

plt.plot(
    days,
    expenses,
    label="Expenses"
)

plt.plot(
    days,
    saving,
    label="Saving"
)

plt.title("Financial Overview")

plt.xlabel("Date")
plt.ylabel("Amount")

plt.xticks(rotation=45)

plt.legend()

plt.grid()

plt.tight_layout()

plt.show()
