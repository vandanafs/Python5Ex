def is_anagram(first_string: str, second_string: str) -> bool:
    """
    Given two strings, this functions determines if they are an anagram of one another.
    """
   # pass  # remove pass statement and implement me
    if sorted(first_string) ==  sorted(second_string) :
        return True
    else:
         return False



