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
    
    # Print results
    print(f"Total Person-Days: {person_days}")
    print(f"Total Discharged Patients: {total_discharged}")
    print(f"Average Length of Stay (ALOS): {alos:.2f} days")
    
    return alos


admissions = [3, 5, 7, 6, 4, 3, 2]
discharges = [1, 2, 3, 4, 5, 3, 2]


calculate_alos(admissions, discharges)
