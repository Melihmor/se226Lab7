import string
def reverse_string(s):
    sreversed=s[::-1]
    return sreversed

def capitalize_words(s):
    scapital=s.upper
    return scapital

def remove_punctuation(input_string):
    result = input_string
    for char in string.punctuation:
        result = result.replace(char, '')
    return result
