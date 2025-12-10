items = input("Enter technologies (comma separated): ").lower().split(",")
items = [i.strip() for i in items]
languages = {"python", "java", "c", "c++"}
databases = {"mysql", "mongodb", "postgres"}
frameworks = {"django", "flask", "react", "angular"}
count_lang = sum(1 for i in items if i in languages)
count_db = sum(1 for i in items if i in databases)
count_fw = sum(1 for i in items if i in frameworks)
print("Programming Languages:", count_lang)
print("Databases:", count_db)
print("Frameworks:", count_fw)


OUTPUT
Enter technologies (comma separated): python, mysql, react, java
Programming Languages: 2
Databases: 1
Frameworks: 1
