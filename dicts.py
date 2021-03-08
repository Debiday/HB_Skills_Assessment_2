"""Dictionaries Assessment

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """
    count = {}

    for word in phrase.split(" "): #split into separate words
        if word in count:
            count[word] = count[word] + 1 #if key already exists in dictionary
        else:
            count[word] = 1
    return count.items()


def print_melon_at_price(price):
    """Given a price, print all melons available at that price, in alphabetical order.

    Here are a list of melon names and prices:

    Honeydew 2.50
    Cantaloupe 2.50
    Watermelon 2.95
    Musk 3.25
    Crenshaw 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

    If there are no melons at that price print "None found"

        >>> print_melon_at_price(2.50)
        Cantaloupe
        Honeydew

        >>> print_melon_at_price(2.95)
        Watermelon

        >>> print_melon_at_price(5.50)
        None found
    """
    melons = {
        "Honeydew": 2.50,
        "Cantaloupe": 2.50,
        "Watermelon": 2.95,
        "Musk": 3.25,
        "Crenshaw": 3.25,
        "Christmas": 14.25,
    }
    
    key_list = list(melons.keys())
    val_list = list(melons.values())

    melons_list = []
    for i in range(len(melons)):
        if float(val_list[i]) == float(price):
            melons_list.append(key_list[i])
    return ' \n'.join(melons_list)
 

def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

    translate = {
        "sir": "matey",
        "hotel": "fleabag inn",
        "student": "swabbie",
        "man": "matey",
        "professor": "foul blaggart",
        "restaurant": "galley",
        "your": "yer",
        "excuse": "arr",
        "students": "swabbies",
        "are": "be",
        "restroom": "head",
        "my": "me",
        "is": "be",
    }

    translated = []

    key_list = list(translate.keys())

    words = phrase.split()

    for word in words:
        if word in key_list: #iterate through the list to find each word
            translated.append(translate[word]) #if word in list, lookup value from dict
        else:
            translated.append(word)
    return ' '.join(translated)


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Two more examples:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

        >>> kids_game(["noon", "naan", "nun"])
        ['noon', 'naan', 'nun']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """
    #create a dictionary with each name as a key

    name_dict = {}
    
    # turn all the names into dictionary keys
    for name in names: 
         name_dict[name] = [] 

    # turn the dict into a list
    key_list = list(name_dict.keys())

    # create a list for first letters of each name
    first_letter_list = []

    for i in key_list:
        first_letter_list.append(i[0])

    #if the last letter of name is in the first_letter add that to key-value in name_dict
    for name in names:
        if name[-1] == name[0]: #to account for edge case of noon naan nun
            name_dict[name] = names
        elif name[-1] in first_letter_list:
            name_dict[name] = key_list[first_letter_list.index(name[-1])] 
        else:
            break

    #create the final string
    final_string = []
    
    #turn dict into list to iterate over
    list_dict = list(name_dict.items())
    first_key = list_dict[0][0]
    final_string.append(first_key)

    for i in range(len(list_dict)):
        for j in range(len(list_dict)):
            if list_dict[i][1] == list_dict[j][0] and list_dict[i][1] not in final_string:
                final_string.extend([list_dict[j][0], list_dict[j][1]])
    return final_string


    
"""give up :P"""

print(kids_game(["bagon", "baltoy", "yamask", "starly","nosepass", "kalob", "nicky", "booger"]))
print(kids_game(["apple", "berry", "cherry"]))
print(kids_game(["noon", "naan", "nun"]))
