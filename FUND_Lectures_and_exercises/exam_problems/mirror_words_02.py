import re

pattern = r"([@#])([a-zA-Z]{3,})\1{2}([a-zA-Z]{3,})\1"
text = input()

result = re.findall(pattern, text)


palindrome_list = []

if result:
    for element in result:
        first_word = element[1]
        second_word = element[2]
        if first_word == second_word[::-1]:
            palindrome_list.append(f"{first_word} <=> {second_word}")
    print(f"{len(result)} word pairs found!")
    if not palindrome_list:
        print("No mirror words!")
    else:
        print(f"The mirror words are:")
        print(', '.join(palindrome_list))
else:

    print("No word pairs found!\nNo mirror words!")