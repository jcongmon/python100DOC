import random


def find_idx(names, used_names):
    idx = random.randint(0, len(names) - 1)
    while names[idx] in used_names:
        idx = random.randint(0, len(names) - 1)
    return idx


def compare_ans(result, names, db, idx1, idx2):
    var1 = db[names[idx1]]
    var2 = db[names[idx2]]
    calc = "higher" if var2 > var1 else "lower"
    if result == calc or var1 == var2:
        return True
    else:
        return False


print("Welcome to Higher or Lower")

db = {
    "Jim Thorpe": 74000,
    "A Clockwork Orange": 135000,
    "David Bowie": 1220000,
    "Gordie Howe": 40500,
    "Melania Trump": 4090000,
    "Fargo": 823000,
    "The Jester": 8100,
    "Window Cleaner": 33100,
    "Uber": 20400000,
    "Mozambique": 246000,
    "Pemba Dorje Sherpa": 1300,
    "Lockerbie Bombing": 9900,
    "Jurassic Park": 1220000,
    "Cheese Fondue": 40500,
    "Bovril": 33100,
    "South Africa": 673000,
    "Iran": 1500000,
    "Drug Addiction": 60500,
    "Russia": 2240000,
    "HP": 2740000,
    "IAMS": 22200,
    "Miley Cyrus": 3350000,
    "The OC": 301000,
    "Harambe": 368000,
    "Doctor Who": 1500000,
    "Pythagoras": 201000,
    "Tokyo": 673000,
    "Testicular Cancer": 135000,
    "Potala Palace": 14800,
    "Atlanta Falcons": 1500000,
    "Cannabis": 823000,
    "Bitcoin": 11100000,
    "Robert De Niro": 823000,
    "Chicago White Sox": 246000,
    "Poland": 550000,
    "Taj Mahal": 1220000,
    "Colossus of Rhodes": 74000,
    "Fruit Ninja": 1500000,
    "Maradona": 450000,
    "Cheap Flights": 6120000,
    "Doritos": 301000,
    "Huffington Post": 7480000,
    "Divorce Lawyer": 40500,
    "Alicia Keys": 1000000,
    "Staffordshire Bull Terrier": 246000,
    "Cher": 1000000,
    "LifeHacker": 550000,
    "Michael Jackson": 4090000,
    "Albert Einstein": 1500000,
    "Antidepressants": 201000,
    "Saxophone": 301000,
    "Weightlifting": 45000
}

names = ["Jim Thorpe", "A Clockwork Orange", "David Bowie", "Gordie Howe", "Melania Trump", "Fargo",
         "The Jester", "Window Cleaner", "Uber", "Mozambique", "Pemba Dorje Sherpa", "Lockerbie Bombing",
         "Jurassic Park", "Cheese Fondue", "Bovril", "South Africa", "Iran", "Drug Addiction",
         "Russia", "HP", "IAMS", "Miley Cyrus", "The OC", "Harambe", "Doctor Who", "Pythagoras", "Tokyo",
         "Testicular Cancer", "Potala Palace", "Atlanta Falcons", "Cannabis", "Bitcoin", "Robert De Niro",
         "Chicago White Sox", "Poland", "Taj Mahal", "Colossus of Rhodes", "Fruit Ninja", "Maradona",
         "Cheap Flights", "Doritos", "Huffington Post", "Divorce Lawyer", "Alicia Keys",
         "Staffordshire Bull Terrier", "Cher", "LifeHacker", "Michael Jackson", "Albert Einstein",
         "Antidepressants", "Saxophone", "Weightlifting"]

used_names = []
score = 0
idx1 = find_idx(names, used_names)
cur_name = names[idx1]
used_names.append(cur_name)

while True:
    idx2 = find_idx(names, used_names)
    next_name = names[idx2]
    used_names.append(next_name)
    print(f"{cur_name} has {db[cur_name]} average monthly searches.")
    print("vs.")
    result = input(f"{next_name} has 'higher' or 'lower' searches than {cur_name}?\n").lower()
    sentinel = compare_ans(result, names, db, idx1, idx2)
    if not sentinel:
        break
    score += 1
    print(f"You're right! Current score: {score}")
    cur_name = next_name
    idx1 = idx2

if score == len(names):
    print(f"You got all the comparisons right!")
else:
    print(f"Sorry, that's wrong: Final score: {score}")
