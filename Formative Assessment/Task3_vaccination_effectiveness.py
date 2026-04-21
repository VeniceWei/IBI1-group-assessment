import matplotlib.pyplot as plt
import numpy as np

def calculate_daily_occupancy(admissions, discharges):
    """
    Task1
    """
    occupancy = []
    current = 0
    for i in range(len(admissions)):
        current += admissions[i] - discharges[i]
        occupancy.append(current)
    return occupancy

def vaccination_effectiveness(admissions, discharges,
                              admissions_after, discharges_after,
                              threshold_percent=5):
    """
    Evaluate whether the vaccine is effective.

    Criteria (based on average daily occupancy):
    - Reduction >= threshold_percent% → Effective
    - Change between -threshold_percent% and +threshold_percent% → Inconclusive
    - Increase >= threshold_percent% → Not effective

    Parameters:
        admissions_before, discharges_before: 7-day data before vaccine
        admissions_after, discharges_after: 7-day data after vaccine
        threshold_percent: Threshold for effectiveness (default 5%)

    Returns:
        Result string and displays comparison graphs
    """
    # Calculate daily occupancy
    before_occ = calculate_daily_occupancy(admissions, discharges)
    after_occ = calculate_daily_occupancy(admissions_after, discharges_after)

    # Average daily occupancy
    avg_before = np.mean(before_occ)
    avg_after = np.mean(after_occ)

    # Percentage change
    if avg_before == 0:
        change_percent = 0 if avg_after == 0 else float('inf')
    else:
        change_percent = (avg_after - avg_before) / avg_before * 100

    # Define criteria
    if change_percent <= -threshold_percent:
        result = f"Vaccine effective: Average occupancy decreased from {avg_before:.1f} to {avg_after:.1f} (change {change_percent:.1f}%)"
    elif change_percent >= threshold_percent:
        result = f"Vaccine not effective: Average occupancy increased from {avg_before:.1f} to {avg_after:.1f} (change {change_percent:.1f}%)"
    else:
        result = f"Inconclusive: Minimal change from {avg_before:.1f} to {avg_after:.1f} (change {change_percent:.1f}%)"

    # Visualization
    days = list(range(1, 8))
    plt.figure(figsize=(12, 5))

    # Subplot 1: Line chart of daily occupancy
    plt.subplot(1, 2, 1)
    plt.plot(days, before_occ, marker='o', label='Before Vaccine', linewidth=2, markersize=6)
    plt.plot(days, after_occ, marker='s', label='After Vaccine', linewidth=2, markersize=6)
    plt.axhline(y=avg_before, color='blue', linestyle='--', alpha=0.5, label=f'Before mean = {avg_before:.1f}')
    plt.axhline(y=avg_after, color='orange', linestyle='--', alpha=0.5, label=f'After mean = {avg_after:.1f}')
    plt.xlabel('Day')
    plt.ylabel('Number of Patients')
    plt.title('Daily Ward Occupancy Comparison')
    plt.legend()
    plt.grid(True, alpha=0.3)

    # Subplot 2: Bar chart of average occupancy
    plt.subplot(1, 2, 2)
    bars = plt.bar(['Before Vaccine', 'After Vaccine'], [avg_before, avg_after], color=['#1f77b4', '#ff7f0e'])
    plt.ylabel('Average Number of Patients')
    plt.title('Average Occupancy Comparison')
    # Display values on top of bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                 f'{height:.1f}', ha='center', va='bottom')

    # Annotate percentage change on the graph
    plt.text(0.5, 0.9, f'Change: {change_percent:.1f}%',
             transform=plt.gca().transAxes, ha='center',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    plt.tight_layout()
    plt.show()

    return result

# Example data
admissions = [3, 5, 7, 6, 4, 3, 2]
discharges = [1, 2, 3, 4, 5, 3, 2]

admissions_after = [2, 3, 4, 5, 3, 2, 1]
discharges_after = [1, 2, 3, 4, 4, 2, 1]

# Execute
print(vaccination_effectiveness(admissions, discharges,
                                admissions_after, discharges_after))