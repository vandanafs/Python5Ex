from math import ceil
def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
   # pass  # remove pass statement and implement me
    input=value.replace(" ","")
    lower=input.lower()
    #print("input string",lower)
    length_half=ceil(len(lower)/2)
    #print(lower[length_half])
    #print(ceil(length_half))
    for i in range(0,length_half):
       if lower[i] != lower[len(lower)-i-1] :
            return False

    return True



