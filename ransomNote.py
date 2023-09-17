def canConstruct(ransomNote, magazine):
    letter_counts = {}

    # Count the occurrences of letters in magazine
    for char in magazine:
        letter_counts[char] = letter_counts.get(char, 0) + 1

    # Check if ransomNote can be constructed
    for char in ransomNote:
        if char not in letter_counts or letter_counts[char] == 0:
            return False
        letter_counts[char] -= 1

    return True
