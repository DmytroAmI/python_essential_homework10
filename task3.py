import re


def print_last_three_symbols(text):
    """Print last 3 symbols in each word in the text"""
    words = re.findall(r"\w{3}\b", text)
    print(words)


if __name__ == '__main__':
    print_last_three_symbols('hello friend, how are you?, Im fine')
