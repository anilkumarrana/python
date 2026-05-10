from interview import reverse_string, is_palindrome, factorial, find_largest

def test():
    print(f"reverse_string('hello') == 'olleh': {reverse_string('hello') == 'olleh'}")
    print(f"is_palindrome('A man, a plan, a canal: Panama') == True: {is_palindrome('A man, a plan, a canal: Panama') == True}")
    print(f"factorial(5) == 120: {factorial(5) == 120}")
    print(f"find_largest([1, 5, 3, 9, 2]) == 9: {find_largest([1, 5, 3, 9, 2]) == 9}")

if __name__ == "__main__":
    test()
