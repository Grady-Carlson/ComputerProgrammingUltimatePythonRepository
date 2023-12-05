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