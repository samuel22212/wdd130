#test sentences
from sentences import get_determiner, get_noun, get_verb
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners


def test_get_noun():
    single_nouns = ["bird", "Boy", "car", "cat", "child"]
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_noun(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_nouns

    plural_nouns =["dogs", "girls", "men", "rabbits", "women"]
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_noun(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in plural_nouns

def test_get_verb():
    single_verbs = ["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_verb(1, "present")

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_verbs

    plural_verbs = ["drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"]
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_verb(2, "present")

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in plural_verbs

    past_verbs =[ "drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_verb(1, "past")

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in past_verbs 

    plural_past_verbs =[ "drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_verb(2, "past")

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in plural_past_verbs 

    future_verbs = ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"]
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_verb(1, "future")

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in future_verbs

    plural_future_verbs = ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"]
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_verb(2, "future")

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in plural_future_verbs


def test_get_prepositon():
    pass

def test_get_prepositional_phrase():
    pass 
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])