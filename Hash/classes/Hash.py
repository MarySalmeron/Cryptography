'''
	Name: Hash.py
	
    Authors: 
		* María José Salmerón Contreras 
		* Edgar Alejandro Ramírez Fuentes
    
'''

import math
import textwrap

class Hash:

	def __init__(self):
		'''
			Class used to do hash
		'''
		return
	
	def __cleanText(self, text : str):
		'''
			Clean the plaintext to delete characters that do not belong to the english alphabet
			Parameters
			--------------
			text : str
				It is the text that will be cleaned
			Returns
			--------------
			text : str
				It is the text cleaned
		'''
		text = text.replace(' ','')
		text = text.replace('\n','')
		text = text.replace('.','')
		text = text.replace(',','')
		text = text.lower()
		return text
	
	def read_plaintext(self, textFile : str):
		'''	
			Read the plaintext from the textfile provided, add padding if necessary, and divide the plaint text in blocks.
			Parameters
			-------------
			textFile : str
				It is the filename (with extension) that contains the plaintext
    
			Returns
			-------------
			blocks : list
				It is the plaintext divided in blocks
		'''
		with open(textFile ,'r', encoding="utf-8") as textfile_data:
			blocks=[]
			plaintext = textfile_data.read()
			plaintext = self.__cleanText(plaintext)
			# Add padding to the message if it is necessary
			plaintext= self.__paddingProcess(plaintext)
			blocks = textwrap.wrap(plaintext, 3)
			return blocks
	
	def __paddingProcess(self, plaintext : str):
		'''
			Add the necessary padding to the plaintext to fulfill the length of the initialization vector
			Parameters
			-------------
			plaintext : str
				It is the plaintext that will be padded
			Returns
			--------------
			plaintext : str
				It is the plaintext with the necessary padding added 
		'''
		plaintext= plaintext.strip()
		if len(plaintext) % 3 != 0:
			plaintext_length = len(plaintext)
			padding = (3 * (math.floor(plaintext_length / 3 + 1))) - plaintext_length
			# Add the padding to the plaintext
			plaintext += ("*" * padding)
		return plaintext

	def xor(self, blocks):
		'''
			xor between each block
			Parameters
			-------------
			blocks : bits
				It is the blocks that will be xor
			Returns
			--------------
			plaintext : str
				The result othe xor
		'''
		block0=[0,0,0]
		for block in blocks:
			# Transform the block from letters to int
			block = [ord(letter) for letter in block]
			print(f"Tamaño de block {len(block)}")
			print(f"Tamaño de block0 {len(block0)}")
			for i in block:
				block0[i]=block[i]
			for block in blocks:
				# XOR between each block
				for index in range(len(block)):
					block0[index] ^= block[index]
		return block0
