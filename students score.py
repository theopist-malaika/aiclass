Student_score={}

Student_score["Gift"]=76
Student_score["Peter"]=23
Student_score["Felix"]=43
Student_score["Mark"]=86
Student_score["Mishelin"]=56
Student_score["Eric"]=88
Student_score["Sana"]=49
Student_score["Samuel"]=68
Student_score["Relais"]=79
Student_score["Godfley"]=94
Student_score["Desire"]=82
Student_score["Denis"]=66

#Average score
Average = sum(Student_score.values())/len(Student_score)
print(f"Average score:{Average:.2f}")

#highest score
highest_score = max(Student_score.values())
print(f"The highest score:{highest_score}")
 

for Student, score in Student_score.items():
    if score == highest_score:
        print(f"Highest score:{Student} with {score}")

#updating
Student_score["Felix"]= 83

for Student, score in Student_score.items():
    if score > 80:
        print(f"{Student}:{score}")


