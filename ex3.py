#---new code for set operations and list de-duplication

print("set operations")

#create 2 sets

set_a = {10, 20, 30, 40, 50, 50}
set_b = {40, 50, 60, 70, 80}

print(f"set A: {set_a}")
print(f"set B: {set_b}\n")

#FIND THE UNION OF 2 SETS

union_set = set_a.union(set_b)
union_set_2 = set_b.union(set_a)

print(f"union of set A & B: {union_set}")
print(f"union of set A & B: {union_set_2}\n")

#find the intersection of 2 sets

intersection_set = set_a.intersection(set_b)
print(f"intersection of set A & B: {intersection_set}\n")

#difference between 2 sets

difference_set = set_a.difference(set_b)
difference_set2 = set_b.difference(set_a)

print(f"differnce: set A - set B: {difference_set}")
print(f"differnce: set B - set A: {difference_set2}\n")

print("de-duplications using sets")

my_list = [1, 2, 2, 3, 4, 5, 6, 6, 7, 10] 
print(f"list with duplications: {my_list} \n")

#list to set to remove duplicates
unique_element_set = set(my_list)
print(f"list converterd to set without duplications: {unique_element_set}\n ")

#convert the set back to a list
back_to_list = list(unique_element_set)
print(f"set converterd back to list: {back_to_list} ")


