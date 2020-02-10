import json
from difflib import get_close_matches

dictionary = json.load(open("data.json"))

def lookUp(word):
    stdEntry = word.lower()
    nl = '\n'  #newline for fstrings
    err = f"ERROR: {word} not found."

    if stdEntry in dictionary:
        return f"{stdEntry.capitalize()}:{nl}{nl.join(dictionary[stdEntry])}"
    elif stdEntry.capitalize() in dictionary:  #checking for proper nouns
        return f"{stdEntry.capitalize()}:{nl}{nl.join(dictionary[stdEntry.capitalize()])}"
    elif stdEntry.upper() in dictionary:  #checking for acronyms/initialisms
        return f"{stdEntry.upper()}:{nl}{nl.join(dictionary[stdEntry.upper()])}"
    elif len(get_close_matches(stdEntry, dictionary.keys())) > 0:
        closestMatch = get_close_matches(stdEntry, dictionary.keys())[0]
        response = (
        err,
        f"Did you mean {closestMatch}?",
        "Enter Y if Yes, or any other input if No. ")
        confirmation = input(nl.join(response))
        if confirmation == "Y":
            return f"{closestMatch.capitalize()}:{nl}{nl.join(dictionary[closestMatch])}"
        else:
            return err
    else:
        return err

entry = input("Enter word: ")

print(lookUp(entry))