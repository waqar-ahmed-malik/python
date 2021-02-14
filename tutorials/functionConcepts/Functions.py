print('imported successfully')


def characters_count(phrase: str, letters: str = 'aeiou') -> dict:      # function with default values
    """Returns a dictionary containing each character in the letters string found in phrase
       string as key and value as the corresponding occurrence count in the phrase string.  """
    result = {}
    for letter in letters:
        for character in phrase:
            if letter == character:
                result.setdefault(letter, 0)
                result[letter] += 1
    return result

# dict is the return type and its just for documentation purpose.


def exist(phrase: str, letter: str) -> bool:
    """Checks if a letter exist in the phrase"""
    letter_set = set(letter)
    phrase_set = set(phrase)
    result = phrase_set.intersection(letter_set)
    return bool(result)


# print(exist('Lets Check', 'e'))                                             # function call
# print(characters_count('once and always the end is beautiful.', 'aeiou'))   # function call

# print(exist(phrase='Lets Check', letter='e'))                               # function call with keyword assignment.


def advance_function(*args, **kwargs):              # function can accept any number of positional or keyword arguments.
    print(args)                                     # positional arguments
    print(kwargs)                                   # keyword arguments


advance_function('a', 'b', param1='p1', param2='p2')    # Call 1

courses = ['a', 'b']
info = {'param1': 'p1', 'param2': 'p2'}

advance_function(courses, info)     # both will be considered as positional arguments as they won't be unpacked.
# above one results in advance_function(['a', 'b'], {'param1': 'p1', 'param2': 'p2'}) and will be two argument function.

advance_function(*courses, **info)  # First they will be unpacked and this call will be equivalent to Call 1
# this will be like advance_function('a', 'b', param1='p1', param2='p2')
