import re


def user_data(text):
    """Extract data from text and return dict."""
    name = re.search(r"([A-Z][a-z]+)\W([A-Z][a-z]+)", text)
    birth = re.search(r"\d{1,2}[-\s]\d{1,2}[-\s]\d{4}", text)
    mail = re.search(r"\w+@\w+\.\w+", text)
    review = re.search(r"(\.\w+)\W+(.+)", text)

    return {
        name.group(1): {
            "name:": name.group(2),
            "birth": birth.group(),
            "mail": mail.group(),
            "review": review.group(2)}
    }


if __name__ == '__main__':
    data = user_data("King Alex, birthday: 12-04-2011, mail: skddfj@ukr.net, Some review text")
    print(data)
