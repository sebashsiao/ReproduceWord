from reproduce_word import repr_rand_word
from random import randint

times = randint(3,10)

repr_word =  repr_rand_word("Banana", times)

print(repr_word)