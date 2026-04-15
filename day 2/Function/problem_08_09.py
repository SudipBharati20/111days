#8.Write a python function to remove a given word from a list ad strip it at the same 
#time.
def remove_word_from_list(word_list, word_to_remove):
    return [word.strip() for word in word_list if word.strip() != word_to_remove]

#9.Write a python function to print multiplication table of a given number. 
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")