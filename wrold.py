import random

with open('FILE PATH TO WORDLIST') as file:
    word_list = [line.strip() for line in file.readlines()]

selected_word = random.choice(word_list)
guess_count = 0 #if you were to add a loop this need to be reset to 0 

first_L = ''
second_L = ''
third_L = ''
fourth_L = ''
fifth_L = ''

print("\nWelcome to the Wrodle game!\n")

print(selected_word)

while first_L != selected_word[0]: #while first_L is not in selected_word
    first_L = input("Guess a letter in the first position: ").lower() #input first letter converts to lower
    guess_count += 1
    if selected_word[0] == first_L: #if first char == firs_L print correct
        print("Correct!")
        print(first_L + " _ _ _ _")
    elif first_L == "duck":
        print("why would you type that")
    elif first_L in selected_word:
        print("its in there")
    else: 
        print("Incorrect!")


while second_L != selected_word[1]: #while first_L is not in selected_word
    second_L = input("Guess a letter in the second position: ").lower() #input first letter converts to lower
    guess_count += 1
    if selected_word[1] == second_L: #if first char == firs_L print correct
        print("Correct!")
        print(first_L + second_L + "_ _ _")
    elif second_L in selected_word:
        print("its in there")
    else: 
        print("Incorrect!")


while third_L != selected_word[2]: #while first_L is not in selected_word
    third_L = input("Guess a letter in the third position: ").lower() #input first letter converts to lower
    guess_count += 1
    if selected_word[2] == third_L: #if first char == firs_L print correct
        print("Correct!")
        print(first_L + second_L + third_L + "_ _")
    elif third_L in selected_word:
        print("its in there")
    else: 
        print("Incorrect!")


while fourth_L != selected_word[3]: #while first_L is not in selected_word
    fourth_L = input("Guess a letter in the fourth position: ").lower() #input first letter converts to lower
    guess_count += 1
    if selected_word[3] == fourth_L: #if first char == firs_L print correct
        print("Correct!")
        print(first_L + second_L + third_L + fourth_L + "_")
    elif fourth_L in selected_word:
        print("its in there")
    else: 
        print("Incorrect!")


while fifth_L != selected_word[4]: #while first_L is not in selected_word
    fifth_L = input("Guess a letter in the last position: ").lower() #input first letter converts to lower
    guess_count += 1
    if selected_word[4] == fifth_L: #if first char == firs_L print correct
        print("You Got it right! The word was " + selected_word)
    elif first_L in selected_word:
        print("its in there")
    else: 
        print("Incorrect!")



#little easter eggs

if selected_word == 'fatal':
    print("Just like your guessing skills!")

if guess_count == 5: 
    print("\nOne try? Really? Sure i'll believe you\n")

if guess_count >= 100:
    print("it took you", guess_count, "... your pretty good at this game")