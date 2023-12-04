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
        if 0<score<=36:
             numberOfScores = numberOfScores + 1
             sum = sum + score
    if numberOfScores == 0:
        return None
    return sum/numberOfScores

print("Average ACT Scores:")
print("[12, 36, 32, 24, 15] =>", average_act_score([12, 36, 32, 24, 15]))
print("")

def all_true(words):
    falses = 0
    for word in words:
        if word == False:
            falses = falses + 1
        else: 
            falses = falses + 0
    if falses > 0:
         return False
    else:
         return True
           
print("All True:")
print("[True,False,False] =>", all_true([True,False,False]))
print("[True,True,True] =>", all_true([True,True,True]))
print("[False,True,True] =>", all_true([False,True,True]))

print("")

def any_true(words):
    trues = 0
    for word in words:
        if word == True:
            trues = trues + 1
    if trues > 0:
        return True
    else:
        return False
    
print("Any True:")
print("[False, False, False, True] =>", any_true([False, False, False, True]))
print("[False, False, False, False] =>", any_true([False, False, False, False]))
print("")

def mostly_true(words):
    trues = 0
    falses = 0
    for word in words:
        if word == True:
            trues = trues + 1
        else:
            falses = falses + 1
    if trues > falses:
        return True
    else:
        return False
    
print("Mostly True:")
print("[True,False,False] =>", mostly_true([True,False,False]))
print("[True,True,True] =>", mostly_true([True,True,True]))
print("[False,True,True] =>", mostly_true([False,True,True]))
print("")

def has_vowel(letters):
    vowels = 0
    for letter in letters:
        if letter in ["a","e","i","o","u"]:
            vowels = vowels + 1
        else:
            vowels = vowels + 0
    if vowels > 0:
        return True
    else:
        return False

print("Has Vowels:")
print("[g,r,a,d,y] =>", has_vowel(["g","r","a","d","y"]))    
print("[g,r,n,d,y] =>", has_vowel(["g","r","n","d","y"])) 
print("")