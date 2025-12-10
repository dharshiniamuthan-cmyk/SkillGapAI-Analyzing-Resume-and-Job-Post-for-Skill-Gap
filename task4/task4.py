job_title = input("Enter job title: ")
clean_title = ''.join(ch for ch in job_title if ch.isalnum() or ch.isspace())
print("Normalized Title:", clean_title.title())


OUTPUT
Enter job title: soft*ware dev@eloper!!
Normalized Title: Software Developer
