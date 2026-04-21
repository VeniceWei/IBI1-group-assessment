import matplotlib.pyplot as plt
def calculate_ward_occupancy(admission, discharge):
    """Task 1: Calculate daily ward occupancy"""
    occupancy = []
    current = 0
    for i in range(len(admission)):
        current += admission[i] - discharge[i]
        occupancy.append(current)
    return occupancy

def hospital_management(daily_patients, max_ward_capacity=30):

    total_days = len(daily_patients)
    days = list(range(1, total_days + 1))
    breach_days = []          # The days when the number of patients exceeded the ward capacity
    exceeded_patients = []    # The number of patients that exceeded the capacity on those breach days

    for day in range(total_days):
        if daily_patients[day] > max_ward_capacity:
            breach_days.append(day + 1)  
            exceeded = daily_patients[day] - max_ward_capacity
            exceeded_patients.append(exceeded)

    # The number of days when the ward capacity was breached
    num_breach_days = len(breach_days)
    # The proportion of breach days to total days
    breach_proportion = num_breach_days / total_days

    # The average number of extra wards needed during breach days
    extra_wards_avg = 0.0
    if num_breach_days > 0:
        # The total number of patients that exceeded the capacity across all breach days
        total_exceeded = sum(exceeded_patients)
        extra_wards_avg = total_exceeded / max_ward_capacity / num_breach_days

    # Visualization
    plt.figure(figsize=(10, 6))
    
    # Color bars: red for breach days, blue for normal days
    colors = ['#E63946' if count > max_ward_capacity else '#2E86AB' for count in daily_patients]
    bars = plt.bar(days, daily_patients, color=colors, edgecolor='black', linewidth=1.5, alpha=0.8)
    
    # Add capacity line
    plt.axhline(y=max_ward_capacity, color='red', linestyle='--', linewidth=2.5,
                label=f'Max Capacity = {max_ward_capacity} patients')
    
    # Add value labels
    for bar, val in zip(bars, daily_patients):
        plt.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.5,
                 f'{val}', ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    plt.title('Hospital Ward Occupancy Report', fontsize=14, fontweight='bold')
    plt.xlabel('Day', fontsize=12)
    plt.ylabel('Number of Patients', fontsize=12)
    plt.xticks(days)
    plt.legend(loc='upper left')
    plt.grid(True, alpha=0.3, axis='y')
    
    # Add annotation
    plt.text(0.98, 0.95, f'Breach Proportion: {breach_proportion:.1%}\nExtra Wards Needed: {extra_wards_avg:.2f}',
             transform=plt.gca().transAxes, ha='right', va='top',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5),
             fontsize=10)
    
    plt.tight_layout()
    plt.show()

    print(f"The max ward capacity: {max_ward_capacity} patients")
    print(f"Total days: {total_days} Days")
    print(f"The breach days{num_breach_days} Days")
    print(f"The breach proportion: {breach_proportion:.2%}")
    print(f"The average of extra wards: {extra_wards_avg:.2f}")

    return {
        "total_days": total_days,
        "breach_days_count": num_breach_days,
        "breach_proportion": breach_proportion,
        "average_extra_wards_needed": extra_wards_avg
    }


admissions = [32, 31, 29,33, 28, 30, 32]
discharges = [0, 28, 30, 31, 27, 32, 29]
occupancy = calculate_ward_occupancy(admissions, discharges)
hospital_management(occupancy)
