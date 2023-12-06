def is_alliteration(word1, word2):
    if word1[0] == word2[0]:
        return True
    else:
        return False

print("Is Alliteration: ")
print("Also Apple =>", is_alliteration("Also", "Apple"))
print("Not Apple =>", is_alliteration("Not", "Apple"))
print("")

def count_vowels(word):
    vowels = 0
    for letters in word:
        if letters in "aeiou":
            vowels = vowels + 1
        else:
            pass
    return vowels

print("Count Vowels:")
print("uhfuhdjdsjsaueodjsahwsidlds =>", count_vowels("uhfuhdjdsjsaueodjsahwsidlds"))
print("")

def count_numbers(word):
    numbers = 0
    for letters in word:
        if letters in "1234567890":
            numbers = numbers + 1
        else:
            pass
    return numbers

print("Count Numbers:")
print("he6t376rhfr73iurj =>", count_numbers("he6t376rhfr73iurj"))
print("")

def count_target_letters(word, number):
    numberAmount = 0
    for letters in word:
        if letters == number:
            numberAmount = numberAmount + 1
        else:
            pass
    return numberAmount

print("Count Target Letters:")
print("A's in Grady Carlson =>", count_target_letters("Grady Carlson", "a"))
print("")

def in_alphabetical_order(word):
    order = True
    first = "a"
    for letters in word:
        if letters < first:
            order = False
        else:
            first = letters
    return order

print("In Alphabetical Order:")
print("abcd =>", in_alphabetical_order("abcd"))
print("dtbgtjfhy =>", in_alphabetical_order("dtbgtjfhy"))
print("")

def alternate_case(word):
    upper = True
    result = ""
    for letter in word:
        if upper == False:
            result = result + letter.lower()
            upper = True
        else:
            result = result + letter.upper()
            upper = False
    return result

print("Alternating Case:")
print("grady carlson =>", alternate_case("grady carlson"))
print("")

def remove_vowels(word):
    result = ""
    for letter in word:
        if letter in "aeiou":
            pass
        else:
            result = result + letter
    return result

print("Remove Vowels:")
print("Grady Carlson =>", remove_vowels("Grady Carlson"))
print("")

def to_camel_case(phrase):
    upp = False
    result = ""
    for word in phrase:
        if word == " ":
            upp = True
        elif upp == True:
            result = result + word.upper()
            upp = False
        else:
            result = result + word
    return result

print("To Camel Case:")
print("Grady Carlson is cool =>", to_camel_case("Grady Carlson is cool"))
print("")

def to_snake_case(phrase):
    result = ""
    for word in phrase:
        if word == " ":
            result = result + "_"
        else:
            result = result + word
    return result

print("To Snake Case:")
print("Grady Carlson is cool =>", to_snake_case("Grady Carlson is cool"))
print("")

def without_duplicates(numbers):
    same = ""
    result = []
    for number in numbers:
        if number == same:
            pass
        else:
            result.append(number)
            same = number
    return result

print("Without Duplicates:")
print("122345677778899 =>", without_duplicates([1,2,2,3,4,5,6,7,7,7,7,8,8,9,9]))
print("")

def filter_valid_act_scores(scores):
    result = []
    for score in scores:
        if 0<score<37:
            result.append(score)
        else:
            pass
    return result

print("Filter Valid ACT Scores:")
print("13,0,39,36,42,24,32,54", filter_valid_act_scores([13,0,39,36,42,24,32,54]))
print("")