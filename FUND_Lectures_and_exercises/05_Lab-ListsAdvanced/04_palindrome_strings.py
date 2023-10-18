words = input().split()
palindrome = input()
palindrome_words = [w for w in words if w == w[::-1]]
found_palindromes = palindrome_words.count(palindrome)
print(palindrome_words)
print(f"Found palindrome {found_palindromes} times")