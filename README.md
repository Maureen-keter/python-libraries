
# Python Data Analysis & Visualization Project

This project demonstrates basic Python operations with **NumPy**, **Pandas**, **Requests**, and **Matplotlib**. It covers:

1. Creating and manipulating arrays with NumPy
2. Building and analyzing a dataset with Pandas
3. Fetching real-time data from a public API using Requests
4. Visualizing data using Matplotlib

---

## Features

* **NumPy**: Create an array of numbers from 1 to 10 and calculate the mean
* **Pandas**: Load a dataset into a DataFrame and display summary statistics
* **Requests (optional)**: Fetch current Bitcoin price from the CoinDesk API
* **Matplotlib**: Plot a simple line graph of squared numbers

---

## Project Structure

```
project/
│── answers.py          # Main script containing all functionality
│── README.md        # Documentation (this file)
│── requirements.txt # Required dependencies
```

---

## Installation

1. Clone this project (or create a new folder):

   ```bash
   git clone <your-repo-url>
   cd project
   ```

2. Create a virtual environment (recommended):

   ```bash
   python -m venv env
   source env/bin/activate  

   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## Requirements

The dependencies are listed in `requirements.txt`:

```
numpy
pandas
matplotlib
requests   # optional, only if you want to fetch API data
```

---

## Usage

Run the script with:

```bash
python3 answers.py
```

The script will:

* Calculate and print the mean of numbers 1–10
* Display summary statistics of a small dataset
* Fetch and display the current Bitcoin price (if internet is available)
* Plot a line graph showing the function

---

## Example Output

```text
Mean of array 1–10: 5.5

Summary statistics:
             Age      Grade
count   4.000000   4.000000
mean   21.500000  67.750000
std     1.290994  16.879475
min    20.000000  45.000000
25%    20.750000  61.500000
50%    21.500000  70.500000
75%    22.250000  76.750000
max    23.000000  85.000000

Current Bitcoin Price (USD): 68,245.87
```
