def is_anagram(word1, word2) -> bool:
    # Convert the words into lists of characters
    list1 = list(word1)
    list2 = list(word2)

    # Check that the words have the same length
    if len(list1) != len(list2):
        return False

    # Check that the words are different
    if word1 == word2:
        return False

    # Sort the lists of characters
    list1.sort()
    list2.sort()

    # Compare the sorted lists
    if list1 == list2:
        return True
    else:
        return False


# Example of use
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

if is_anagram(word1.lower(), word2.lower()):
    print("The words are anagrams.")
else:
    print("The words are not anagrams.")
