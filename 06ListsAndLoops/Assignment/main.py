def count_failing_grades(scores):
    failing = 0
    for score in scores:
        if score < 60:
            failing = failing + 1
    return failing

print("Students Failing: ")
print("[30, 50, 99, 84, 22, 100] =>", count_failing_grades([30,50,99,84,22,100]))
print("")

def count_act_scores(scores):
    valid = 0 
    for score in scores:
        if 0 < score <= 36:
            valid = valid + 1
    return valid

print("Valid ACT Scores:")
print("[4, 36, 55, 100, 12] =>", count_act_scores([4, 36, 55, 100, 12]))      
print("")

def number_sum(numbers):
    sum = 0
    for number in numbers:
        sum = sum + number
    return sum

print("Number Sum: ")
print("[4, 36, 55, 100, 12] =>", number_sum([4, 36, 55, 100, 12])) 
print("")

def average_act_score(scores):
    numberOfScores = 0
    sum = 0
    for score in scores:
        numberOfScores = numberOfScores + 1
        sum = sum + score
    return sum/numberOfScores

print("Average ACT Scores:")
print("[12, 36, 32, 24, 15] =>", average_act_score([12, 36, 32, 24, 15]))
print("")