import matplotlib.pyplot as plt

def estimate_treatment_cycle(admissions, discharges):

    # Find peak positions and values for admissions
    admission_peak_count = max(admissions)
    admission_peak_idx = admissions.index(admission_peak_count)
    admission_peak_day = admission_peak_idx + 1 
    
    # Find peak positions and values for discharges
    discharge_peak_count = max(discharges)
    discharge_peak_idx = discharges.index(discharge_peak_count)
    discharge_peak_day = discharge_peak_idx + 1 
    
    treatment_cycle = discharge_peak_day - admission_peak_day
    days = list(range(1, 8))
    
    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(days, admissions, marker='o', linewidth=2, markersize=8,
             label='Daily Admissions', color='#2E86AB')
    plt.plot(days, discharges, marker='s', linewidth=2, markersize=8,
             label='Daily Discharges', color='#A23B72')
    plt.annotate(f'Admission Peak: {admission_peak_count}',
                 xy=(admission_peak_day, admission_peak_count),
                 xytext=(admission_peak_day + 0.5, admission_peak_count + 0.5),
                 arrowprops=dict(arrowstyle='->', color='#2E86AB', lw=1.5),
                 fontsize=11, color='#2E86AB', fontweight='bold')
    plt.annotate(f'Discharge Peak: {discharge_peak_count}',
                 xy=(discharge_peak_day, discharge_peak_count),
                 xytext=(discharge_peak_day - 1.5, discharge_peak_count + 0.5),
                 arrowprops=dict(arrowstyle='->', color='#A23B72', lw=1.5),
                 fontsize=11, color='#A23B72', fontweight='bold')
    plt.title('Daily Admissions & Discharges\nEstimating Average Treatment Cycle', 
              fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Day', fontsize=12)
    plt.ylabel('Number of Patients', fontsize=12)
    plt.xticks(days)
    plt.ylim(bottom=0)
    plt.legend(loc='upper right', fontsize=11)
    plt.grid(True, alpha=0.3, linestyle='--', axis='y')
    plt.text(0.98, 0.95, f'Estimated Treatment Cycle: {treatment_cycle} days',
             transform=plt.gca().transAxes, ha='right', va='top',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5),
             fontsize=11, fontweight='bold')
    plt.tight_layout()
    plt.show()
    
    # Print the results
    print(f"Admission peak: {admission_peak_count} patients on day {admission_peak_day}")
    print(f"Discharge peak: {discharge_peak_count} patients on day {discharge_peak_day}")
    print(f"Estimated average treatment cycle: {treatment_cycle} days")
    
    return admission_peak_day, discharge_peak_day, treatment_cycle

# Example test data
admissions = [3, 8, 6, 6, 4, 6, 2]
discharges = [1, 2, 3, 4, 5, 3, 2]

# Execute the function
estimate_treatment_cycle(admissions, discharges)
