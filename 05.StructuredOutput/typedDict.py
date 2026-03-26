from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    courses: list[str]

person : Person = {
    "name": "Satyam Garg",
    "age": 23,
    "courses": ["Python", "JavaScript", "React"]
}  

print(person)  