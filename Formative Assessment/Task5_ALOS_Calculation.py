import matplotlib.pyplot as plt
import numpy as np

def calculate_daily_occupancy(admissions, discharges, initial_bed=0):
    occupancy = []
    current = initial_bed
    for a, d in zip(admissions, discharges):
        current += a - d
        occupancy.append(current)
    return occupancy

def calculate_alos(admissions, discharges, initial_bed=0):
    daily_occupancy = calculate_daily_occupancy(admissions, discharges, initial_bed)
    person_days = sum(daily_occupancy)
    total_discharged = sum(discharges)
    
    if total_discharged == 0:
        raise ValueError("No discharged patients in the period, cannot calculate ALOS")
    alos = person_days / total_discharged
    
    days = list(range(1, len(admissions)+1))
    plt.figure(figsize=(12, 6))
    
    bars = plt.bar(days, daily_occupancy, alpha=0.5, color='#2E86AB', 
                   edgecolor='black', linewidth=1.5, label='Daily Occupancy')
    

    plt.plot(days, daily_occupancy, marker='o', linewidth=2.5, markersize=9,
             color='#A23B72', markerfacecolor='#A23B72', markeredgecolor='white',
             markeredgewidth=2, label='Trend Line')
    

    for bar, occ in zip(bars, daily_occupancy):
        plt.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.3,
                 f'{occ}', ha='center', va='bottom', fontsize=11, fontweight='bold')
    

    plt.text(0.98, 0.95, 
             f'ALOS Calculation Result:\nTotal Person-Days: {person_days}\nTotal Discharged: {total_discharged}\nAverage Length of Stay: {alos:.2f} days',
             transform=plt.gca().transAxes, ha='right', va='top',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5),
             fontsize=11, fontweight='bold')
    
    
    plt.title('Daily Ward Occupancy & ALOS Calculation', fontsize=15, fontweight='bold', pad=15)
    plt.xlabel('Day', fontsize=13)
    plt.ylabel('Number of Patients', fontsize=13)
    plt.xticks(days)
    plt.ylim(bottom=0)
    plt.legend(loc='upper left', fontsize=11)
    plt.grid(True, alpha=0.3, linestyle='--', axis='y')
    
    plt.tight_layout()
    plt.show()
    
    # Print results
    print(f"Total Person-Days: {person_days}")
    print(f"Total Discharged Patients: {total_discharged}")
    print(f"Average Length of Stay (ALOS): {alos:.2f} days")
    
    return alos


admissions = [3, 5, 7, 6, 5, 4, 5]
discharges = [1, 2, 3, 4, 5, 3, 2]


calculate_alos(admissions, discharges)
