import matplotlib.pyplot as plt
import numpy as np 

def calculate_ward_occupancy(admission, discharge):
    ward_occupancy = []
    current_occupancy = 0 # Initialize variable
    for i in range(len(admission)):
        current_occupancy += admission[i] - discharge[i]
        ward_occupancy.append(current_occupancy)
    
    # Generate a graph with both line and bars
    days = list(range(1, 8))
    
    plt.figure(figsize=(12, 6))
    
    # Bar chart for daily occupancy
    bars = plt.bar(days, ward_occupancy, alpha=0.5, color='#2E86AB', 
                   edgecolor='black', linewidth=1.5, label='Daily Occupancy')
    
    # Line plot on top of bars
    plt.plot(days, ward_occupancy, marker='o', linewidth=2.5, markersize=9,
             color='#A23B72', markerfacecolor='#A23B72', markeredgecolor='white',
             markeredgewidth=2, label='Trend Line')
    
    # Add value labels on top of bars
    for bar, occ in zip(bars, ward_occupancy):
        plt.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.3,
                 f'{occ}', ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    # Add average line
    avg_occupancy = np.mean(ward_occupancy)
    plt.axhline(y=avg_occupancy, color='red', linestyle='--', alpha=0.7,
                label=f'Average = {avg_occupancy:.1f}')
    
    # Customize the graph
    plt.title('Ward Occupancy Over 7 Days', fontsize=15, fontweight='bold', pad=15)
    plt.xlabel('Day', fontsize=13)
    plt.ylabel('Number of Patients', fontsize=13)
    plt.xticks(days)
    plt.ylim(bottom=0)
    plt.legend(loc='upper left', fontsize=11)
    plt.grid(True, alpha=0.3, linestyle='--', axis='y')
    
    # Add annotation for max occupancy
    max_occ = max(ward_occupancy)
    max_day = days[ward_occupancy.index(max_occ)]
    plt.annotate(f'Peak: {max_occ} patients', xy=(max_day, max_occ),
                 xytext=(max_day + 0.5, max_occ + 1),
                 arrowprops=dict(arrowstyle='->', color='darkred', lw=1.5),
                 fontsize=10, color='darkred', fontweight='bold')
    
    plt.tight_layout()
    plt.show()
    return ward_occupancy