import random
def rand_sample(list, sample_size):
    for i in range(sample_size):
        yield list[random.randint(0, len(list) - 1)]



names = ["Jack", "Bill", "Caren", "Jemimah", "Noel", "Joy", "Dan", "Immaculate", "John"]
profiles = {
    "Jack" : {"Name": "Jacob Watua" , "Age": 24, "Role" :  "Accountant"},
    "Bill" : {"Name": "Bill Amos" , "Age": 24, "Role" :  "Advocate"} ,
    "Caren" : {"Name": "Caren Grace" , "Age": 21, "Role" :  "HealthCare"}, 
    "Jemimah" : {"Name": "Jemimah Rachael" , "Age": 27, "Role" :  "Technical Support"},
    "Noel" : {"Name": "Noeline Kavindu" , "Age": 28, "Role" :  "Human Resource Manager"},
    "Joy" :  {"Name": "Joy Chebby" , "Age": 21, "Role" :  "Intern"},
}

for i in rand_sample(names, 5):
    try:
        print(f"Name : {profiles[i]['Name']}\nAge : {profiles[i]['Age']}\nRole : {profiles[i]['Role']}", end="\n\n")
    except KeyError:
        print("{}'s Profile does not exist".format(i), end = "\n\n")
print()    