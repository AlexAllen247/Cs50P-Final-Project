# Cs50P Final Project - Scrabble Practice

### Video Demo: https://www.youtube.com/watch?v=5gEZeCL9qZo

### Description:

This is the final project of the Cs50 Introduction to Programming with Python course. This project is called Scrabble Practice. This is a program to help Scrabble players improve their ability to create words with seven randomly generated letters. As an avid Scrabble player myself, this was the main reasoning for the creation of this program. It has helped me to become faster at forming words from any Scrabble rack. There are three main functions in the program. The first function generates seven random letters for the user, the second checks if it is a word and the third scores the word if it is a word.

`random_letters()` - This function generates seven random letters to the terminal for the user to make words from them. Those seven letters are generated randomly from the set amount of letters in a Scrabble game. I used the Counter function from the collections module to count all the letters, which were then sorted in a list. Then I used the sample function from the random module to then pick the seven random letters from that list. Once the letters are generated on the terminal, the user can then input their word into the terminal.

`check_word()` - This function then checks the user's word to see if it is in fact a word from the Scrabble dictionary. I was able to obtain the 2019 Collins Scrabble Word dictionary, and so the word is compared to those in that file. If it is not a word, the program will exit and a message will come up saying better luck next time. If it is a word, it will then be scored by the final function.

`word_score()` - This function scores the word based on the points of each letter from the Scrabble game. I use a for loop to iterate through all the letters of the word to get the points of each letter and calculate the total points of the word. The total points of the word are then printed to the terminal with a congratulatory message.

The test file tests each of the main functions in the project to make sure the functions perform correctly:
`test_random_letters()` - tests whether the random letters function produces random letters.
`test_check_word()` - tests whether the user's word is a word or not.
`test_word_score()` - tests the scores of sample words.