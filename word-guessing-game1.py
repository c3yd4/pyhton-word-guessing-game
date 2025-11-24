import random

word_bank= ["ophelia","lovely","speed","element","lock"]
word= random.choice(word_bank)

guessed_word=["_"]*len(word)
attempts=10
guessed_letters=[]

print("Welcome to the Word Guessing Game!!")

while attempts > 0:
    print("\nWord: " + " ".join(guessed_word))
    print(f"Remaining entitlement: {attempts}")

    guess=input("Guess a letter please: ").lower()
    
    if not guess.isalpha() or len(guess)!= 1:
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already entered this letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i]== guess:
                guessed_word[i]=guess

    else:
        attempts-=1
        print(f"Wrong guess, you have only {attempts} left.")
    if "_" not in guessed_word:
        print(f"You found the word! {word}")
        break
if attempts==0 and "_" in guessed_word:
    print(f"You lost. The word is {word}")
        
    
