student_add={
    "ashish":"chanod",
    "shivam":"vapi",
    "raj":"banaras"
}
def get_add(name) :
    name=input("enter the name:").lower()
    if name in student_add :
        print(f"The student {name.title()} lives in {student_add[name]}")
    else:
        print("the student is not found")

get_add(student_add)
