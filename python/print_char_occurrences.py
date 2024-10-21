name = input("Enter Name: ")

used_chars = ""

for char in name:
    if char not in used_chars:
        print(f"{char}: {name.count(char)}")
        used_chars += char
