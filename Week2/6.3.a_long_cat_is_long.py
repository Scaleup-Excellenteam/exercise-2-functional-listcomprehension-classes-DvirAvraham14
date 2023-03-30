def count_words(text):
    """
    Count the number of words in a string, and return a dictionary with the word
    lengths as keys and the number of words of that length as values.
    :param text: The text to be analyzed
    :return: A dictionary with the word lengths as keys and the number of words of
    """
    # Clean the text by removing non-letter characters
    cleaned_text = ''.join(c for c in text if c.isalpha() or c.isspace())
    # Use a dictionary comprehension to count the word lengths
    word_lengths = {word: len(word) for word in cleaned_text.split()}
    return word_lengths

# Test the function

text = """
You see, wire telegraph is a kind of a very, very long cat.
You pull his tail in New York and his head is meowing in Los Angeles.
Do you understand this?
And radio operates exactly the same way: you send signals here, they receive them there.
The only difference is that there is no cat.
"""

print(count_words(text))