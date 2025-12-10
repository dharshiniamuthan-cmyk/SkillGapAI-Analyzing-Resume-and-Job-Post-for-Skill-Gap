text = input("Enter the resume paragraph: ")
words = text.split()
total_words = len(words)
unique_words = len(set(words))
most_repeated = max(set(words), key=words.count)
print("Total words:", total_words)
print("Unique words:", unique_words)
print("Most repeated word:", most_repeated)


OUTPUT
Enter the resume paragraph: I am a Python developer and Python programmer.
Total words: 8
Unique words: 7
Most repeated word: Python
