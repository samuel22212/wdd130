#sentences 
import random

words = []
def main():
    sentence1 = get_sentence(1,"past")
    sentence2 = get_sentence(1,"present")
    sentence3 = get_sentence(1,"future")
    sentence4 = get_sentence(2,"past")
    sentence5 = get_sentence(2,"present")
    sentence6 = get_sentence(2,"future")

    print(sentence1)
    print(sentence2)
    print(sentence3)
    print(sentence4)
    print(sentence5)
    print(sentence6)

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
    "bird", "boy", "car", "cat", "child",
    "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
    "birds", "boys", "cars", "cats", "children",
    "dogs", "girls", "men", "rabbits", "women"

    Parameter
    quantity: an integer that determines if
    the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity ==1:
        words = ["bird", "Boy", "car", "cat", "child"]
    else: 
        words = [ "dogs", "girls", "men", "rabbits", "women"]
    
    word = random.choice(words)
    return word

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
    "drank", "ate", "grew", "laughed", "thought",
    "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
    "drinks", "eats", "grows", "laughs", "thinks",
    "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
    "drink", "eat", "grow", "laugh", "think",
    "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
    "will drink", "will eat", "will grow", "will laugh",
    "will think", "will run", "will sleep", "will talk",
    "will walk", "will write"

    Parameters
    quantity: an integer that determines if the
    returned verb is single or plural.
    tense: a string that determines the verb conjugation,
    either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == "present":
        if quantity == 1:
            words = ["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]
        elif quantity != 1: words =["drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"]

    elif tense == "past":
        words =["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]

    elif tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"]

    word = random.choice(words)
    return word

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    words = ["about", "above", "across", "after", "along","around", "at", "before", "behind", "below","beyond", "by", "despite", "except", "for","from", "in", "into", "near", "of","off", "on", "onto", "out", "over","past", "to", "under", "with", "without"]
    word = random.choice(words)
    return word
def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """
    preposition = get_preposition()
    if quantity ==1:
        noun = get_noun(1)
        determiner = get_determiner(1)
    elif quantity != 1: 
        noun = get_noun(2)
        determiner = get_determiner(2)

    prepositonal_phrase = preposition+" "+determiner+" "+noun
    return prepositonal_phrase


    

def get_sentence(quantity,tense):
    if tense == "present":

        if quantity == 1:
            
            phrase = get_prepositional_phrase(1)
            determiner = get_determiner(1)
            noun = get_noun(1)

        elif quantity !=1:
            phrase = get_prepositional_phrase(2)
            determiner = get_determiner(2)
            noun = get_noun(2)

    elif tense == "past":
            verb = get_verb(quantity,"past")
        
    elif tense == "future":
            verb = get_verb(quantity,"future")
        
    elif tense == "present":
            if quantity == 1:
                get_verb(1,"present")
            elif quantity != 1:
                get_verb(2,"present")
    sentence = (f"{determiner} {noun} {verb} {phrase}.")
    return sentence


"""
This is my milestone code before I wrote the get sentence function. I didn't have it in me to delete it so I am commenting it out. 
 #runs the program obtaining a determiner, noun, and verb in that order. 
    determiner1 = get_determiner(1).capitalize()
    noun1 = get_noun(1)
    verb1 = get_verb(1,"past")
    sentence1 =  (f"{determiner1} {noun1} {verb1}.")

    determiner2 = get_determiner(1).capitalize()
    noun2 = get_noun(1)
    verb2 = get_verb(1,"present")
    sentence2 =  (f"{determiner2} {noun2} {verb2}.")

    determiner3 = get_determiner(1).capitalize()
    noun3 = get_noun(1)
    verb3 = get_verb(1,"future")
    sentence3 =  (f"{determiner3} {noun3} {verb3}.")

    determiner4 = get_determiner(2).capitalize()
    noun4 = get_noun(2)
    verb4 = get_verb(2,"past")
    sentence4 =  (f"{determiner4} {noun4} {verb4}.")

    determiner5 = get_determiner(2).capitalize()
    noun5 = get_noun(2)
    verb5 = get_verb(2,"present")
    sentence5 =  (f"{determiner5} {noun5} {verb5}.")

    determiner6 = get_determiner(2).capitalize()
    noun6 = get_noun(2)
    verb6 = get_verb(2,"future")
    sentence6 =  (f"{determiner6} {noun6} {verb6}.")

    print(sentence1)
    print(sentence2)
    print(sentence3)
    print(sentence4)
    print(sentence5)
    print(sentence6)

            
            

"""
if __name__ == "__main__":
    main()