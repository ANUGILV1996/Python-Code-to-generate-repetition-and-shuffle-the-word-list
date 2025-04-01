Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Python Code to generate repetition and shuffle the word list. 
... 
... #Start of code
... 
... import random
... 
... # List of words with their Token IDs
... words = [ "word1", "word2", "word3", "word4", "word5",
...           "word6", "word7", "word8", "word9", "word10",
...           "word11", "word12", "word13", "word14", "word15",
...           "word16", "word17", "word18", "word19", "word20"]
... 
... # Generate list with repetition
... word_repeats = words*10
... 
... # Shuffle to randomize order
... random.shuffle(word_repeats)
... 
... # Select 200 words
... final_list = word_repeats[:200]
... 
... # Print the shuffled word list with token ID and repetition
... for i, word in enumerate(final_list, start=1):
...     print(f"{i}. {word}")
... 
