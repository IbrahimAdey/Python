def generate_word():
   
	alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	return alphabets
    
while True:
	alphabets = generate_word()
for alphabet in alphabets:
	correct_answer = ([alphabet] + [13])
    
	user_input = string(input("Enter a word"))

for index in enumerate(alphabets):
	print(index)
       