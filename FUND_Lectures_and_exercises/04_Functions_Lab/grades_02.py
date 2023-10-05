""""•	2.00 – 2.99 - "Fail"
•	3.00 – 3.49 - "Poor"
•	3.50 – 4.49 - "Good"
•	4.50 – 5.49 - "Very Good"
•	5.50 – 6.00 - "Excellent"
"""


def grade_function(score):
    if 2.00 <= score < 3.00:
        return "Fail"
    elif 3.00 <= score <= 3.49:
        return "Poor"
    elif 3.50 <= score <= 4.49:
        return "Good"
    elif 4.50 <= score <= 5.49:
        return "Very Good"
    elif 5.50<=score<=6.00:
        return "Excellent"


grade_number = float(input())
print(grade_function(grade_number))
