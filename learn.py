#!/usr/bin/env python3
from random import randint
file=open('vocab','r',encoding='utf8')
vocab=[]
for line in file:
	vocab.append({'l1':line.split('=')[0],'l2':line.strip('\n').split('=')[1]})
remaining=len(vocab)-1
while remaining>0:
	thisround = randint(0,remaining)
	fromlang = 'l'+str(randint(1,2))
	if fromlang=='l1':
		tolang='l2'
	else:
		tolang='l1'
	answer=input("Please Translate the word "+vocab[thisround][fromlang]+" :")
	if answer==vocab[thisround][tolang]:
		print('Correct!')
		vocab.remove(vocab[thisround])
		remaining-=1
		print(remaining," words left !")
	else:
		print('Incorrect :(')
print("All words in the List have been successfully learnt")
