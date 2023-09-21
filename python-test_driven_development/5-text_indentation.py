#!/usr/bin/python3
"""python3 -c 'print(__import__("5-text_indentation").__doc__)'"""


def text_indentation(text):
    """ prints a text with 2 new lines after each of these characters: ., ? and :
    Param Arg: text(str) - text to be printed
    raise Exception:
    TypeError - if not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    count = 0
    while count < len(text) and text[count] == ' ':
        count += 1

    while count < len(text):
        print(text[count], end="")
        if text[count] == "\n" or text[count] in ".?:":
            if text[count] in ".?:":
                print("\n")
            count += 1
            while count < len(text) and text[count] == ' ':
                count += 1
            continue
        count += 1
