import sys


if len(sys.argv) != 2:
    print("invalid number of arguments: expected 1")

else:
    name = sys.argv[1]
    used_chars = ""

    for char in name:
        if char not in used_chars:
            print(f"\'{char}\': {name.count(char)}")
            used_chars += char
