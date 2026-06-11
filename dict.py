stud={
    101 : {"name": "ram", "age":18, "sub":("python","java","mern"), "marks":[30,89,78]}, 
    102 : {"name": "sita", "age":19, "sub":("python","java","mern"), "marks":[70,80,90]},
    103 : {"name": "rahul", "age":20, "sub":("python","java","mern"), "marks":[58,79,90]},
    104 : {"name": "gita", "age":21, "sub":("python","java","mern"), "marks":[88,97,100]}   
}

print("1. Total Marks")
for roll, data in stud.items():
    total = sum(data["marks"])
    print(f"Roll No: {roll}, Name: {data['name']}, Total Marks: {total}")

topper_roll = max(stud, key=lambda x: sum(stud[x]["marks"]))
topper = stud[topper_roll]
print("\n2. Topper")
print(f"Roll No: {topper_roll}")
print(f"Name: {topper['name']}")
print(f"Total Marks: {sum(topper['marks'])}")
python_topper_roll = max(stud, key=lambda x: stud[x]["marks"][0])

print("\n3. Highest Marks in Python")
print(f"Roll No: {python_topper_roll}")
print(stud[python_topper_roll])

print("\n4. Students with age > 19")
for roll, data in stud.items():
    if data["age"] > 19:
        print(f"Name: {data['name']}, Age: {data['age']}")


print("\n5. Students with mern marks between 70 and 90")
for roll, data in stud.items():
    mern_marks = data["marks"][2]
    if 70 < mern_marks < 90:
        print(f"Roll No: {roll}, Details: {data}")

