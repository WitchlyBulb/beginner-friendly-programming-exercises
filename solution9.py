"""
ex.9
The exercise is almost identical to a previous exercise with a minor change. It's the end of the semester and you got your marks from, Geometry, Algebra,
 Physics classes. If the average score is 7 and above print "Good job!", if the average score is between 6 and 4 print "You need to work harder!",
   if the average score is below 4 print "Failed, you really need to work harder!".

Create a program that:
* Reads the values of these 3 lessons
* Calculate the average of your grades
* Example: Geometry = 6, Algebra = 7, Physics = 8
* Output: Your average score is 7, Good job!"
"""

def subjects_scores(geometry, algebra, physics):
    sum1 = geometry + algebra + physics
    average = sum1/3
    return average

geo = 6
alg = 2
phy = 3

avg_score = subjects_scores(geo, alg, phy)

if avg_score >= 7:
    print("Good job!")
elif 6 >= avg_score >= 4:
    print("You need to work harder!")
else:
    print("Failed, you really need to work harder!")
