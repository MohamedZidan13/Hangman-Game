import random 
words = ["bad", "good","game", "nice", "hook"]
random_word = random.choice(words)
guessed_letters = []
len = len(random_word)
word_list = ["_"]*len 
final_list = " ".join(word_list)
print(final_list)
n = 0
chances = 6
acci_hang_man = [''' +---+
  |   |
      |
      |
      |
      |
=========''',''' +---+
  |   |
  O   |
      |
      |
      |
=========''','''+---+
  |   |
  O   |
  |   |
      |
      |
=========''','''+---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''+---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''+---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',''' +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
print("")
print(acci_hang_man[n])
while "_" in final_list and chances != 0: 
  letter_index = 0
  guess = input("Please guess a letter: ").lower()
  if guess in guessed_letters :
    print("\nYou already guessed that. Try again. ")
    print(f"\nYou have {chances} chances")
    print(acci_hang_man[n])
  else :
    if guess not in random_word :
      chances -= 1
      n += 1
      print(acci_hang_man[n])
    else :
      for letter in random_word :
        if guess == letter :
          word_list[letter_index] = letter
          letter_index += 1
        else :
          letter_index += 1
    final_list = " ".join(word_list)
    guessed_letters.append(guess)
    print(final_list)
    print(f"\nYou have {chances} chances")
if chances == 0 :
  print("\n     You lose!     ")
else :
  print("""\n     ********** You Win !!!! ********** 
    """)
  
