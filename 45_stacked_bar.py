# Stacked Bar Chart

# Create a stacked bar chart showing the Indian Government budget allocation across the following categories:

#  Interest Payments
#  States' Share of Taxes & Duties
#  Central Sector Schemes
#  Defence
#  Centrally Sponsored Schemes
#  Finance Commission & Other Transfers
#  Subsidies
#  Pensions
#  Capital Expenditure
#  Rural Development

import matplotlib.pyplot as plt

budget_data = {
    "States' Share of Taxes & Duties": 20,
    "Interest Payments": 20,
    "Central Sector Schemes": 15,
    "Capital Expenditure": 14,
    "Defence": 8,
    "Centrally Sponsored Schemes": 8,
    "Finance Commission & Other Transfers": 6,
    "Subsidies": 5,
    "Rural Development": 2,
    "Pensions": 2
}

categories = list(budget_data.keys())
values = list(budget_data.values())

fig, ax = plt.subplots(figsize=(6, 9))
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

bottom_y = 0

# Stacking the bars using the 'bottom' parameter
for i, (category, val) in enumerate(zip(categories, values)):
    ax.bar("Union Budget", val, bottom=bottom_y, color=colors[i], label=f"{category} ({val}%)", width=0.5)
    
    # Adding percentage labels inside each stacked segment
    if val >= 5:
        ax.text("Union Budget", bottom_y + (val / 2), f"{val}%", 
                ha='center', va='center', color='white' if i in [0, 3, 4, 5] else 'black', 
                fontweight='bold', fontsize=10)
    elif val >= 2:
        ax.text("Union Budget", bottom_y + (val / 2), f"{val}%", 
                ha='center', va='center', color='black', 
                fontweight='bold', fontsize=8)
        
    bottom_y += val

ax.set_ylabel('Percentage Share (%)', fontsize=12, fontweight='bold')
ax.set_title('Indian Government Budget Allocation Share\n(True Stacked Bar Chart)', fontsize=14, fontweight='bold', pad=15)
ax.set_ylim(0, 105)
ax.grid(axis='y', linestyle='--', alpha=0.3)

# Placing the legend outside so it doesn't overlap the column
ax.legend(loc='center left', bbox_to_anchor=(1.05, 0.5), title="Categories", fontsize=10, title_fontsize=11)

plt.tight_layout()
plt.show()