text = input("Enter text: ").split()
email = None
for word in text:
    if "@" in word:
        email = word
        break
if email:
    print("Email found:", email)
else:
    print("No email detected.")


OUTPUT
Enter text: My email is dharshini123gmail.com
No email detected.
