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
    
    
    # Customize the graph
    plt.title('Ward Occupancy Over 7 Days', fontsize=15, fontweight='bold', pad=15)
    plt.xlabel('Day', fontsize=13)
    plt.ylabel('Number of Patients', fontsize=13)
    plt.xticks(days)
    plt.ylim(bottom=0)
    plt.legend(loc='upper left', fontsize=11)
    plt.grid(True, alpha=0.3, linestyle='--', axis='y')
     
    plt.tight_layout()
    plt.show()
    return ward_occupancy

def reuse_calculate_ward_occupancy(admission, discharge):
    ward_occupancy = []
    current_occupancy = 0 # Initialize variable
    for i in range(len(admission)):
        current_occupancy += admission[i] - discharge[i]
        ward_occupancy.append(current_occupancy)

# testing
admission = [11, 17, 28, 20, 21, 15, 14]
discharge = [2, 5, 12, 13, 30, 21, 15]
calculate_ward_occupancy(admission, discharge)