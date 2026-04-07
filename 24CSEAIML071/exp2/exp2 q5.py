#creating a dictionary
student = {

    "name": "amit kumar sahu",
    "age": 18,
    "course": "B-TECH",
    "city": "odisha gopalpur"
}

#display the entire dictionary
print("dictionary data:")
print(student)

#display keys and values separately
print("\n values in dictionary:")
print(student.values())
 
print("\n keys in dictionary")
print(student.keys())

#display key value pairs using loops
print("\n key value pairs")
for key, value in student.items():
    print(key, ":" , value)
