import re


def split_text(text):
    """Split text into the words and find their frequency"""
    pattern = re.compile(r"(\w+)")
    matches = pattern.findall(text)
    print("words:", matches)

    for match in set(matches):
        print(f"word '{match}' count {matches.count(match)} times in text")


if __name__ == '__main__':
    split_text('asd asd asd asd asd asd asd ., fff wr ff')
