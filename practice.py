""" Pylint told me I should add an doc String"""

import collections
import functools
############################################################
# Problem 1a

def compute_max_word_length(text):
    """
    Given a string |text|, return the longest word in |text|.  If there are
    ties, choose the word that comes latest in the alphabet.
    A word is defined by a maximal sequence of characters without whitespaces.
    You might find max() and list comprehensions handy here.
    """
    # BEGIN_YOUR_CODE (around 1 line of code expected)
    var_f = lambda a, b: min(a, b) if len(min(a, b)) > len(max(a, b)) else max(a, b)
    return functools.reduce(var_f, text.split())
    #raise Exception("Not implemented yet")
    # END_YOUR_CODE

############################################################
# Problem 1b

def manhattan_distance(loc1, loc2):
    """
    Return the Manhattan distance between two locations, where the locations
    are pairs of numbers (e.g., (3, 5)).
    """
    # BEGIN_YOUR_CODE (around 1 line of code expected)
    #raise Exception("Not implemented yet")
    return abs((loc1[1] - loc2[1])) + abs((loc1[0] - loc2[0]))
    # END_YOUR_CODE

############################################################
# Problem 1c

def sparse_vector_dot_product(self_v1, self_v2):
    """
    Given two sparse vectors |v1| and |v2|, each represented as Counters, return
    their dot product.
    You might find it useful to use sum() and a list comprehension.
    """
    # BEGIN_YOUR_CODE (around 5 lines of code expected)
    return sum([v*self_v2[k] for (k, v) in self_v1.most_common()])
    # END_YOUR_CODE

############################################################
# Problem 1d

def compute_most_frequent_word(text):
    """
    Splits the string |text| by whitespace and returns two things as a pair: 
    the set of words that occur the maximum number of times, and
	their count, i.e. (set of words that occur the most number of times, that maximum number/count)
    You might find it useful to use collections.Counter().
    """
    # BEGIN_YOUR_CODE (around 5 lines of code expected)
    cnt = collections.Counter(text.split())
    var_f = lambda k: cnt[k] == max(cnt.values())	
    return (set([k for k in cnt.keys() if var_f(k)]), max(cnt.values()))
    # END_YOUR_CODE
    #return (set(filter(f, cnt.keys())), max(cnt.values()))
    #raise Exception("Not implemented yet")
    #count = max(cnt.values())
    #cnt.subtract(collections.Counter(cnt.keys()*(count-1)))
    #return (set(cnt.elements()), count)
############################################################
# Problem 1e

def correct_parentheses(expression):
    """
    Checks if a given expression has a correct combination of opening and
    closing parentheses. (a+b)*c returns True, ((a+b) returns False.
    Hint: use stack
    """
    # BEGIN_YOUR_CODE 
    var_st = list()
    for var_c in iter(expression):
        if var_c == '(':
            var_st.append(var_c)
        elif var_c == ')':
            try:
                var_st.pop()
            except IndexError:
                return False
    return len(var_st) == 0
    #raise Exception("Not implemented yet")
    # END_YOUR_CODE
    
############################################################
# Problem 1f

def nested_parentheses(expression):
    """
    Must be done recursively. 
    Given a string, return true if it is a nesting of zero or more pairs of parenthesis, 
    like "(())" or "((()))". Suggestion: check the first and last chars, 
    and then recur on what's inside them. 

    nestedParentheses("(())") -> true
    nestedParentheses("((()))") -> true
    nestedParentheses("(((x))") -> false
    
    Use this link to practice in Java first:
    http://codingbat.com/prob/p183174
    """
    # BEGIN_YOUR_CODE 
    if expression == "":
        return True
    if expression.startswith('(') and  expression.endswith(')'):
        return nested_parentheses(expression[1:-1])
    else:
        return False
    #raise Exception("Not implemented yet")
    # END_YOUR_CODE    
