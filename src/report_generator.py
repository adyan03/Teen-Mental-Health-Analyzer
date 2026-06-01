import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import os

os.system('cls' if os.name == 'nt' else 'clear')

# Define Paths
PATH_DIR = Path(__file__).resolve().parent.parent
PATH_CSV = PATH_DIR / 'data' / 'Teen_Mental_Health_Dataset.csv'
REPORT_DIR = PATH_DIR / 'reports'

REPORT_DIR.mkdir(parents=True, exist_ok=True)

# Load Dataset
try:
    df = pd.read_csv(PATH_CSV)
    print("✅ Successfully loaded the dataset.")
except FileNotFoundError:
    print("❌ ERROR: File not found. Please check your data directory.")
    exit()

print("⏳ Generating visualizations...")

# Bar Chart 
platform_avg = df.groupby('platform_usage')['daily_social_media_hours'].mean()
plt.figure(figsize=(10,6))
platform_avg.plot(kind='bar', color=['#ff9999','#66b3ff','#99ff99', '#ffcc99'])
plt.title('Average Daily Social Media Hours by Platform')
plt.xlabel('Platforms Used')
plt.ylabel('Screen Time (Hours)')
plt.xticks(rotation=0)
plt.savefig(REPORT_DIR / 'chart1_platform_usage.png', bbox_inches='tight')
plt.clf() # Clear canvas

# Scatter Plot 
plt.figure(figsize=(10,6))
plt.scatter(df['screen_time_before_sleep'], df['sleep_hours'], color='purple', alpha=0.6)
plt.title('Impact of Screen Time on Sleep Hours')
plt.xlabel('Screen Time Before Sleep (Hours)')
plt.ylabel('Sleep Hours')
plt.savefig(REPORT_DIR / 'chart2_sleep_impact.png', bbox_inches='tight')
plt.clf() # Clear canvas

# Histogram 
stress_lv = df['stress_level']
plt.figure(figsize=(10,6))
plt.hist(stress_lv, color='skyblue', edgecolor='black', linewidth=1.2)
plt.title('Distribution of Stress Levels')
plt.xlabel('Stress Level (1-10)')
plt.ylabel('Frequency (Number of Teens)')
plt.savefig(REPORT_DIR / 'chart3_stress_distribution.png', bbox_inches='tight')
plt.clf() # Clear canvas

print(f"✅ SUCCESS! All reports saved to '{REPORT_DIR.name}' folder.")