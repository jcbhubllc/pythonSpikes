my_name = "Jim"
my_role = "President"

def jims_func(nm, rl):
    """
    This is a function docstring.  The purpose is to describe what the
    function does and give important information.

    This function takes 2 variables; nm, rl.  It will insert the variables
    into a phrase for output.

    Parameters:
    nm = the name of the person being referenced.
    rl = the role of the person being referenced.
    """

    # the f before the string indicates an f-string.  Look it up.
    phrase = f"{nm} is the {rl} of jcbhub."
    
    return phrase


my_phrase = jims_func(my_name, my_role)
print(my_phrase)
