def count_characters(s):
    count=len(s)
    return count

def count_words(s):
    scount=len(s.split(" "))
    return scount

def average_word_length(s):
    return len(count_characters(s))/len(count_words(s))
