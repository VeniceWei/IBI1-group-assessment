import matplotlib.pyplot as plt
def calculate_ward_occupancy(admission, discharge):
    """Task 1: Calculate daily ward occupancy"""
    occupancy = []
    current = 0
    for i in range(len(admission)):
        current += admission[i] - discharge[i]
        occupancy.append(current)
    return occupancy

def find_infection_peak(admission, discharge):
    """
    Task 2: Find the peak infection day and determine if the peak has passed
    Input: 7-day admission list and 7-day discharge list
    Output: max increase day, peak status
    """
    # Step 1: Get daily occupancy from Task 1 function
    occupancy = calculate_ward_occupancy(admission, discharge)
    
    # Step 2: Calculate daily increase in patients (change from previous day)
    daily_increases = []
    total_days = len(occupancy)
    # Day 1 increase (starting from 0)
    daily_increases.append(occupancy[0])
    for i in range(1, total_days):
        increase = occupancy[i] - occupancy[i-1]
        daily_increases.append(increase)
    
    # Step 3: Find the maximum daily increase and its position
    max_increase = max(daily_increases)
    max_increase_index = daily_increases.index(max_increase)
    peak_day = max_increase_index + 1  # convert index to actual day number
   
     # Step 4: Determine if the peak has passed
    if peak_day < total_days:
        peak_status = "Peak has passed, the increase is declining"
    else:
        peak_status = "Peak not reached, cases are still rising"
    
    # Step5: generate plots
    days = list(range(1, 8))
    plt.figure(figsize=(10, 6))
    # Color bars: highlight the peak increase in red
    bar_colors = ['#E63946' if i == max_increase else '#2E86AB' for i in daily_increases]
    bars = plt.bar(days, daily_increases, color=bar_colors, edgecolor='black', linewidth=1.5, alpha=0.8)
    
    # Add value labels on bars
    for bar, val in zip(bars, daily_increases):
        y_offset = 0.02 if val >= 0 else -0.02
        va = 'bottom' if val >= 0 else 'top'
        plt.text(bar.get_x() + bar.get_width()/2., bar.get_height() + y_offset,
                 f'{val:+d}', ha='center', va=va, fontsize=12, fontweight='bold')
    # Add zero line
    plt.axhline(y=0, color='black', linestyle='-', linewidth=1)
    # Annotate peak
    plt.annotate(f'Peak: +{max_increase} patients\nreached on Day {peak_day}',
                 xy=(peak_day, max_increase),
                 xytext=(peak_day + 0.5, max_increase - 0.5),
                 arrowprops=dict(arrowstyle='->', color='red', lw=1.5),
                 fontsize=11, color='red', fontweight='bold',
                 bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.3))
    # Customize chart
    plt.title('Daily Increase in Ward Patients\n(Occupancy[i] - Occupancy[i-1])', fontsize=14, fontweight='bold')
    plt.xlabel('Day', fontsize=12)
    plt.ylabel('Increase in Number of Patients', fontsize=12)
    plt.xticks(list(range(1, 8)))
    plt.grid(True, alpha=0.3, axis='y')
    # Add status text on chart
    color = 'green' if peak_day < total_days else 'orange'
    plt.text(0.98, 0.95, f'Status: {"Peak Passed" if peak_day < total_days else "Peak Not Reached"}',
             transform=plt.gca().transAxes, ha='right', va='top',
             bbox=dict(boxstyle='round', facecolor=color, alpha=0.2),
             fontsize=11, fontweight='bold')
    plt.tight_layout()
    plt.show()

    
    # Step 6: Print and return all results
    print(f"Maximum daily increase: {max_increase} patients")
    print(f"Peak increase occurs on day: {peak_day}")
    print(f"Status: {peak_status}")
    
    return max_increase, peak_day, peak_status

# testing
admissions = [3, 5, 7, 6, 4, 3, 2]
discharges = [1, 2, 3, 4, 5, 3, 2]
find_infection_peak(admissions, discharges)