import requests 
from collections import defaultdict
play_again=True

def Fetch_New_Word():
	link = "https://random-word-api.herokuapp.com/word?"
	response = requests.get(url = link)
	if response.status_code!=200:
		return 0 
	word = response.json()[0]
	return word

def valid_input_letters(gussed_letter,all_gussed_letters):
	if not gussed_letter.isalpha():
		print("Please enter only english aplhabets")
		return 0 
	elif len(gussed_letter)!=1:
		print("Please enter single letter at a time")
		return 0
	elif all_gussed_letters[gussed_letter]:
		print("Letter already gussed, try another letter")
		return 0
	else:
		all_gussed_letters[gussed_letter]=True
		return gussed_letter

def correct_guess(gussed_letter,word,display_string):
	wordList  = list(word)
	display_stringList = list(display_string)
	for ind,letter in enumerate(wordList):
		if letter == gussed_letter:
			display_stringList[ind]=gussed_letter
	print(*display_stringList,sep=' ')
	return ''.join(display_stringList)

def play_game(word):
	
	length = len(word)
	all_gussed_letters = defaultdict(bool)	
	lettersleft = length
	lives = 5 
	display_string='_'*length
	print(*list(display_string),sep=' ')

	while(lives>0 and lettersleft>0):
		print(f"Lives left - {lives}")
		input_letter =	input("Guess a letter - ")
		gussed_letter = valid_input_letters(input_letter,all_gussed_letters)
		if gussed_letter==0:
			continue 
		if gussed_letter in word:
			display_string = correct_guess(gussed_letter,word,display_string) 
			lettersleft-=1
		else:
			lives-=1
			print(*list(display_string),sep=' ')
	if lives ==0:
		print(f"Better Luck Next time. The word was {word}")
	else:
		print("Congratulations! You won!")
while(play_again):
	word = Fetch_New_Word()
	if word == 0:
		print("Bad response")
	else:
		play_game(word) 
	replay = input("Do you want to play again? Y|N - ")
	if replay =='N':
		play_again = False
