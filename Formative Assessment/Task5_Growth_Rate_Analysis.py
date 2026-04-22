import matplotlib.pyplot as plt

def calculate_ward_occupancy(admission, discharge):
    ward_occupancy = []
    current_occupancy = 0
    for i in range(len(admission)):
        current_occupancy += admission[i] - discharge[i]
        ward_occupancy.append(current_occupancy)
    return ward_occupancy

def calculate_growth_rates(data):
    growth_rates = []
    for i in range(1, len(data)):
        prev = data[i-1]
        curr = data[i]
        if prev == 0:
            # Handle edge case: previous day had 0 patients
            if curr == 0:
                # No change
                rate = 0.0
            else:
                # New cases starting from 0, treat as 100% growth
                rate = 100.0
        else:
            rate = (curr - prev) / prev * 100
        growth_rates.append(round(rate, 2))  # Round to 2 decimal places for readability
    return growth_rates

def growth_rate_analysis(admissions, discharges):
    # 1. Calculate basic data
    occupancy = calculate_ward_occupancy(admissions, discharges)
    
    # 2. Calculate three types of growth rates
    adm_growth = calculate_growth_rates(admissions)
    dis_growth = calculate_growth_rates(discharges)
    occ_growth = calculate_growth_rates(occupancy)
    
    # 3. Analyze trends
    # Epidemic trend (based on occupancy growth)
    last_occ = occ_growth[-1]
    if last_occ > 0:
        if len(occ_growth) >= 2 and last_occ > occ_growth[-2]:
            epidemic_trend = "Epidemic is accelerating: inpatient count is growing faster."
        else:
            epidemic_trend = "Epidemic growth is slowing: the peak may be approaching."
    else:
        epidemic_trend = "Epidemic is declining: inpatient count is decreasing."
    
    # Infection status (based on admission growth)
    last_adm = adm_growth[-1]
    if last_adm > 0:
        infection_trend = "Infection situation is worsening: new admissions are increasing."
    else:
        infection_trend = "Infection situation is improving: new admissions are decreasing."
    
    # Recovery status (based on discharge growth)
    last_dis = dis_growth[-1]
    if last_dis > 0:
        recovery_trend = "Recovery situation is improving: discharges are increasing, more patients are recovering."
    else:
        recovery_trend = "Recovery situation is slowing: discharges are decreasing, fewer patients are recovering."
    
    # 4. Print results
    print("Daily Growth Rate Analysis Results")
    days_growth = list(range(2, 8))  # Growth rates are for Day 2 to Day 7
    print(f"\nAdmission Growth Rates (%) (Day 2-7): {adm_growth}")
    print(f"Discharge Growth Rates (%) (Day 2-7): {dis_growth}")
    print(f"Occupancy Growth Rates (%) (Day 2-7): {occ_growth}")
    
    print("\nTrend Analysis")
    print(f"1. Epidemic Trend: {epidemic_trend}")
    print(f"2. Infection Status: {infection_trend}")
    print(f"3. Recovery Status: {recovery_trend}")
    
    # 5. Visualization
    plt.figure(figsize=(10, 6))
    
    # Plot the three growth rate lines
    plt.plot(days_growth, adm_growth, marker='o', linewidth=2.5, markersize=8,
             color='#2E86AB', label='Admission Growth Rate', markeredgecolor='white')
    plt.plot(days_growth, dis_growth, marker='s', linewidth=2.5, markersize=8,
             color='#A23B72', label='Discharge Growth Rate', markeredgecolor='white')
    plt.plot(days_growth, occ_growth, marker='^', linewidth=2.5, markersize=8,
             color='#F18F01', label='Occupancy Growth Rate', markeredgecolor='white')
    
    # Add zero line (reference for growth/decline)
    plt.axhline(y=0, color='black', linestyle='-', linewidth=1.5, alpha=0.7, label='Zero Growth Line')
    
    # Customize the plot
    plt.title('Daily Growth Rate Analysis\n(Epidemic, Infection & Recovery Trends)', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Day', fontsize=12)
    plt.ylabel('Growth Rate (%)', fontsize=12)
    plt.xticks(days_growth)
    plt.grid(True, alpha=0.3, linestyle='--', axis='y')
    plt.legend(loc='best', fontsize=11)
    
    # Add latest status annotation
    status_text = (f"Latest Occupancy Growth: {last_occ:.1f}%\n"
                   f"Latest Admission Growth: {last_adm:.1f}%\n"
                   f"Latest Discharge Growth: {last_dis:.1f}%")
    plt.text(0.98, 0.95, status_text,
             transform=plt.gca().transAxes, ha='right', va='top',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5),
             fontsize=10)
    
    plt.tight_layout()
    plt.show()
    
    # Return results for further use if needed
    return {
        "admission_growth": adm_growth,
        "discharge_growth": dis_growth,
        "occupancy_growth": occ_growth,
        "epidemic_trend": epidemic_trend,
        "infection_trend": infection_trend,
        "recovery_trend": recovery_trend
    }

# Example test run
if __name__ == "__main__":
    # Sample 7-day data
    test_admissions = [3, 5, 7, 6, 4, 3, 2]
    test_discharges = [1, 2, 3, 4, 5, 3, 2]
    growth_rate_analysis(test_admissions, test_discharges)
