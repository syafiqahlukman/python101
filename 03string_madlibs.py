def mad_libs(): 
# def - tells python that you are defining a function
# mad_libs is name of the function
# ()are used to define any inputs the function might need. In this case, our function doesn't need any inputs, so the parentheses are empty.

    # Prompt the user for various words
    colour = input("Enter a colour: ")
    noun = input("Enter a noun: ")
    noun = noun.capitalize()
    celebrity_name = input("Enter a celebrity name: ")
    celebrity_name = celebrity_name.title()
  

    # Story template (use f string to embed user input directly)
    story = f"""
    Roses are {colour},
    {noun} are blue,
    I love {celebrity_name}.
    """

    # Print the completed story
    
    print(story)

# Run the Mad Libs game
mad_libs() #means you are calling the function (Since you have define it)
'''
If you only define the function but never call it, the computer knows what to do but never actually does it. 
By calling the function, you make the computer execute the instructions inside the function.
'''