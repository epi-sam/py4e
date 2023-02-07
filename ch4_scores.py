score = input("Enter Score: ")
score = float(score)

# validate input
try:
    valid = (score > 0 & score < 1)
except: 
     valid = False
if not valid :
    print("Invalid input (req 0-1)")
else :
    if score >= 0.9 :
        letter_grade = "A"
    elif score >= 0.8 :
        letter_grade = "B"
    elif score >= 0.7 :
        letter_grade = "C"
    elif score >= 0.6 :
        letter_grade = "D"
    else :
        letter_grade = "F"
    print(letter_grade)