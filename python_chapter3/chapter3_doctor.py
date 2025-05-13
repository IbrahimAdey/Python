input("What is your problem? ")

# Prompt if the problem has occurred before
response = input("Have you had this problem before (yes or no)? ").strip().lower()

if response == 'yes':
    print("Well, you have it again.")
elif response == 'no':
    print("Well, you have it now.")
else:
    print("I didn’t understand your response.")