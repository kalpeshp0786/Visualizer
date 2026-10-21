import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class SalesDataAnalyzer:
    def __init__(self, file_path=None):
        self.data = pd.DataFrame()
        self.last_plot = None

        if file_path:
            self.load_data(file_path)

    def __del__(self):
        pass

    def load_data(self, file_path):
        file_path = file_path.strip().strip('"').strip("'")
        try:
            self.data = pd.read_csv(file_path)
            print("\nDataset loaded successfully!")
            print("Rows:", len(self.data), "| Columns:", len(self.data.columns))
            return True
        except FileNotFoundError:
            print("Error: File not found. Please check the CSV path.")
        except pd.errors.EmptyDataError:
            print("Error: The CSV file is empty.")
        except Exception as error:
            print("Unable to load dataset:", error)
        return False

    def check_data(self):
        if self.data.empty:
            print("Please load a dataset first.")
            return False
        return True

    def explore_data(self):
        if not self.check_data():
            return

        while True:
            print("\n== Explore Data ==")
            print("1. Display the first 5 rows")
            print("2. Display the last 5 rows")
            print("3. Display column names")
            print("4. Display data types")
            print("5. Display basic info")
            print("6. Back to Main Menu")
            choice = input("\nEnter your choice: ").strip()

            if choice == "1":
                print(self.data.head())
            elif choice == "2":
                print(self.data.tail())
            elif choice == "3":
                print(list(self.data.columns))
            elif choice == "4":
                print(self.data.dtypes)
            elif choice == "5":
                self.data.info()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")

    def clean_data(self):
        if not self.check_data():
            return

        while True:
            print("\n== Handle Missing Data ==")
            print("1. Display rows with missing values")
            print("2. Fill missing values with mean")
            print("3. Drop rows with missing values")
            print("4. Replace missing values with a specific value")
            print("5. Back to Main Menu")
            choice = input("\nEnter your choice: ").strip()

            if choice == "1":
                missing_rows = self.data[self.data.isnull().any(axis=1)]
                if missing_rows.empty:
                    print("\nNo missing values found in the dataset!")
                else:
                    print(missing_rows)
            elif choice == "2":
                numeric_columns = self.data.select_dtypes(include=np.number).columns
                for column in numeric_columns:
                    if self.data[column].isnull().any():
                        self.data[column] = self.data[column].fillna(self.data[column].mean())
                print("Missing values filled with mean where possible.")
            elif choice == "3":
                before = len(self.data)
                self.data.dropna(inplace=True)
                print("Dropped", before - len(self.data), "rows with missing values.")
            elif choice == "4":
                value = input("Enter the value to replace missing values: ")
                self.data.fillna(value, inplace=True)
                print("Missing values replaced successfully.")
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

    def mathematical_operations(self):
        if not self.check_data():
            return

        numeric = list(self.data.select_dtypes(include=np.number).columns)
        if not numeric:
            print("No numeric columns found.")
            return

        print("Numeric columns:", numeric)
        column = input("Enter a numeric column: ").strip()
        if column not in numeric:
            print("Column not found or not numeric.")
            return

        values = self.data[column].to_numpy()
        print("\nFirst values:", values[:5])
        print("First three values (slicing):", values[:3])
        if len(values):
            print("First value (indexing):", values[0])
        print("Values + 10:", values + 10)
        print("Values * 2:", values * 2)
        print("Values squared:", values ** 2)
        print("Sum:", np.sum(values))
        print("Mean:", np.mean(values))
        print("Standard deviation:", np.std(values))
        self.data[column + "_plus_10"] = values + 10
        print("Added column:", column + "_plus_10")

    def combine_data(self, other_dataframe):
        if not self.check_data():
            return
        self.data = pd.concat([self.data, other_dataframe], ignore_index=True)
        print("DataFrames combined successfully.")

    def split_data(self):
        if not self.check_data():
            return

        print("Available columns:", list(self.data.columns))
        column = input("Split by which column (e.g. Region or Product)? ").strip()
        if column not in self.data.columns:
            print("Column not found.")
            return

        for value, part in self.data.groupby(column, dropna=False):
            safe_name = str(value).replace(" ", "_").replace("/", "_")
            filename = "split_" + safe_name + ".csv"
            part.to_csv(filename, index=False)
            print("Saved", filename, "-", len(part), "rows")

    def search_sort_filter(self):
        if not self.check_data():
            return

        print("\n1. Search for text")
        print("2. Sort by a column")
        print("3. Filter by a column value")
        print("4. Filter numeric values above a limit")
        choice = input("Choose an option: ").strip()
        column = input("Enter column name: ").strip()

        if column not in self.data.columns:
            print("Column not found.")
            return

        if choice == "1":
            term = input("Enter text to search: ").strip()
            result = self.data[self.data[column].astype(str).str.contains(term, case=False, na=False)]
            print(result)
        elif choice == "2":
            order = input("Ascending order? (y/n): ").strip().lower()
            print(self.data.sort_values(column, ascending=(order != "n")))
        elif choice == "3":
            value = input("Enter exact value to filter: ").strip()
            print(self.data[self.data[column].astype(str).str.lower() == value.lower()])
        elif choice == "4":
            if not pd.api.types.is_numeric_dtype(self.data[column]):
                print("This column is not numeric.")
                return
            try:
                limit = float(input("Show rows where value is greater than: "))
                print(self.data[self.data[column] > limit])
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("Invalid option.")

    def aggregate_functions(self):
        if not self.check_data():
            return

        numeric = self.data.select_dtypes(include=np.number)
        if numeric.empty:
            print("No numeric columns available.")
            return

        print("\nSum:\n", numeric.sum())
        print("\nMean:\n", numeric.mean())
        print("\nMinimum:\n", numeric.min())
        print("\nMaximum:\n", numeric.max())
        print("\nCount:\n", numeric.count())

        column = input("\nEnter a column to group by (or press Enter to skip): ").strip()
        if column in self.data.columns:
            print(self.data.groupby(column, dropna=False)[numeric.columns].sum(numeric_only=True))

    def statistical_analysis(self):
        if not self.check_data():
            return

        numeric = self.data.select_dtypes(include=np.number)
        if numeric.empty:
            print("No numeric columns available.")
            return

        print("\n--- Descriptive Statistics ---")
        print(numeric.describe())
        print("\nStandard deviation:\n", numeric.std())
        print("\nVariance:\n", numeric.var())
        print("\n25th, 50th and 75th percentiles:\n", numeric.quantile([0.25, 0.50, 0.75]))

    def create_pivot_table(self):
        if not self.check_data():
            return

        print("Available columns:", list(self.data.columns))
        index_column = input("Enter grouping/index column: ").strip()
        value_column = input("Enter numeric values column: ").strip()

        if index_column not in self.data.columns or value_column not in self.data.columns:
            print("One or both columns were not found.")
            return
        if not pd.api.types.is_numeric_dtype(self.data[value_column]):
            print("Values column must be numeric.")
            return

        table = pd.pivot_table(
            self.data, index=index_column, values=value_column,
            aggfunc=["sum", "mean", "count"], fill_value=0
        )
        print(table)

    def _numeric_columns(self):
        return list(self.data.select_dtypes(include=np.number).columns)

    def visualize_data(self):
        if not self.check_data():
            return

        print("\n== Data Visualization ==")
        print("1. Bar Plot")
        print("2. Line Plot")
        print("3. Scatter Plot")
        print("4. Pie Chart")
        print("5. Histogram")
        print("6. Stack Plot")
        choice = input("\nEnter your choice: ").strip()
        numeric = self._numeric_columns()

        if choice in ("1", "2", "5", "6", "8") and not numeric:
            print("No numeric columns available.")
            return

        try:
            if choice in ("1", "2", "5", "6", "8"):
                print("Numeric columns:", numeric)
                column = input("Enter numeric column: ").strip()
                if column not in numeric:
                    print("Invalid numeric column.")
                    return

            if choice == "1":
                self.data[column].plot(kind="bar", title=column + " Bar Plot")
                plt.ylabel(column)
            elif choice == "2":
                self.data[column].plot(kind="line", marker="o", title=column + " Line Plot")
                plt.ylabel(column)
            elif choice == "3":
                x = input("Enter x-axis column name: ").strip()
                y = input("Enter y-axis column name: ").strip()
                if x not in self.data.columns or y not in self.data.columns:
                    print("Column not found. Please enter valid column names.")
                    return
                sns.scatterplot(data=self.data, x=x, y=y)
                plt.title(x + " vs " + y)
            elif choice == "4":
                print("Columns:", list(self.data.columns))
                category = input("Enter category column (e.g. Product or Region): ").strip()
                if category not in self.data.columns:
                    print("Column not found.")
                    return
                counts = self.data[category].value_counts().head(10)
                if counts.empty:
                    print("No data to plot.")
                    return
                counts.plot(kind="pie", autopct="%1.1f%%", title=category + " Distribution")
                plt.ylabel("")
            elif choice == "5":
                self.data[column].plot(kind="hist", bins=10, edgecolor="black", title=column + " Histogram")
                plt.xlabel(column)
            elif choice == "6":
                columns = [c for c in numeric[:5]]
                self.data[columns].fillna(0).plot.area(stacked=True, title="Stack Plot")
                plt.ylabel("Value")
            elif choice == "7":
                if len(numeric) < 2:
                    print("At least two numeric columns are needed for a heatmap.")
                    return
                sns.heatmap(self.data[numeric].corr(), annot=True, cmap="coolwarm", fmt=".2f")
                plt.title("Correlation Heatmap")
            elif choice == "8":
                sns.boxplot(data=self.data, y=column)
                plt.title(column + " Box Plot")
            elif choice == "9":
                if not numeric:
                    print("No numeric columns available.")
                    return
                columns = numeric[:4]
                fig, axes = plt.subplots(2, 2, figsize=(10, 7))
                for ax, col in zip(axes.flat, columns):
                    self.data[col].plot(kind="hist", ax=ax, title=col)
                for ax in axes.flat[len(columns):]:
                    ax.set_visible(False)
                fig.tight_layout()
            else:
                print("Invalid option.")
                return

            plt.tight_layout()
            self.last_plot = plt.gcf()
            plt.show()
            print("Plot displayed successfully.")
        except Exception as error:
            plt.close("all")
            print("Could not create plot:", error)

    def save_visualization(self):
        if self.last_plot is None:
            print("Create a plot first, then choose Save Visualization.")
            return

        print("\n== Save Visualization ==")
        filename = input("Enter file name to save the plot (e.g., scatter_plot.png): ").strip().strip('"').strip("'")
        if not filename:
            filename = "sales_plot.png"
        if not filename.lower().endswith((".png", ".jpg", ".jpeg")):
            filename += ".png"

        try:
            self.last_plot.savefig(filename, bbox_inches="tight", dpi=300)
            print("Visualization saved as", filename, "successfully!")
        except Exception as error:
            print("Unable to save visualization:", error)

    def export_results(self):
        if not self.check_data():
            return
        filename = input("Enter CSV output file name (e.g. analysis_result.csv): ").strip()
        if not filename:
            filename = "analysis_result.csv"
        if not filename.lower().endswith(".csv"):
            filename += ".csv"
        self.data.to_csv(filename, index=False)
        print("Results exported to", os.path.abspath(filename))

    def dataframe_operations_menu(self):
        while True:
            print("\n--- DataFrame Operations ---")
            print("1. Mathematical / NumPy operations")
            print("2. Search, Sort and Filter")
            print("3. Aggregate functions")
            print("4. Split data into CSV files")
            print("5. Combine another CSV file")
            print("6. Create Pivot Table")
            print("7. Back to Main Menu")
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.mathematical_operations()
            elif choice == "2":
                self.search_sort_filter()
            elif choice == "3":
                self.aggregate_functions()
            elif choice == "4":
                self.split_data()
            elif choice == "5":
                path = input("Enter path of another CSV file: ")
                path = path.strip().strip('"').strip("'")
                try:
                    other = pd.read_csv(path)
                    self.combine_data(other)
                except Exception as error:
                    print("Unable to combine file:", error)
            elif choice == "6":
                self.create_pivot_table()
            elif choice == "7":
                self.export_results()
            elif choice == "8":
                break
            elif choice == "9":
                break
            else:
                print("Invalid option. Try again.")

    def main_menu(self):
        while True:
            print("\n========== Data Analysis & Visualization Program ==========")
            print("Please select an option:")
            print("1. Load Dataset")
            print("2. Explore Data")
            print("3. Perform DataFrame Operations")
            print("4. Handle Missing Data")
            print("5. Generate Descriptive Statistics")
            print("6. Data Visualization")
            print("7. Save Visualization")
            print("8. Exit")
            print("============================================================")
            choice = input("\nEnter your choice: ").strip()

            if choice == "1":
                print("\n== Load Dataset ==")
                path = input("Enter the path of the dataset (CSV file): ")
                self.load_data(path)
            elif choice == "2":
                self.explore_data()
            elif choice == "3":
                self.dataframe_operations_menu()
            elif choice == "4":
                self.clean_data()
            elif choice == "5":
                self.statistical_analysis()
            elif choice == "6":
                self.visualize_data()
            elif choice == "7":
                self.save_visualization()
            elif choice == "8":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number from the menu.")


if __name__ == "__main__":
    print("Data Analysis & Visualization Program")
    analyzer = SalesDataAnalyzer()
    analyzer.main_menu()
