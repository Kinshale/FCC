import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("/home/ale/Desktop/FCC/9-DataAnalysis/medical_data_visualizer/medical_examination.csv")

df['overweight'] = ( df['weight'] / ((df ['height']) ** 2) > 0.0025 ).astype(int)
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

def draw_cat_plot():
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    
    df_cat = pd.DataFrame(df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total'))
    

    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar').figure

    fig.savefig('catplot.png')
    return fig

def draw_heat_map():
  
  df_heat = df[(df['ap_lo'] <= df['ap_hi'])
    & (df['height'] >= df['height'].quantile(0.025))
    & (df['height'] <= df['height'].quantile(0.975))
    & (df['weight'] >= df['weight'].quantile(0.025))
    & (df['weight'] <= df['weight'].quantile(0.975))]

  corr = df_heat.corr()

  # Upper triangle mask
  n = corr.shape[0]
  mask = np.array([[i >= j for i in range(n)] for j in range(n)], dtype = bool )

  fig, ax = plt.subplots(figsize=(11, 11))
  sns.heatmap(corr, annot=True, fmt='.1f', linewidths=0.5, mask=mask, center=0, vmin=-0.1, vmax=0.25, cbar_kws={'shrink': .45, 'format': '%.2f'}, ax=ax)
  
  # Do not modify the next two lines
  fig.savefig('heatmap.png')
  return fig