import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Dataset Generation
np.random.seed(42)
dates = pd.date_range(start='2026-01-01', periods=120, freq='D')
categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Beauty']
regions = ['North', 'South', 'East', 'West']

data = {
    'Transaction_ID': range(1001, 1501),
    'Date': np.random.choice(dates, 500),
    'Category': np.random.choice(categories, 500, p=[0.3, 0.25, 0.2, 0.15, 0.1]),
    'Region': np.random.choice(regions, 500),
    'Unit_Price': np.random.uniform(15.0, 450.0, 500),
    'Quantity': np.random.randint(1, 8, 500)
}

df = pd.DataFrame(data)
df['Total_Revenue'] = df['Unit_Price'] * df['Quantity']

# 2. Key Metrics
print("=== BUSINESS SALES PERFORMANCE REPORT ===")
print(f"Total Revenue     : ${df['Total_Revenue'].sum():,.2f}")
print(f"Total Units Sold  : {df['Quantity'].sum():,}")
print(f"Avg Order Value   : ${df['Total_Revenue'].mean():,.2f}")

# 3. Save Visualization Plot
plt.figure(figsize=(10, 5))
sns.barplot(data=df, x='Category', y='Total_Revenue', hue='Region', estimator=sum, errorbar=None)
plt.title('Revenue by Category & Region')
plt.tight_layout()
plt.savefig('sales_performance.png')
plt.close()
