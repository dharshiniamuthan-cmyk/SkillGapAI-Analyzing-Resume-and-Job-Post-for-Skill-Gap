skills = input("Enter skills: ").lower()
if "python" in skills or "ml" in skills or "data" in skills:
    print("Category: Data / ML")
elif "html" in skills or "css" in skills or "javascript" in skills:
    print("Category: Web Development")
elif "java" in skills or "c++" in skills:
    print("Category: Software Development")
else:
    print("Category: Other")


OUTPUT
Enter skills: python, machine learning, sql
Category: Data / ML
