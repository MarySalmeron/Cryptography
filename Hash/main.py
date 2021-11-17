'''
	Name: main.py
	
    Authors: 
		* María José Salmerón Contreras 
		* Edgar Alejandro Ramírez Fuentes
    
'''

from classes.Hash import Hash

if __name__ == "__main__":
    hash=Hash()
    text=input("Enter the name of the file with the text:\n")
    blocks=hash.read_plaintext(text)
    res=hash.xor(blocks)
    for index in range(3):
        print(f"El resultado del hash es: {chr(res[index]+97)} \n")