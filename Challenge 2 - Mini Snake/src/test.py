import datetime
from your_solution import f
data = [
    {"Team_name": "Team_A", "Running_time": 120123, "Accuracy": 87.5, "Submission_time": datetime.datetime(2024, 4, 23, 10, 15, 0)},
    {"Team_name": "Team_B", "Running_time": 135234, "Accuracy": 92.3, "Submission_time": datetime.datetime(2024, 4, 23, 11, 30, 0)},
    {"Team_name": "Team_C", "Running_time": 110345, "Accuracy": 84.9, "Submission_time": datetime.datetime(2024, 4, 23, 12, 45, 0)},
    {"Team_name": "Team_D", "Running_time": 125456, "Accuracy": 88.2, "Submission_time": datetime.datetime(2024, 4, 23, 13, 0, 0)},
    {"Team_name": "Team_E", "Running_time": 145567, "Accuracy": 91.7, "Submission_time": datetime.datetime(2024, 4, 23, 14, 15, 0)},
    {"Team_name": "Team_F", "Running_time": 130678, "Accuracy": 86.4, "Submission_time": datetime.datetime(2024, 4, 23, 15, 30, 0)},
    {"Team_name": "Team_G", "Running_time": 115789, "Accuracy": 89.8, "Submission_time": datetime.datetime(2024, 4, 23, 16, 45, 0)},
    {"Team_name": "Team_H", "Running_time": 140890, "Accuracy": 83.2, "Submission_time": datetime.datetime(2024, 4, 23, 17, 0, 0)},
    {"Team_name": "Team_I", "Running_time": 150901, "Accuracy": 90.1, "Submission_time": datetime.datetime(2024, 4, 23, 18, 15, 0)},
    {"Team_name": "Team_J", "Running_time": 128012, "Accuracy": 85.6, "Submission_time": datetime.datetime(2024, 4, 23, 19, 30, 0)}
]


print(f(data))
