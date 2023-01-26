"""
This is an example of how to format our code
"""

humor = "humor"
the_name = "the name"
quote = (
    "Sometimes it pays to stay in bed on Monday, rather than spending "
    "the rest of the week debugging Monday\'s code."
)

# Output ...
print(
    f"Code is like {humor}. When you have to explain it, it’s bad.",
    f"Experience is %s everyone {the_name} gives to their mistakes.",
    quote,
    sep="\n"
)

print("Let\'s calculate 2 pul two multiplied by 2", 2 + (2 * 2), sep=": ")

c = (2 + 2) * 2  # This is just an example expression
