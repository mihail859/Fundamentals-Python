version = input().split('.')
version_number = int("".join(version))
version_number += 1
string_number = str(version_number)
new_version = ''
for ch in string_number:
    new_version += ch + '.'

output_string = new_version.rstrip('.')  # Removes trailing dots
print(output_string)