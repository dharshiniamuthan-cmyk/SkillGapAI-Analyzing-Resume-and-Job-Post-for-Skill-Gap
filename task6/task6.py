paragraph = input("Enter resume text: ").lower()
skill = input("Enter skill to search: ").lower()
count = paragraph.count(skill)
print(f"Skill appears {count} times.")


OUTPUT
Enter resume text: Python is good. Python developer uses Python
Enter skill to search: python
Skill appears 3 times.
