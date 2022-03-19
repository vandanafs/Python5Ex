import math
from typing import List
from math import ceil
from math import floor


def get_item_at_position(list_in: List, pos: int) -> List:
    """
    Returns the item at pos.

    :param list_in: Input list
    :param pos: Position of desired item in list_in
    :return: Item in pos
    """
    #pass  # remove pass statement and implement me
    return list_in[pos]


def print_list_items(list_in: List) -> None:
    """
    Given a list, this function iterates through it and prints each element.

    :param list_in: Input list
    :return: None
    """
    #pass  # remove pass statement and implement me
    for i in list_in:
         print(i)



def sort_by_commit_count(list_in: List) -> List:
    """
    Given a list of entries, return a new list sorted based on the commit count.

    :param list_in: A list where each entry is a list containing a name and the commit count corresponding to a user
    :return: The same list sorted in ascending order based on the commit count
    """
    #pass  # remove pass statement and implement me
    (list_in.sort(key=lambda  list_in: list_in[1]))
    return list_in



def gen_list_of_nums(n: int) -> List[int]:
    """
    Given a number (N), this function returns a list of integers from 0 to N (exclusive).

    :param n: The number of items the result should contain
    :return: A list of integers
    """
    #pass  # remove pass statement and implement me
    new_list=[]
    for i in range(n) :
        new_list.append(i)
    return new_list


def half_list1(list_in: List, half: int) -> List:
    """
    Given a list, this function will return a new list that contains half of the items in the list_in parameter.

    :param list_in: The list which will be used to generate the return value
    :param half: 1 will use the first half of the input list. 2 will use the second half of the input list.
    If the length of list_in is an odd number, round the half value up (hint: math.ceil()).
    :return: A list.
    """
    #pass  # remove pass statement and implement me
    length_input=ceil(len(list_in)/2)
    print(length_input)
    list_out=[]
    if  half == 1:
        for i in range(length_input) :
            list_out.append(i)

        print(list_out)
        return list_out
    else:
        #size=odd i strt my index length_input-1
        if len(list_in) % 2!=0:
            length_input -=1
        for i in range(length_input,len(list_in)):
            list_out.append(i)
        print(list_out)
        return list_out


def half_list(list_in: List, half: int) -> List:
    from math import ceil
    i=ceil(len(list_in)/2)
    if half == 1:
        list_in=list_in[:i]
    else :
        list_in=list_in[-i:]
    return list_in


def remove_odds(list_in: List[int]) -> None:
    """
    Given a list of integers, this function removes the odd numbers from the same list.

    :return: None
    """
    #pass  # remove pass statement and implement me

    for i in range(len(list_in)) :
        if i % 2 !=0 :
            list_in.remove(i)
    print(list_in)
    return list_in


def remove_evens(list_in: List[int]) -> None:
    """
    Given a list of integers, this function removes the even numbers from the same list.

    :return: None
    """
    #pass  # remove pass statement and implement me
    for i in range(len(list_in)) :
        if i % 2 ==0 :
            list_in.remove(i)
    print(list_in)
    return list_in



def concatenate_lists(list_a: List, list_b: List) -> List:
    """
    Given two lists, this function combines them and returns the result as a new list.

    :param list_a: A list
    :param list_b: Another list
    :return: A list containing all elements from list_a and list_b
    """
    #pass  # remove pass statement and implement me
    return list_a +list_b


def multiply_list(list_in: List, scalar: int) -> List:
    """
    Given a list and an integer, this function will return a new list which is the result of multiplying
    the input list by the value of the scalar.

    :param list_in: A list
    :param scalar: An integer
    :return: A list
    """
    #pass  # remove pass statement and implement me
    element=list_in[0]
    for i in range(scalar-1) :
          list_in.append(element)
    print(list_in)


    return list_in
