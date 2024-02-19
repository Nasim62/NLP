# Q2. If you are trying to print a string, what happens if you leave out one of the quotation marks, or both?
# Ans.If i leave out one of the quotation marks, Python will not know where the string ends, so i’ll get a SyntaxError. 
#     If i leave out both, Python will think i am trying to reference a variable and will raise a NameError if the variable is not defined. 
#     Here’s an example:  
print(Hello, world)
# This will result in a NameError: name 'Hello' is not defined