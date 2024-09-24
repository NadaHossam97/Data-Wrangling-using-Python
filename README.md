# Data Wrangling with Python: Adult Dataset

## Project Overview

This project focuses on data wrangling using the Adult dataset from the UCI Machine Learning Repository. The primary goal is to clean and preprocess the data to make it suitable for analysis. This involves handling missing values, normalizing numerical features, and creating dummy variables for categorical features.

## Dataset

The Adult dataset contains information about individuals from the 1994 Census database, with attributes such as age, education, work class, and income. The dataset can be found at [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/2/adult).

## Project Structure

## Libraries Used

- `pandas`: For data manipulation and analysis.
- `numpy`: For numerical operations.
- `matplotlib`: For data visualization.
- `seaborn`: For enhanced data visualization.

## Key Steps in Data Wrangling

1. **Import Libraries**: The necessary libraries are imported for data handling and visualization.

2. **Load Dataset**: The dataset is loaded into a pandas DataFrame.

3. **Handle Missing Values**: 
    - Replace "?" with NaN.
    - Fill missing values in categorical columns (`workclass`, `occupation`, `native-country`) with the mode (most frequent value).

4. **Normalize Numerical Features**: 
   - Normalize the following columns to a range of 0 to 1:
     - Age
     - Fnlwgt
     - Education Number
     - Capital Gain
     - Capital Loss
     - Hours per Week

5. **Create Dummy Variables**: Generate dummy variables for categorical columns (`workclass`, `education`, `marital-status`, `occupation`, `relationship`, `race`, `sex`).

## Running the Script

To run the data wrangling script, follow these steps:

1. Ensure you have Python installed on your machine.
2. Install the required libraries if you haven't already:

   ```bash
   pip install pandas numpy matplotlib seaborn

python data_wrangling.py


### Tips for Using the README

1. **Update Links**: Make sure to include links to any other resources, documentation, or files relevant to your project.
2. **Add More Sections**: Feel free to add any additional sections or details that you think would be useful for viewers of your portfolio.
3. **Formatting**: GitHub Markdown supports various formatting options, so adjust the README for clarity and presentation as needed.
