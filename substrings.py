a = "abc"
b = "A quick brown fox jumps over the lazy dog"

print(
    f"\"{a}\" is{('', ' not')[bool(set(a) - set(b))]} substring of \"{b}\""
)
