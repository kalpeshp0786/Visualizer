# Sales Data Analyzer

## Project Overview
Sales Data Analyzer is a menu-driven Python program for loading, exploring, cleaning, analyzing, and visualizing data from CSV files. It uses Pandas and NumPy for data operations and Matplotlib and Seaborn for charts.

## Features
- Load a dataset from a CSV file.
- Explore the first and last five rows, column names, data types, and basic dataset information.
- Handle missing values by displaying affected rows, filling numeric missing values with the mean, dropping rows with missing values, or replacing missing values with a chosen value.
- Perform NumPy operations on numeric columns, including indexing, slicing, addition, multiplication, squaring, sum, mean, and standard deviation.
- Search text, sort rows, and filter by exact values or numeric limits.
- Calculate aggregate values: sum, mean, minimum, maximum, and count.
- Generate descriptive statistics, variance, standard deviation, and percentiles.
- Create pivot tables.
- Split data into separate CSV files by a selected column.
- Combine another CSV file with the current dataset.
- Create bar, line, scatter, pie, histogram, area/stack, heatmap, and box plots (where supported by the code).
- Save the most recently created visualization as an image.
- Export the current dataset to a CSV file.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Installation
Make sure Python is installed. Install the required libraries with:

```bash
python -m pip install numpy pandas matplotlib seaborn
```

On Windows PowerShell, if you need to use a particular Python installation:

```powershell
& "C:\Path\To\Python\python.exe" -m pip install numpy pandas matplotlib seaborn
```

Replace `C:\Path\To\Python\python.exe` with your actual Python executable path.

## How to Run
1. Save the program code in a Python file, for example `Visualizer.py`.
2. Open PowerShell or a terminal in the folder containing that file.
3. Run the program:

```bash
python Visualizer.py
```

Replace `Visualizer.py` with the actual filename if yours is different.

## How to Use
1. Start the program.
2. Choose **1. Load Dataset**.
3. Enter the path to your CSV file, for example:

   ```text
   C:\Users\YourName\Downloads\sales_data.csv
   ```

4. Select an option from the main menu and follow the prompts.
5. To save a chart, create a visualization first and then choose **Save Visualization**.
6. Use the export option in the DataFrame Operations menu to save the current data as a CSV file.

Tip: If you copy a file path surrounded by quotation marks, the program removes those quotation marks automatically.

## Main Menu
1. **Load Dataset** — load a CSV file.
2. **Explore Data** — inspect rows, columns, data types, and dataset information.
3. **Perform DataFrame Operations** — calculations, search/sort/filter, aggregation, splitting, combining, and pivot tables.
4. **Handle Missing Data** — inspect or handle missing values.
5. **Generate Descriptive Statistics** — calculate summary statistics for numeric columns.
6. **Data Visualization** — create charts from the loaded dataset.
7. **Save Visualization** — save the latest chart as an image.
8. **Exit** — close the program.

## Output Files
Depending on the selected operations, the program may create:
- `split_<value>.csv` — CSV files created when splitting data by a column.
- `analysis_result.csv` — the default exported dataset filename (or a name you enter).
- `.png`, `.jpg`, or `.jpeg` files — saved chart images.

Files are saved in the current working directory unless you provide a different path.

## Notes
- The input dataset must be a readable CSV file.
- Numeric operations and many plots require numeric columns.
- Scatter plots require valid X and Y columns.
- Pie charts display up to the ten most frequent values in the selected category column.
- The actual output depends on the dataset and options selected.

## Project Structure
```text
Project Folder/
├── Visualizer.py       # Python source file (use your actual filename)
├── README.md           # Project documentation
└── sales_data.csv      # Input dataset (example; add your own file)
```

## Author
Add your name here.
