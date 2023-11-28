import re
def count_words(text):
    words = re.findall(r'\b\w+\b', text)
    return len(words)
if __name__ == "__main__":
    given_text = "To be, or not to be, that is the question"
    word_count = count_words(given_text)
    print(f"The number of words in the text is: {word_count}")