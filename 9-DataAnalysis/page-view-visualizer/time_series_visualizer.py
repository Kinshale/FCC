import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

df = pd.read_csv("fcc-forum-pageviews.csv")
df = df[(df['value'] > df['value'].quantile(0.025)) & (df['value'] < df['value'].quantile(0.975))]

def draw_line_plot():
    fig = plt.figure(figsize=(25, 7))
    plt.plot(df['date'], df['value'], color='red')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date', fontsize = 14)
    plt.xticks(ticks=[], labels=[])
    plt.ylabel('Page Views', fontsize = 14)

    fig.savefig('plots/line_plot.png')
    return fig

def draw_bar_plot():
    df_bar = df.copy(deep=True)

    df_bar['date'] = pd.to_datetime(df['date'])
    df_bar['year'] = df_bar['date'].dt.year
    df_bar['month'] = df_bar['date'].dt.month

    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().reset_index(name='mean')

    df_pivot = df_bar.pivot(index='year', columns='month', values='mean')
   
    fig = df_pivot.plot(kind='bar', figsize=(14, 7), width=0.6).get_figure()

    plt.xlabel('Years', fontsize=14)
    plt.ylabel('Average Page Views', fontsize=14)
    
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    plt.legend(title='Months', labels=months, title_fontsize=14, fontsize=12)
    
    fig.savefig('plots/bar_plot.png')
    return fig

def draw_box_plot():
    df_box = df.copy(deep=True)

    df_box['date'] = pd.to_datetime(df['date'])
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')

    # Order the months
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df_box['month'] = pd.Categorical(df_box['month'], categories=month_order, ordered=True)

    fig, axes = plt.subplots(1, 2, figsize=(20, 6)) 

    sns.boxplot(ax=axes[0], df=df_box, x='year', y='value', hue = 'year', palette='bright', dodge=False, legend=False).get_figure()
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    sns.boxplot(ax=axes[1], df=df_box, x='month', y='value', hue = 'month', palette='husl', dodge=False, legend=False).get_figure()
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    fig.savefig('plots/box_plot.png')
    return fig
