def make_abc():
    return ["a","b","c"]

print("")
print("Make ABC:")
print(make_abc())
print("")

def equal_edges(list):
    if list[0] == list[-1]:
        return True
    else:
        return False

print("Equal Edges:")   
print("[1, 2, 3, 4, 1] =>", equal_edges([1, 2, 3, 4, 1]))
print("[5, 6, 7, 8, 9] =>", equal_edges([5, 6, 7, 8, 9]))
print("[4,4] =>", equal_edges([4,4]))
print("")

def common_edge(list1, list2):
    if list1[0] == list2[0] or list1[0] == list2[-1] or list1[-1] == list2[0] or list1[-1] == list2[-1]:
        return True
    else:
        return False
    
print("Common Edge:")
print("[1,2,3,4,5] and [2,2,3,4,1] =>", common_edge([1,2,3,4,5],[2,2,3,4,1]))
print("[1,9,5,0,1] and [-1,0,2,3,4] =>", common_edge([1,9,5,0,1],[-1,0,2,3,4]))
print("[1,3,6] and [6,2,9] =>", common_edge([1,3,6],[6,2,9]))
print("")

def all_the_same(item):
    if item[0] == item[1] and item[2] == item[1]:
        return True
    else:
        return False
    
print("All the Same:")
print("[1,2,3] =>", all_the_same([1,2,3]))
print("[5,5,5] =>", all_the_same([5,5,5]))
print("[9,9,6] =>", all_the_same([9,9,6]))
print("")

def all_unique(item):
    if item[0] == item[1] or item[2] == item[1] or item[2] == item[0]:
        return False
    else:
        return True

print("All Unique:")
print("[1,2,3] =>", all_unique([1,2,3]))
print("[5,5,5] =>", all_unique([5,5,5]))
print("[9,9,6] =>", all_unique([9,9,6]))
print("")

def increasing(list):
    if list[1] > list[0] and list [2] > list[1]:
        return True
    else:
        return False
    
print("Increasing:")
print("[1,2,3] =>", increasing([1,2,3]))
print("[5,5,5] =>", increasing([5,5,5]))
print("[-1,0,1] =>", increasing([-1,0,1]))
print("")

def all_true(list):
    if list[0] == True and list[1] == True and list[2] == True:
        return True
    else:
        return False
    
print("All True:")
print("[True,True,True] =>", all_true([True,True,True]))
print("[False,True,True] =>", all_true([False,True,True]))
print("[True,False,False] =>", all_true([True,False,False]))
print("")

def mostly_true(list):
    if list[0] == True and list[1] == True or list[0] == True and list[1] == True and list[2] == True or list[1] == True and list[2] == True or list[0] == True and list[2] == True:
        return True
    else:
        return False

print("Mostly True:")
print("[True,True,True] =>", mostly_true([True,True,True]))
print("[False,True,True] =>", mostly_true([False,True,True]))
print("[True,False,False] =>", mostly_true([True,False,False]))
print("")

def make_copy(list):
    return list

print("Make Copy: ")
print("[1,2,3] =>", make_copy([1,2,3]))
print("[5,4,3] =>", make_copy([5,4,3]))
print("[2,4,6] =>", make_copy([2,4,6]))
print("")

def repeat_thrice(list):
    num1 = list
    num2 = list
    num3 = list
    return [num1,num2,num3]

print("Repeat Thrice")
print("-1 =>", repeat_thrice(-1))
print("5 =>", repeat_thrice(5))
print("")

def make_reversed_copy(list):
    a = list[0]  
    b = list[1] 
    c = list[2]
    return [c,b,a]

print("Make Reversed Copy:")
print("[1,2,3] =>", make_reversed_copy([1,2,3]))
print("[13,5,6] =>", make_reversed_copy([13,5,6]))
print("")

def reverse_in_place(list):
    a = list[0]  
    b = list[1] 
    c = list[2]
    list[0] = c
    list[1] = b
    list[2] = a
    return (list)

print("Reverse in Place:")
print("[1,2,3] =>", reverse_in_place([1,2,3]))
print("[5,4,3] =>", reverse_in_place([5,4,3]))
print("[2,4,6] =>", reverse_in_place([2,4,6]))
print("")

