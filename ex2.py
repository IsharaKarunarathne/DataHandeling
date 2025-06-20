#create dictionary named students scores where keys are student names and values are their scores (integeres)
student_scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95,
    "Eve":88,
    "Frank": 70
}

print("_initial student scores_")

for name, score in student_scores.items():
    print(f"{name}: {score}")
print("\n")


#adding a new student to the list
new_student_name = "Grace"
new_student_score = 90
student_scores[new_student_name] = new_student_score
print(f"added new student: {new_student_name} with score of {new_student_score}")

for name, score in student_scores.items():
       print(f"{name}: {score}")
print("\n")

#update the score for an existing student

student_scores["Alice"] = 60
print(f"upated marks for one student")

for name, score in student_scores.items():
       print(f"{name}: {score}")
print("\n")

#find the highest mark

if student_scores: #ensure dictionary is not empty
      highest_score = 0
      highest_scorer_name = ""
      for name, score in student_scores.items():
            if score > highest_score:
                  highest_score = score
                  highest_scorer_name = name
      print("highest score")
      print(f"{highest_scorer_name}: {highest_score}\n")
else:
      print("the dictionary is empty, can not find the highest score.\n")


