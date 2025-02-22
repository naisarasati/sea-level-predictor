import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    #1. Read Data from File
    df = pd.read_csv('/Users/macbookair/Documents/Sea-level-predictor/sea-level-predictor/epa-sea-level.csv')
    print(df.head())

    #2. Create Scatter Plot
    plt.figure(figsize=(10,5))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    #3. Set Linear Regression for First Line Best Fit for 2050
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    #4. Generate Values
    years_value = range(df['Year'].min(), 2051)
    best_fit = slope * years_value + intercept

    #5. Create First Line Best Fit Plot
    plt.plot(years_value, best_fit)

    #6. Slicing Data from >2000
    df_from_2000 = df[df['Year'] >= 2000]

    #7. Set Linear Regression for Second Line Best Fit Between 2000 to 2050
    slope, intercept, r_value, p_value, std_err = linregress(df_from_2000['Year'], df_from_2000['CSIRO Adjusted Sea Level'])

    #8. Generate Second Line Values (2000 to 2050)
    second_years_value = range(df_from_2000['Year'].min(), 2051)
    second_best_fit = slope * second_years_value + intercept

    #9. Create Second Line Best Fit
    plt.plot(second_years_value, second_best_fit)

    # Add Labels and Title
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("CSIRO Adjusted Sea Level", fontsize=12)
    plt.title("Sea Level Rise Prediction", fontsize=14, fontweight="bold")
    
    # Save Plot and Return Data for Testing
    plt.savefig('sea_level_plot.png')
    return plt.gca()