from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    student_name: str
    # Default value is assigned to the variable
    student_age: int = 23
    # Optional is used to make the field optional
    student_city: Optional[str] = None

    student_email: EmailStr
    # gt = greater than, lt = less than
    student_cgpa : float = Field(gt=0, lt=10)

    # pattern is used to validate the phone number
    student_phone: str = Field(description="Enter the 10 digit phone number", pattern=r"^[0-9]{10}$")

new_student = {"student_name": "Satyam", "student_email": "satyam@gmail.com", "student_cgpa": 5, "student_phone": '1234567890'}
# ** is used to unpack the dictionary
# * is used to unpack the list


# Object of the class
student = Student(**new_student)


#Convert it to Dictionary
stu_dict = student.model_dump()
print("Dictionary",stu_dict)

stu_json = student.model_dump_json()
print("JSON",stu_json)

print("Object",student)

    

