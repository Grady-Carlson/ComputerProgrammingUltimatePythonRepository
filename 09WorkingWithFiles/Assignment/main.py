import csv
f = open("../data/4000-most-common-english-words.csv", "r")
words = f.read().split("\n")
    
def Most_Vowels(wordlist):
    word_with_most_vowels = ""
    most_amount = 0 
    vowel_amount = 0
    for words in wordlist:
        for letters in words:
            if letters in "aeiou":
                vowel_amount = vowel_amount + 1
            else: pass
        if vowel_amount > most_amount:
            most_amount = vowel_amount
            word_with_most_vowels = words
            vowel_amount = 0
        else:
            vowel_amount = 0
    return word_with_most_vowels

print("4000 Most Common English Words =>", Most_Vowels(words))
print("")

def average_word_length(wordlist):
    denominator = 0
    sum = 0
    for words in wordlist:
        sum = len(words) + sum
        denominator = denominator + 1
    return sum/denominator

print("4000 Most Common English Words =>", average_word_length(words))
print("")

f = open("../data/gradebook_data.csv", "r")
reader = csv.reader(f) 
A = 0
B = 0 
C = 0
D = 0
F = 0
for row in reader:
    name, gradelevel, percent = row
    percent = int(percent)
    if percent >= 90:
        A = A + 1
    elif percent < 90 and percent >= 80:
        B = B + 1
    elif percent < 80 and percent >= 70:
        C = C + 1
    elif percent < 70 and percent >= 60:
        D = D + 1
    else:
        F = F + 1

print(A,B,C,D,F)
print("")

f = open("../data/gradebook_data.csv", "r")
reader = csv.reader(f)
freshmen = 0
soph = 0
jun = 0
sen = 0
freshdiv = 0
sophdiv = 0
jundiv = 0
sendiv = 0
for row in reader:
    name, gradelevel, percent = row
    percent = int(percent)
    grade = int(gradelevel)
    if grade == 9:
        freshmen = freshmen + percent
        freshdiv = freshdiv + 1
    elif grade == 10:
        soph = soph + percent
        sophdiv = sophdiv + 1
    elif grade == 11:
        jun = jun + percent
        jundiv = jundiv + 1
    else:
        sen = sen + percent
        sendiv = sendiv + 1
    
print(freshmen/freshdiv, soph/sophdiv, jun/jundiv, sen/sendiv)
print()

f = open("../data/gradebook_data.csv", "r")
reader = csv.reader(f)
failing_seniors = ""
for row in reader:
    name, gradelevel, percent = row
    percent = int(percent)
    grade = int(gradelevel)
    if grade == 12 and percent <60:
        failing_seniors = failing_seniors + name +" "

print(failing_seniors)