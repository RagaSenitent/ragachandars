alpha= input("Input the alphabet: ")
if alpha in ('a', 'e', 'i', 'o', 'u'):
	print("%s vowel." % alpha)
elif alpha in ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'):
	print("consonant.")
else:
	print("invalid") 
