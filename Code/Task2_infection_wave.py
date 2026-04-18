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
    for i in range(1, total_days):
        increase = occupancy[i] - occupancy[i-1]
        daily_increases.append(increase)
    
    # Step 3: Find the maximum daily increase and its position
    max_increase = max(daily_increases)
    max_increase_index = daily_increases.index(max_increase)
    peak_day = max_increase_index + 2  # convert index to actual day number
    
    # Step 4: Determine if the peak has passed
    if peak_day < total_days:
        peak_status = "Peak has passed, the increase is declining"
    else:
        peak_status = "Peak not reached, cases are still rising"
    
    # Step 5: Print and return all results
    print(f"Maximum daily increase: {max_increase} patients")
    print(f"Peak increase occurs on day: {peak_day}")
    print(f"Status: {peak_status}")
    
    return max_increase, peak_day, peak_status