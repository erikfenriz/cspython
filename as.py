people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest_age = 9999
youngest_name = ""
for person_line in people:
    parts = person_line.split()
    name = parts[0]
    age = int(parts[1])


    if age < youngest_age:
        youngest_age = age
        youngest_name = name

# Outside of the loop, so we are all done now
print(f"The youngest person is: {youngest_name} with an age of {youngest_age}")