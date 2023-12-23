"""
12.	The educational course ends with a test checking the participants' knowledge. 
To pass the course, the participant must obtain a minimum number of points. Write a 
program that checks whether a participant has passed the course. Define a higher order 
function. Sample result:
"""
def min_pts(limit):
    def check(pts):
        if pts >= limit:
            return True
        return False
    return check

print("=== MIN 50 PTS TO PASS ===")
assess_test = min_pts(50)
print(f"52 pts -> {assess_test(52)}")
print(f"39 pts -> {assess_test(39)}")

print("=== MIN 60 PTS TO PASS ===")
assess_test = min_pts(60)
print(f"52 pts -> {assess_test(52)}")
print(f"39 pts -> {assess_test(39)}")