"""
# ex.2
It's the end of the semester and you got your grades from three classes: Geometry, Algebra, and Physics.

Create a program that:
1) Reads the grades of these 3 classes (Grades range from 0 - 10)
2) Calculate the average of your grades

* Example: Geometry = 6, Algebra = 7, Physics = 8
* Output: average_score = 7
"""

def subjects_dict(dict1):
    sum1 = sum(dict1.values())
    average = sum1/3
    return average

geo = 6
alg = 7
phy = 8

dict2 = {"Geometry" : geo, "Algebra" : alg, "Physics" : phy}

result = subjects_dict(dict2)
print(f"Your scores are Geometry: {geo}, Algebra: {alg}, Physics: {phy}")
print("Your average score is", result)
