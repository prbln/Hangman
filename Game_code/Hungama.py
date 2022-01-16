import requests
from collections import defaultdict
from PyDictionary import PyDictionary
play_again=True

class Play_Game: 
	def __init__(self):
		self.lives = 3
		self. word = self.fetch_new_word()
		self.all_gussed_letters = defaultdict(bool)	

	def fetch_new_word(self):
		link = "https://random-word-api.herokuapp.com/word?"
		response = requests.get(url = link)

		if response.status_code!=200:
			return 0 
		word = response.json()[0]

		self.lettersleft = len(word)
		self.display_string='_'*len(word) 
		return word

	def valid_input_letters(self,gussed_letter):
		if not gussed_letter.isalpha():
			print("Please enter only english aplhabets")
			return 0 
		elif len(gussed_letter)!=1:
			print("Please enter single letter at a time")
			return 0
		elif self.all_gussed_letters[gussed_letter]:
			print("Letter already gussed, try another letter")
			return 0
		else:
			self.all_gussed_letters[gussed_letter]=True
			return gussed_letter

	def correct_guess(self,gussed_letter):
		wordList  = list(self.word)
		display_stringList = list(self.display_string)
		for ind,letter in enumerate(wordList):
			if letter == gussed_letter:
				display_stringList[ind]=gussed_letter
		print(*display_stringList,sep=' ')
		return ''.join(display_stringList)

	
	def hint(self,lives_left):
		clue = PyDictionary() 
		if lives_left==3:
			return clue.synonym(self.word)

		elif lives_left==2:
		
			return type(clue.antonym(self.word))
		else:
			return clue.meaning(self.word)

	def start_game(self):
		
		print(*list(self.display_string),sep=' ')

		while(self.lives>0 and self.lettersleft>0):
			input_letter =	input("Guess a letter - ")
			gussed_letter = self.valid_input_letters(input_letter)
			if gussed_letter==0:
				continue 
			if gussed_letter in self.word:
				self.display_string = self.correct_guess(gussed_letter) 
				self.lettersleft-=self.word.count(gussed_letter)
			else:
				self.lives-=1
				print("Oopes that is not correct!")
				if self.lives in [1,2,3] and self.hint(self.lives) != None:
					hint_required = input("Do you need a hint? Y|N ")
					if hint_required=='Y':
						print(type(self.hint(self.lives)))
				print(*list(self.display_string),sep=' ')
			
			print(f"Lives left - {self.lives}")
		if self.lives ==0:
			print(f"Better Luck Next time. The word was {self.word}")
		else:
			print("Congratulations! You won!")

if __name__	== '__main__':
	
	obj = Play_Game()
	if obj.word == 0:
		print("Bad response")
	else:
		obj.start_game() 

	replay = input("Do you want to play again? Y|N - ")
	if replay =='Y':
		__main__.py
