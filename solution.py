import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


# STEP 0: Data Loading and Cleaning

df = pd.read_csv('last_mile_delivery_dataset.csv')

df['order_date'] = pd.to_datetime(df['order_date'])
df['month'] = df['order_date'].dt.month

df['order_time'] = pd.to_datetime(df['order_time'], format='%H:%M', errors='coerce')
df['hour'] = df['order_time'].dt.hour

df['vehicle_type'] = df['vehicle_type'].str.title()

print("--- Data Loading & Cleaning Complete ---\n")

# Q1: Peak Hour Delay Pattern

print("--- Q1: Peak Hour Delay Pattern ---")
peak_condition = df['hour'].isin([8, 9, 17, 18, 19])

peak_data = df[peak_condition]
off_peak_data = df[~peak_condition]

peak_avg_delay = peak_data['delay_mins'].mean()
off_peak_avg_delay = off_peak_data['delay_mins'].mean()
diff = peak_avg_delay - off_peak_avg_delay

print(f"Average Peak Delay: {peak_avg_delay:.2f} mins")
print(f"Average Off-Peak Delay: {off_peak_avg_delay:.2f} mins")
print(f"Difference: {diff:.2f} mins\n")


# Q2: Weather vs. Delay Correlation

print("--- Q2: Weather vs. Delay Correlation ---")
weather_delay = df.groupby('weather_condition')['delay_mins'].median()
print("Median Delay by Weather Condition:")
print(weather_delay)

rain_data = df[df['weather_condition'] == 'Rain']
rain_impact = rain_data.groupby('order_type')['delay_mins'].median().sort_values(ascending=False)
print("\nOrder Type hit hardest by Rain:")
print(rain_impact.head(1))
print("\n")


# Q3: Rider Experience Effect (Statistics)

print("--- Q3: Rider Experience Effect ---")
novice_riders = df[df['rider_experience_yrs'] < 2]['delay_mins'].dropna()
veteran_riders = df[df['rider_experience_yrs'] > 4]['delay_mins'].dropna()

t_stat, p_value = stats.ttest_ind(novice_riders, veteran_riders)

print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")

if p_value < 0.05:
    print("Conclusion: There is a statistically meaningful difference in delays between <2yr and >4yr riders.\n")
else:
    print("Conclusion: The difference in delays is NOT statistically meaningful.\n")


# Q4: City-Level Performance Dashboard

print("--- Q4: Generating Dashboard (Check for pop-up window) ---")

df['is_on_time'] = df['delay_mins'] <= 0

sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle('Last-Mile Delivery Performance Dashboard', fontsize=16, fontweight='bold')

city_performance = df.groupby('city')['is_on_time'].mean() * 100
city_performance.sort_values().plot(kind='bar', ax=axes[0], color='cornflowerblue', edgecolor='black')
axes[0].set_title('City-wise On-Time Rate (%)')
axes[0].set_ylabel('On-Time %')
axes[0].set_xlabel('City')
axes[0].tick_params(axis='x', rotation=45)

monthly_trend = df.groupby('month')['delay_mins'].mean()
monthly_trend.sort_index().plot(kind='line', marker='o', ax=axes[1], color='crimson', linewidth=2)
axes[1].set_title('Average Delay by Month')
axes[1].set_ylabel('Avg Delay (mins)')
axes[1].set_xlabel('Month (1-12)')
axes[1].set_xticks(range(1, 13))

sns.boxplot(data=df, x='vehicle_type', y='delay_mins', ax=axes[2], palette='Set2')
axes[2].set_title('Delay Distribution by Vehicle Type')
axes[2].set_ylabel('Delay (mins)')
axes[2].set_xlabel('Vehicle Type')

plt.tight_layout()
plt.show()