import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'], c='blue', marker='_')


    # Create first line of best fit
    best_fit_1 = linregress(x = df['Year'], y = df['CSIRO Adjusted Sea Level'])
    x_pred_1 = pd.Series([i for i in range(1880, 2051)])
    y_pred_1 = best_fit_1.slope * x_pred_1 + best_fit_1.intercept
    plt.plot(x_pred_1, y_pred_1, color = 'orange')

    # Create second line of best fit
    df2000 = df[df['Year'] >= 2000]
    best_fit_2 = linregress(x = df2000['Year'], y = df2000['CSIRO Adjusted Sea Level'])
    x_pred_2 = pd.Series([i for i in range(2000, 2051)])
    y_pred_2 = best_fit_2.slope * x_pred_2 + best_fit_2.intercept
    plt.plot(x_pred_2, y_pred_2, color = 'red')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    # Save plot and return df for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()