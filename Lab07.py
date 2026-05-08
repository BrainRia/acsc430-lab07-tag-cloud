from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

DATA_FILE = Path(__file__).resolve().parent / "sales.csv"
PRODUCT_COLUMNS = [
    "facecream",
    "facewash",
    "toothpaste",
    "bathingsoap",
    "shampoo",
    "moisturizer",
]


def load_sales_data() -> pd.DataFrame:
    # Read the csv file that contains the company sales data
    return pd.read_csv(DATA_FILE)


def print_menu() -> None:
    print("\nLab 07 Menu")
    print("1. Print the month with the biggest profit")
    print("2. Print the average yearly sales for all products")
    print("3. Print filtered records for toothpaste and face cream")
    print("4. Plot total profit for all months")
    print("5. Plot monthly units sold for each product")
    print("6. Show correlation of face cream and shampoo sales")
    print("7. Show shampoo sales using a bar chart")
    print("8. Calculate yearly average sales of moisturizer using NumPy")
    print("9. Plot total units sold using a NumPy array")
    print("10. Exit")


def exercise_1(df: pd.DataFrame) -> None:
    # Find the row with the highest total profit
    max_profit_row = df.loc[df["total_profit"].idxmax()]
    print(
        f"Month with biggest profit: {int(max_profit_row['month_number'])} "
        f"(profit = {int(max_profit_row['total_profit'])})"
    )


def exercise_2(df: pd.DataFrame) -> None:
    # Calculate the average sales for each product column
    averages = df[PRODUCT_COLUMNS].mean()
    print("Average yearly sales for all products:")
    for product, average in averages.items():
        print(f"{product}: {average:.2f}")


def exercise_3(df: pd.DataFrame) -> None:
    # Keep only rows where both conditions are true
    filtered_df = df[(df["toothpaste"] > 6000) & (df["facecream"] < 3000)]
    if filtered_df.empty:
        print("No records matched the conditions.")
        return

    print(filtered_df.to_string(index=False))


def exercise_4(df: pd.DataFrame) -> None:
    # Simple line plot for total profit by month
    plt.figure("Total Profit by Month")
    plt.plot(df["month_number"], df["total_profit"], marker="o")
    plt.xlabel("Month")
    plt.ylabel("Profit")
    plt.title("Total Profit for All Months")
    plt.xticks(df["month_number"])
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def exercise_5(df: pd.DataFrame) -> None:
    # Draw one line for each product so they can be compared
    plt.figure("Monthly Units Sold by Product")
    for product in PRODUCT_COLUMNS:
        plt.plot(df["month_number"], df[product], marker="o", label=product)

    plt.xlabel("Month")
    plt.ylabel("Units Sold")
    plt.title("Number of Units Sold per Month for Each Product")
    plt.xticks(df["month_number"])
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def exercise_6(df: pd.DataFrame) -> None:
    # Scatterplot helps show if the two products move together
    plt.figure("Face Cream vs Shampoo")
    plt.scatter(df["facecream"], df["shampoo"], color="purple")
    plt.xlabel("Face Cream Sales")
    plt.ylabel("Shampoo Sales")
    plt.title("Correlation Between Face Cream and Shampoo Sales")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def exercise_7(df: pd.DataFrame) -> None:
    # Bar chart for shampoo sales in every month
    plt.figure("Shampoo Sales by Month")
    plt.bar(df["month_number"], df["shampoo"], color="skyblue")
    plt.xlabel("Month")
    plt.ylabel("Shampoo Sales")
    plt.title("Shampoo Sales for All Months")
    plt.xticks(df["month_number"])
    plt.tight_layout()
    plt.show()


def exercise_8(df: pd.DataFrame) -> None:
    # Convert the moisturizer column to a NumPy array first
    moisturizer_array = df[["moisturizer"]].to_numpy()
    average_sales = np.mean(moisturizer_array)
    print(f"Yearly average moisturizer sales: {average_sales:.2f}")


def exercise_9(df: pd.DataFrame) -> None:
    # Use to_numpy() and then split the month and total units columns
    sales_array = df[["month_number", "total_units"]].to_numpy()
    x_values = sales_array[:, 0]
    y_values = sales_array[:, 1]

    plt.figure("Total Units Sold by Month")
    plt.plot(
        x_values,
        y_values,
        linestyle="dotted",
        color="red",
        marker="o",
        markerfacecolor="red",
        markeredgecolor="red",
        label="Total Units Sold",
    )
    plt.xlabel("Month Number")
    plt.ylabel("Sold units number")
    plt.title("Total Units Sold for All Months")
    plt.xticks(x_values)
    plt.legend(loc="upper right")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def handle_choice(choice: str, df: pd.DataFrame) -> bool:
    if choice == "1":
        exercise_1(df)
    elif choice == "2":
        exercise_2(df)
    elif choice == "3":
        exercise_3(df)
    elif choice == "4":
        exercise_4(df)
    elif choice == "5":
        exercise_5(df)
    elif choice == "6":
        exercise_6(df)
    elif choice == "7":
        exercise_7(df)
    elif choice == "8":
        exercise_8(df)
    elif choice == "9":
        exercise_9(df)
    elif choice == "10":
        print("Exiting program.")
        return False
    else:
        print("Invalid selection. Please choose a number from 1 to 10.")

    return True


def main() -> None:
    # Load the data once and reuse it for all menu options
    df = load_sales_data()

    running = True
    while running:
        print_menu()
        choice = input("Enter your choice (1-10): ").strip()
        running = handle_choice(choice, df)


if __name__ == "__main__":
    main()
