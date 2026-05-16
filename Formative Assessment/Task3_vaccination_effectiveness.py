import matplotlib.pyplot as plt
import numpy as np
import Task1_ward_occupancy

def vaccination_effectiveness(admission, discharge,
                              admission_after, discharge_after,
                              threshold_percent=30):
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
    before_occ = Task1_ward_occupancy.reuse_calculate_ward_occupancy(admission, discharge)
    after_occ = Task1_ward_occupancy.calculate_ward_occupancy(admission_after, discharge_after)

    # Average daily occupancy
    avg_before = np.mean(before_occ)
    avg_after = np.mean(after_occ)

    # Percentage change
    if avg_before == 0:
        change_percent = 0 if avg_after == 0 else float('inf')
    else:
        change_percent = (avg_after - avg_before) / avg_before * 100

    # Define criteria
    if change_percent < -threshold_percent:
        result = f"Vaccine effective: Average occupancy decreased from {avg_before:.1f} to {avg_after:.1f} (change {change_percent:.1f}%)"
    elif change_percent >= -threshold_percent:
        result = f"Vaccine not effective: Average occupancy increased from {avg_before:.1f} to {avg_after:.1f} (change {change_percent:.1f}%)"

    # Visualization
    days = list(range(1, 8))

    # Line chart of daily occupancy
    plt.plot(days, before_occ, marker='o', label='Before Vaccine', 
         linewidth=2, markersize=6, color='#2E86AB')
    plt.plot(days, after_occ, marker='s', label='After Vaccine', 
         linewidth=2, markersize=6, color='#E63946')
    plt.axhline(y=avg_before, color='#2E86AB', linestyle='--', alpha=0.5, label=f'Before mean = {avg_before:.1f}')
    plt.axhline(y=avg_after, color='#E63946', linestyle='--', alpha=0.5, label=f'After mean = {avg_after:.1f}')
    plt.xlabel('Day')
    plt.ylabel('Number of Patients')
    plt.title('Daily Ward Occupancy Comparison')
    plt.legend()
    plt.grid(True, alpha=0.3)

    # Annotate percentage change on the graph
    plt.text(0.5, 0.9, f'Change: {change_percent:.1f}%',
             transform=plt.gca().transAxes, ha='center',
             horizontalalignment='left',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    plt.tight_layout()
    plt.show()

    return result

# Example data
admission = [11, 17, 28, 20, 21, 15, 14]
discharge = [2, 5, 12, 13, 30, 21, 15]

admission_after = [11, 17, 28, 20, 21, 15, 14]
dischargem_after = [4, 13, 14, 18, 22, 25, 14]

# Execute
print(vaccination_effectiveness(admission, discharge,
                                admission_after, discharge_after))