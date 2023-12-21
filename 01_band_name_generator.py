# welcome message
print("Welcome to the Band Name Generator.")

# prompt for city
city = input("\nWhat is the name of the city you grew up in?\n")
if not city:
    city="Sokoto"
# prompt for pet name
pet = input("\nWhat is the name of your pet?\n")
if not pet:
    pet="Lions"

def output_msg(city, pet ):
    print(f"Your band name could be {city} {pet}")

# output
output_msg(city, pet)


