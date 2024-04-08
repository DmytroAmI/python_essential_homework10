import re


def analyze_text(text):
    """Print unique words in text, length words and length unique words."""
    words = re.findall(r"\w+", text)
    unique_words = set(words)
    print("Unique words:", unique_words)
    print("Length of words:", len(words))
    print("Length of unique words:", len(unique_words))


if __name__ == '__main__':
    analyze_text('hhhh hhhh hhhh hhh hhh hhh hh hh h')
