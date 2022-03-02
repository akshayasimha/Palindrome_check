print("Enter a word: ")
word1 = input()
list_word1 = []

for chars in word1:
    print(chars)
    list_word1.append(chars)

backup = list_word1.copy()
print("String before reversing is:" , backup)

list_word1.reverse()
print("String after reversing is:", list_word1)

if backup == list_word1:
    print("Yes. It is palindrome.")

else:
    print("No. It is not palindrome.")
