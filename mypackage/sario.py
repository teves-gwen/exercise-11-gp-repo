from pyjokes import get_joke

def tell_joke():
    return get_joke()

print("\n-------------------------------------------------------")
print(f"\nJoke of the day: {tell_joke()}")