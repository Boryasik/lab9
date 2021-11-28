def sort_sentence(sentence):
    sentence_sort = sentence[0].lower() + sentence[1:len(sentence)]
    list_sentence_sort = sentence_sort.split()
    list_sentence_sort.sort(key=len)
    sentence_sort = " ".join(list_sentence_sort)
    sentence_sort = sentence_sort[0].upper() + sentence_sort[1:len(sentence)]
    return sentence_sort
