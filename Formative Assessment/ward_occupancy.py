import matplotlib.pyplot as plt

def calculate_ward_occupancy(admission, discharge):
    ward_occupancy = []
    current_occupancy = 0
    for i in range(len(admission)):
        current_occupancy += admission[i] - discharge[i]
        ward_occupancy.append(current_occupancy)
    
    plt.plot([1,2,3,4,5,6,7],ward_occupancy)
    plt.title('Ward Occupancy Over Time')
    plt.xlabel('Time')
    plt.ylabel('Number of Patients')
    plt.show()
    return ward_occupancy