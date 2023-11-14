sample_text = input()
encrypted_list = [chr(ord(w) + 3) for w in sample_text]
print("".join(encrypted_list))