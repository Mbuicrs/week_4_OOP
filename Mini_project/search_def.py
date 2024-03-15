import json
from difflib import get_close_matches

class Dictionary:
    def __init__(self, dictionary_file):
        # Loads the dictionary data from the JSON file
        with open(dictionary_file) as f:
            self.dictionary_data = json.load(f)

    def get_definition(self, word):
        # Convert the word to lowercase for case insensitivity
        word = word.lower()

        if word in self.dictionary_data:
            return self.dictionary_data[word]
        
        elif word.title() in self.dictionary_data:  # Check for title case
            return self.dictionary_data[word.title()]
        
        elif word.upper() in self.dictionary_data:  # Check for uppercase
            return self.dictionary_data[word.upper()]
        else:
            # Try to find a close match for the word
            close_matches = get_close_matches(word, self.dictionary_data.keys())
            if close_matches:
                suggestion = close_matches[0]
                response = input(f"Did you mean '{suggestion}' \n instead? Enter Y if yes, or N if no: ")
                if response.lower() == 'y':
                    return self.dictionary_data[suggestion]
                elif response.lower() == 'n':
                    return "The word doesn't exist. Please double check it."
                else:
                    return "Invalid input. Please enter Y or N."
            else:
                return "The word doesn't exist. Please double check it."

def main():
    # Create a Dictionary object with the dictionary file
    dictionary = Dictionary("dic_data.json")

    # Prompt the user to enter a word
    word = input("Enter a word: ")

    # Get the definition of the word
    definition = dictionary.get_definition(word)

    # Print the definition
    print(definition)
    
main()
