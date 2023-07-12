# Create a function called generate_password that generates any length of password for the user.
# The password should have a random mix of upper letters, lower letters, numbers, and punctuation symbols.
# The function should ask the user how strong they want the password to be.
# The user should pick from - weak, strong, and very strong.
# If the user picks weak, the function should generate a 5-character long password.
# If the user picks strong, generate an 8-character password and 
# if they pick very strong, generate a 12-character password.

import string
import random
from random import randint

def generate_password():

    nb_upper_letter = nb_lower_letter = nb_number = nb_punctuation =  1
    random_list = ["upper", "lower", "number", "punctuation"]
    password = ""

    weak_character = 1
    strong_character = 4
    very_strong_character = 8

    user_choice = ""
    while user_choice not in ["weak", "strong", "very strong"]:
        user_choice = input("How strong do you want the password to be? (weak, strong or very strong): ")
        print("*"*59)

        if user_choice == "weak":
            while weak_character:
                random_mix = random.choice(random_list)
                if random_mix == "upper": nb_upper_letter+=1
                elif random_mix == "lower": nb_lower_letter+=1
                elif random_mix == "number": nb_number+=1
                elif random_mix == "punctuation": nb_punctuation+=1
                weak_character -= 1
            print(f"Password with {nb_lower_letter} lower, {nb_upper_letter} upper, {nb_number} number and {nb_punctuation} punctuation!")
            password = list(random.choices(string.ascii_uppercase, k=nb_upper_letter) + random.choices(string.ascii_lowercase, k=nb_lower_letter) + random.choices(string.digits, k=nb_number) + random.choices(string.punctuation, k=nb_punctuation))
            return password
        
        if user_choice == "strong":
            while strong_character:
                random_mix = random.choice(random_list)
                if random_mix == "upper": nb_upper_letter+=1
                elif random_mix == "lower": nb_lower_letter+=1
                elif random_mix == "number": nb_number+=1
                elif random_mix == "punctuation": nb_punctuation+=1
                strong_character -= 1
            print(f"Password with {nb_lower_letter} lower, {nb_upper_letter} upper, {nb_number} number and {nb_punctuation} punctuation!")
            password = list(random.choices(string.ascii_uppercase, k=nb_upper_letter) + random.choices(string.ascii_lowercase, k=nb_lower_letter) + random.choices(string.digits, k=nb_number) + random.choices(string.punctuation, k=nb_punctuation))
            return password
        
        if user_choice == "very strong":
            while very_strong_character:
                random_mix = random.choice(random_list)
                if random_mix == "upper": nb_upper_letter+=1
                elif random_mix == "lower": nb_lower_letter+=1
                elif random_mix == "number": nb_number+=1
                elif random_mix == "punctuation": nb_punctuation+=1
                very_strong_character -= 1
            print(f"Password with {nb_lower_letter} lower, {nb_upper_letter} upper, {nb_number} number and {nb_punctuation} punctuation!")
            password = list(random.choices(string.ascii_uppercase, k=nb_upper_letter) + random.choices(string.ascii_lowercase, k=nb_lower_letter) + random.choices(string.digits, k=nb_number) + random.choices(string.punctuation, k=nb_punctuation))
            return password
        
def lettre_random(nom):
    nom_liste = list(nom)
    for _ in range(len(nom)):
        rand_index = randint(0, len(nom_liste) - 1)
        yield nom_liste.pop(rand_index)

new_str = "".join([letter for letter in lettre_random(generate_password())])
print("*"*59)
print(new_str)
