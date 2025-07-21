# %%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# Create graphs directory if it doesn't exist
os.makedirs("graphs", exist_ok=True)

# Set style for better looking plots
plt.style.use("seaborn-v0_8")

# %%
# GRAPH 1: HISTOGRAM - Customer Age Distribution in Online Store
print("=" * 60)
print("GRAPH 1: HISTOGRAM - Customer Age Distribution")
print("=" * 60)

# Generate fake data
np.random.seed(42)
ages = np.concatenate(
    [
        np.random.normal(25, 5, 150),  # Young adults
        np.random.normal(35, 8, 200),  # Middle-aged
        np.random.normal(50, 10, 120),  # Older adults
        np.random.normal(65, 6, 78),  # Seniors
    ]
)
ages = np.clip(ages, 18, 78)  # Keep ages realistic

plt.figure(figsize=(10, 6))
n, bins, patches = plt.hist(
    ages, bins=np.arange(18, 79, 5), color="steelblue", alpha=0.7, edgecolor="black"
)
plt.xticks(np.arange(min(bins), max(bins) + 1, 5.0))
plt.title("Customer Age Distribution in Online Store", fontsize=16, fontweight="bold")
plt.xlabel("Age (years)", fontsize=12)
plt.ylabel("Number of Customers", fontsize=12)
plt.grid(True, alpha=0.3)

# Color bars by age groups
for i, patch in enumerate(patches):
    if bins[i] < 30:
        patch.set_facecolor("lightcoral")  # Young: Light red
    elif bins[i] < 45:
        patch.set_facecolor("lightblue")  # Middle-aged: Light blue
    elif bins[i] < 60:
        patch.set_facecolor("lightgreen")  # Older: Light green
    else:
        patch.set_facecolor("lightyellow")  # Seniors: Light yellow

plt.tight_layout()
plt.savefig("graphs/histogram_customer_ages.png", dpi=300, bbox_inches="tight")
plt.show()

# Data Analysis
age_groups = pd.cut(
    ages, bins=[18, 33, 48, 63, 78], labels=["18-33", "34-48", "49-63", "64-78"]
)
age_counts = age_groups.value_counts().sort_index()

print("\n📦 DATA VALUES:")
print(f"Total customers: {len(ages)}")
for group, count in age_counts.items():
    print(f"Age group {group}: {count} customers ({count / len(ages) * 100:.1f}%)")

print("\n🎨 LEGEND:")
print("• Light Red: Young adults (18-33 years)")
print("• Light Blue: Middle-aged (34-48 years)")
print("• Light Green: Older adults (49-63 years)")
print("• Light Yellow: Seniors (64-78 years)")

print("\n🚀 COMPARISONS:")
print(
    f"• Most common age group: {age_counts.idxmax()} with {age_counts.max()} customers"
)
print(
    f"• Least common age group: {age_counts.idxmin()} with {age_counts.min()} customers"
)
print(f"• Average customer age: {np.mean(ages):.1f} years")

print("\n🤔 QUESTIONS:")
print("1. (Multiple Choice) Which age group has the most customers?")
print("   a) 18-33  b) 34-48  c) 49-63  d) 64-78")
print("   Answer: a) 18-33")
print("\n2. (True/False) More than 50% of customers are under 48 years old.")
print("   Answer: True")
print("\n3. (Short Answer) Which age group has the least number of customers?")
print("   Answer: 64-78")

# %%
# GRAPH 2: SCATTERPLOT - Product Price vs Sales Volume
print("\n" + "=" * 60)
print("GRAPH 2: SCATTERPLOT - Product Price vs Sales Volume")
print("=" * 60)

# Generate fake data with specific patterns for each category
np.random.seed(123)
n_products = 80

# Create category-specific data
n_electronics = 25
n_clothing = 30
n_books = 25

# Electronics: High prices (100-200), Low sales (200-600)
electronics_prices = np.random.uniform(100, 200, n_electronics)
electronics_sales = np.random.uniform(200, 600, n_electronics)

# Books: Low prices (10-80), High sales (600-1200)
books_prices = np.random.uniform(10, 80, n_books)
books_sales = np.random.uniform(600, 1200, n_books)

# Clothing: Medium prices (50-140), Medium sales (400-900)
clothing_prices = np.random.uniform(50, 140, n_clothing)
clothing_sales = np.random.uniform(400, 900, n_clothing)

# Combine all data
prices = np.concatenate([electronics_prices, clothing_prices, books_prices])
sales = np.concatenate([electronics_sales, clothing_sales, books_sales])
categories = np.array(
    ["Electronics"] * n_electronics + ["Clothing"] * n_clothing + ["Books"] * n_books
)

colors = {"Electronics": "red", "Clothing": "blue", "Books": "green"}

plt.figure(figsize=(12, 8))
for category in colors.keys():
    mask = categories == category
    plt.scatter(
        prices[mask],
        sales[mask],
        c=colors[category],
        label=category,
        alpha=0.7,
        s=60,
        edgecolors="black",
        linewidth=0.5,
    )

plt.title("Product Price vs Sales Volume by Category", fontsize=16, fontweight="bold")
plt.xlabel("Price ($)", fontsize=12)
plt.ylabel("Sales Volume (units sold)", fontsize=12)
plt.legend(title="Product Category", title_fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("graphs/scatterplot_price_vs_sales.png", dpi=300, bbox_inches="tight")
plt.show()

# Data Analysis
df_products = pd.DataFrame({"Price": prices, "Sales": sales, "Category": categories})

print("\n📦 DATA VALUES:")
print(f"Total products analyzed: {n_products}")
print(f"Price range: ${prices.min():.2f} - ${prices.max():.2f}")
print(f"Sales range: {sales.min():.0f} - {sales.max():.0f} units")

category_stats = (
    df_products.groupby("Category")
    .agg({"Price": ["mean", "count"], "Sales": "mean"})
    .round(2)
)

print("\nAverage by category:")
for category in colors.keys():
    cat_data = df_products[df_products["Category"] == category]
    print(
        f"• {category}: {len(cat_data)} products, avg price ${cat_data['Price'].mean():.2f}, avg sales {cat_data['Sales'].mean():.0f} units"
    )

print("\n🎨 LEGEND:")
print("• Red dots: Electronics")
print("• Blue dots: Clothing")
print("• Green dots: Books")

print("\n🚀 COMPARISONS:")
category_avg_price = (
    df_products.groupby("Category")["Price"].mean().sort_values(ascending=False)
)
print("Categories by average price (highest to lowest):")
for i, (category, price) in enumerate(category_avg_price.items(), 1):
    print(f"{i}. {category}: ${price:.2f}")

print("\n❓ QUESTIONS:")
print("1. (Multiple Choice) Which category generally has the highest prices?")
print("   a) Electronics  b) Clothing  c) Books")
print("   Answer: a) Electronics")
print(
    "\n2. (True/False) There is a positive correlation between price and sales volume."
)
print("   Answer: False (negative correlation)")
print("\n3. (Short Answer) What happens to sales volume as price increases?")
print("   Answer: Sales volume generally decreases as price increases")

# %%
# GRAPH 3: LINE CHART - Monthly Revenue Over 2 Years
print("\n" + "=" * 60)
print("GRAPH 3: LINE CHART - Monthly Revenue Over 2 Years")
print("=" * 60)

# Generate fake data
months = pd.date_range("2022-01-01", "2023-12-31", freq="ME")
np.random.seed(456)

# Base revenue with seasonal trends
base_revenue = 50000
seasonal_effect = 10000 * np.sin(
    np.arange(len(months)) * 2 * np.pi / 12
)  # Yearly cycle
growth_trend = np.arange(len(months)) * 1000  # Growth over time
noise = np.random.normal(0, 5000, len(months))
revenue = base_revenue + seasonal_effect + growth_trend + noise

plt.figure(figsize=(14, 8))
plt.plot(
    months,
    revenue,
    marker="o",
    linewidth=2.5,
    markersize=6,
    color="darkblue",
    markerfacecolor="lightblue",
    markeredgecolor="darkblue",
)
plt.title("Monthly Revenue Over 2 Years (2022-2023)", fontsize=16, fontweight="bold")
plt.xlabel("Month", fontsize=12)
plt.ylabel("Revenue ($)", fontsize=12)
plt.grid(True, alpha=0.3)

# Add trend line
z = np.polyfit(np.arange(len(months)), revenue, 1)
p = np.poly1d(z)
plt.plot(
    months,
    p(np.arange(len(months))),
    "--",
    color="red",
    alpha=0.8,
    linewidth=2,
    label="Trend Line",
)
plt.legend()

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("graphs/linechart_monthly_revenue.png", dpi=300, bbox_inches="tight")
plt.show()

# Data Analysis
df_revenue = pd.DataFrame({"Month": months, "Revenue": revenue})

print("\n📊 DATA VALUES:")
print(f"Total months: {len(months)}")
print(f"Revenue range: ${revenue.min():,.2f} - ${revenue.max():,.2f}")
print(f"Average monthly revenue: ${revenue.mean():,.2f}")

# Seasonal analysis
df_revenue["Month_Name"] = df_revenue["Month"].dt.strftime("%B")
monthly_avg = (
    df_revenue.groupby("Month_Name")["Revenue"].mean().sort_values(ascending=False)
)

print("\nMonthly averages:")
for month, avg_rev in monthly_avg.head(6).items():
    print(f"• {month}: ${avg_rev:,.2f}")

print("\n🎨 LEGEND:")
print("• Dark blue line with light blue markers: Monthly revenue")
print("• Red dashed line: Overall trend line")

print("\n📈 COMPARISONS:")
print("Months by average revenue (highest to lowest):")
for i, (month, revenue_val) in enumerate(monthly_avg.head(3).items(), 1):
    print(f"{i}. {month}: ${revenue_val:,.2f}")

yearly_revenue = df_revenue.groupby(df_revenue["Month"].dt.year)["Revenue"].sum()
print("\nYearly totals:")
for year, total in yearly_revenue.items():
    print(f"• {year}: ${total:,.2f}")
print(
    f"• Growth from 2022 to 2023: ${yearly_revenue[2023] - yearly_revenue[2022]:,.2f}"
)

print("\n❓ QUESTIONS:")
print("1. (Multiple Choice) Which year had highest total revenue?")
print("   Answer: 2023")
print("\n2. (True/False) Revenue shows a general upward trend over the 2-year period.")
print("   Answer: True")
print("\n3. (Short Answer) What was the lowest revenue?")
print(f"   Answer: ${revenue.min():,.0f}")

# %%
# GRAPH 4: BAR CHART - Sales Performance by Region
print("\n" + "=" * 60)
print("GRAPH 4: BAR CHART - Sales Performance by Region")
print("=" * 60)

# Generate fake data
regions = [
    "North America",
    "Europe",
    "Asia Pacific",
    "Latin America",
    "Middle East & Africa",
]
np.random.seed(789)
sales_values = [850000, 720000, 920000, 450000, 380000]
colors_bar = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]

plt.figure(figsize=(12, 8))
bars = plt.bar(
    regions, sales_values, color=colors_bar, alpha=0.8, edgecolor="black", linewidth=1
)
plt.title("Sales Performance by Region (Annual)", fontsize=16, fontweight="bold")
plt.xlabel("Region", fontsize=12)
plt.ylabel("Sales ($)", fontsize=12)
plt.grid(True, alpha=0.3, axis="y")

# Add value labels on bars
for bar, value in zip(bars, sales_values):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 10000,
        f"${value:,.0f}",
        ha="center",
        va="bottom",
        fontweight="bold",
    )

plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("graphs/barchart_regional_sales.png", dpi=300, bbox_inches="tight")
plt.show()

# Data Analysis
df_regions = pd.DataFrame({"Region": regions, "Sales": sales_values})

print("\n📊 DATA VALUES:")
total_sales = sum(sales_values)
print(f"Total global sales: ${total_sales:,.2f}")
for region, sales in zip(regions, sales_values):
    percentage = (sales / total_sales) * 100
    print(f"• {region}: ${sales:,.2f} ({percentage:.1f}%)")

print("\n🎨 LEGEND:")
colors_legend = ["Blue", "Orange", "Green", "Red", "Purple"]
for region, color in zip(regions, colors_legend):
    print(f"• {color}: {region}")

print("\n📈 COMPARISONS:")
sorted_regions = df_regions.sort_values("Sales", ascending=False)
print("Regions by sales performance (highest to lowest):")
for i, (_, row) in enumerate(sorted_regions.iterrows(), 1):
    print(f"{i}. {row['Region']}: ${row['Sales']:,.2f}")

best_region = sorted_regions.iloc[0]["Region"]
worst_region = sorted_regions.iloc[-1]["Region"]
print(f"\n• Best performing region: {best_region}")
print(f"• Lowest performing region: {worst_region}")
print(
    f"• Performance gap: ${sorted_regions.iloc[0]['Sales'] - sorted_regions.iloc[-1]['Sales']:,.2f}"
)

print("\n❓ QUESTIONS:")
print("1. (Multiple Choice) Which region has the highest sales?")
print("   a) North America  b) Europe  c) Asia Pacific  d) Latin America")
print("   Answer: c) Asia Pacific")
print("\n2. (True/False) Europe outperformed North America in sales.")
print("   Answer: False")
print("\n3. (Short Answer) What was the sales volume of Latin America?")
print(f"   Answer: ${sales_values[3]:,.0f}")

# %%
# GRAPH 5: PIE CHART - Market Share by Company
print("\n" + "=" * 60)
print("GRAPH 5: PIE CHART - Market Share by Company")
print("=" * 60)

# Generate fake data
companies = ["TechCorp", "InnovateInc", "FutureSoft", "DataDyne", "CloudMax", "Others"]
market_shares = [28.5, 22.3, 18.7, 12.8, 9.2, 8.5]
colors_pie = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#ff99cc", "#c2c2f0"]

plt.figure(figsize=(10, 10))
wedges, texts = plt.pie(
    market_shares,
    labels=None,  # Remove default labels
    colors=colors_pie,
    autopct=None,  # Hide percentages
    startangle=90,
    explode=None,  # No exploded slices
)

plt.title("Market Share by Company", fontsize=16, fontweight="bold", pad=20)

# Add company names inside slices
for i, (wedge, company) in enumerate(zip(wedges, companies)):
    angle = (wedge.theta2 + wedge.theta1) / 2
    x = 0.6 * np.cos(np.radians(angle))
    y = 0.6 * np.sin(np.radians(angle))
    plt.text(
        x,
        y,
        company,
        ha="center",
        va="center",
        fontsize=15,
        fontweight="bold",
        color="black",
    )

# No percentage text formatting needed since autopct=None

plt.axis("equal")
plt.tight_layout()
plt.savefig("graphs/piechart_market_share.png", dpi=300, bbox_inches="tight")
plt.show()

# Data Analysis
df_market = pd.DataFrame({"Company": companies, "Market_Share": market_shares})

print("\n📦 DATA VALUES:")
print("Market share breakdown:")
for company, share in zip(companies, market_shares):
    print(f"• {company}: {share}%")

print("\n🎨 LEGEND:")
color_names = [
    "Light Red",
    "Light Blue",
    "Light Green",
    "Light Orange",
    "Light Pink",
    "Light Purple",
]
for company, color in zip(companies, color_names):
    print(f"• {color}: {company}")

print("\n🚀 COMPARISONS:")
sorted_market = df_market.sort_values("Market_Share", ascending=False)
print("Companies by market share (largest to smallest):")
for i, (_, row) in enumerate(sorted_market.iterrows(), 1):
    print(f"{i}. {row['Company']}: {row['Market_Share']}%")

top_3_share = sorted_market.head(3)["Market_Share"].sum()
print(f"\n• Top 3 companies control: {top_3_share}% of the market")
print(
    f"• Market leader advantage: {sorted_market.iloc[0]['Market_Share'] - sorted_market.iloc[1]['Market_Share']:.1f} percentage points"
)

print("\n❓ QUESTIONS:")
print("1. (Multiple Choice) Which company has the largest market share?")
print("   a) TechCorp  b) InnovateInc  c) FutureSoft  d) DataDyne")
print("   Answer: a) TechCorp")
print("\n2. (True/False) The top 3 companies control more than 60% of the market.")
print("   Answer: True")
print(
    "\n3. (Short Answer) What percentage of the market do the top 2 companies control combined?"
)
print(f"   Answer: {sorted_market.head(2)['Market_Share'].sum():.1f}%")

# %%
# GRAPH 6: STACKED BAR CHART - Plant Composition Comparison
print("\n" + "=" * 60)
print("GRAPH 6: STACKED BAR CHART - Plant Composition Comparison")
print("=" * 60)

# Generate fake data for 4 plants (each totaling 100%)
plants = ["Sunflower", "Oak Tree", "Rose Bush", "Tomato Plant"]
np.random.seed(202324)

# Plant composition by parts (percentages that sum to 100% for each plant)
roots_pct = [18, 23, 26, 25]  # Roots percentage for each plant
stem_pct = [55, 40, 30, 45]  # Stem percentage for each plant
leaves_pct = [27, 37, 44, 30]  # Leaves percentage for each plant

# Verify each plant sums to 100%
for i, plant in enumerate(plants):
    total = roots_pct[i] + stem_pct[i] + leaves_pct[i]
    assert total == 100, f"{plant} doesn't sum to 100%"

# Create stacked bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Define colors for each category
colors = ["#FF6B6B", "#4ECDC4", "#45B7D1"]

# Create the stacked bars
bars1 = ax.bar(plants, roots_pct, color=colors[0], label="Roots")
bars2 = ax.bar(plants, stem_pct, bottom=roots_pct, color=colors[1], label="Stem")
bars3 = ax.bar(
    plants,
    leaves_pct,
    bottom=[r + s for r, s in zip(roots_pct, stem_pct)],
    color=colors[2],
    label="Leaves",
)

plt.title("Plant Composition Comparison", fontsize=16, fontweight="bold")
plt.xlabel("Plant Type", fontsize=12)
plt.ylabel("Percentage of Total Plant Mass (%)", fontsize=12)
plt.legend(title="Plant Parts", title_fontsize=12, loc="center left", bbox_to_anchor=(1, 0.5))
plt.grid(True, alpha=0.3, axis="y")

plt.ylim(0, 100)
plt.tight_layout()
plt.savefig("graphs/stackedbar_plant_composition.png", dpi=300, bbox_inches="tight")
plt.show()

# Data Analysis
df_plants = pd.DataFrame(
    {
        "Plant": plants,
        "Roots": roots_pct,
        "Stem": stem_pct,
        "Leaves": leaves_pct,
    }
)

print("\n📦 DATA VALUES:")
print("Plant composition breakdown (percentage of total plant mass):")
for i, plant in enumerate(plants):
    print(f"\n{plant}:")
    print(f"  • Roots: {roots_pct[i]}%")
    print(f"  • Stem: {stem_pct[i]}%")
    print(f"  • Leaves: {leaves_pct[i]}%")

print("\n🎨 LEGEND:")
print("• Red: Roots")
print("• Teal: Stem")
print("• Blue: Leaves")

print("\n🚀 COMPARISONS:")
# Calculate average percentages across plants
avg_roots = np.mean(roots_pct)
avg_stem = np.mean(stem_pct)
avg_leaves = np.mean(leaves_pct)

parts_avg = [
    ("Roots", avg_roots),
    ("Stem", avg_stem),
    ("Leaves", avg_leaves),
]
parts_avg.sort(key=lambda x: x[1], reverse=True)

print("Plant parts by average composition (highest to lowest):")
for i, (part, avg_pct) in enumerate(parts_avg, 1):
    print(f"{i}. {part}: {avg_pct:.1f}%")

print("\nPlant characteristics:")
print(f"• Oak Tree has the highest stem percentage ({max(stem_pct)}%)")
print(f"• Tomato Plant has the most leaves ({max(leaves_pct)}%)")
print("• Rose Bush has balanced composition across all parts")

print("\n🤔 QUESTIONS:")
print(
    "1. (Multiple Choice) Which plant part has the lowest average percentage across all plants?"
)
print("   a) Roots  b) Stem  c) Leaves")
print("   Answer: a) Roots")
print("\n2. (True/False) Oak Tree has the highest stem percentage among all plants.")
print("   Answer: False")
print(
    "\n3. (Short Answer) Which plant has the most balanced composition across all parts?"
)
print("   Answer: Tomato Plant")

