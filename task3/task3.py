sentence = input("Enter experience sentence: ")
for word in sentence.split():
    if word.isdigit():  # checks if word is a number
        print("Experience Detected:", word, "Years")
        break


OUTPUT
Enter experience sentence: I have 4 years of experience.
Experience Detected: 4 Years
