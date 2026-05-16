import matplotlib.pyplot as plt
import numpy as np
import Task1_ward_occupancy


def calculate_alos(admission, discharge):
    daily_occupancy = Task1_ward_occupancy.reuse_calculate_ward_occupancy(admission, discharge)
    person_days = sum(daily_occupancy)
    total_discharged = sum(discharge)
    
    if total_discharged == 0:
        raise ValueError("No discharged patients in the period, cannot calculate ALOS")
    alos = person_days / total_discharged
    
    days = list(range(1, len(admission)+1))
    
    # Print results
    print(f"Total Person-Days: {person_days}")
    print(f"Total Discharged Patients: {total_discharged}")
    print(f"Average Length of Stay (ALOS): {alos:.2f} days")
    
    return alos


admission = [11, 17, 28, 20, 21, 15, 14]
discharge = [2, 5, 12, 13, 30, 21, 15]


calculate_alos(admission, discharge)
