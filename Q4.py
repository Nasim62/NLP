# Q4. In math notation, leading zeros are ok, as in 09. What happens if you try this in Python? What about 011?
# Ans.In Python, a number with a leading zero is interpreted as an octal (base 8) number. 
#     So, 09 would result in a SyntaxError because 9 is not a valid digit in the octal system. Example:
print(011)
# Output: SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers