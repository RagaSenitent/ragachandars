alpha= input("Input the alphabet: ")

if alpha in ('a', 'e', 'i', 'o', 'u'):
	print("%s is a vowel." % alpha)
elif alpha == 'y':
	print("Sometimes y is vowel or consonant.")
else:
	print("%s consonant." % alpha) 
