# Challenge 2 - Mini Snake

## Overview

This challenge requires the participants to write the shortest possible Python program solving a specific task.

## Knowledge

- Python

## Files provided

- template.py: template file you should use to write your program
- test.py: useful file to test your solution

## Dependencies & Tools

- Python

## Documentation

Our chapter is running an international hackathon and your task is helping the judges to compute the final ranking of the participating teams. Your software will receive a list of dictionaries with the results.

Every team will have a measurement for the running time, accuracy and submission time of their solution, every measurement will have a different format and they will all be considered for the final ranking.

Your solution must be able to receive the data and create the ordered ranking for the competition, by assigning the correct points and sorting the dictionary.

The judges data will be formatted as follows

```python
[{"Team_name": string, "Running_time":int", Accuracy": float, "Submission_time": datetime}, {"Team_name": string, "Running_time":int,” Accuracy": float, "Submission_time": datetime}, . . .]
```

With the following variable types:

- Team name is a string
- Running time is an int representing the total milliseconds
- Accuracy is a float with only one decimal digit, representing the accuracy percentage
- Submission time is a datetime object

The aim of your code is to provide a function that can receive the data and return it ordered

At first your function will be assigning point based on the results of the teams, following the tables below, then based on the total score and the submission time your code will sort the list and return it with the correct order and scores

Below you can find the scoring criteria for each field

### Running time

The running time will be evaluated taking into account the difference between the shortest and the longest time. Then for every result the percentage difference with respect to the maximum one will be evaluated.

For example, if the shortest time is 15 milliseconds and the longest is 25 milliseconds, the maximum difference will be 10 milliseconds. So, a result of 20 milliseconds will have a difference of 5 milliseconds compared to the shortest one and will be evaluated as 50% of the maximum difference, thus receiving 4 points. Meanwhile, a result of 17 milliseconds will receive 7 points. (All percentage results are rounded down).

The running time will be evaluated using the following table

| Difference Percentage | Points |
| --------------------- | ------ |
| Top 0-5%              | 10     |
| Top 6-10%             | 9      |
| Top 11-19%            | 8      |
| Top 20-29%            | 7      |
| Top 30-39%            | 6      |
| Top 40-49%            | 5      |
| Top 50-59%            | 4      |
| Top 60-69%            | 3      |
| Top 70-79%            | 2      |
| Top 80-100%           | 1      |

### Accuracy

| Accuracy Percentage | Points |
| ------------------- | ------ |
| 90-100%             | 10     |
| 80-89.99%           | 9      |
| 70-79.99%           | 8      |
| 60-69.99%           | 7      |
| 50-59.99%           | 6      |
| 40-49.99%           | 5      |
| 30-39.99%           | 4      |
| 20-29.99%           | 3      |
| 10-19.99%           | 2      |
| 0-9.99%             | 1      |

### Example

Here's what the output should be for the test file

```python
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
```

```
[{'Team_name': 'Team_C', 'Score': 19, 'Submission_time': '23-04-24 12:45:00'},
{'Team_name': 'Team_G', 'Score': 17, 'Submission_time': '23-04-24 16:45:00'},
{'Team_name': 'Team_A', 'Score': 16, 'Submission_time': '23-04-24 10:15:00'},
{'Team_name': 'Team_D', 'Score': 15, 'Submission_time': '23-04-24 13:00:00'},
{'Team_name': 'Team_J', 'Score': 14, 'Submission_time': '23-04-24 19:30:00'},
{'Team_name': 'Team_B', 'Score': 13, 'Submission_time': '23-04-24 11:30:00'},
{'Team_name': 'Team_F', 'Score': 13, 'Submission_time': '23-04-24 15:30:00'},
{'Team_name': 'Team_E', 'Score': 11, 'Submission_time': '23-04-24 14:15:00'},
{'Team_name': 'Team_H', 'Score': 11, 'Submission_time': '23-04-24 17:00:00'},
{'Team_name': 'Team_I', 'Score': 11, 'Submission_time': '23-04-24 18:15:00'}]
```

## Evaluation Criteria

The submission time will not award any points; it will only be considered in the event of ties. The team with the earlier submission will be ranked above the others.

**Important Remark**: your program will be tested considering a wide range of possibilities: do not base you solution only on the example. Programs not passing 100% of tests will be penalized.

### RULES

- You cannot change the structure of the dictionary (both the input one and the output one)
- Your code should work offline
- You cannot use any python module that is not already included in python 3.10
- The test case D=[] should not be taken into account

## Submission

To complete the challenge, use [this form]() to submit a `.py` file containing your solution.

```

```
