import re


def search_data(file_read, file_write):
    """Search data on birth, mail, phone from file and write to other file."""
    with open(file_read, 'r') as f:
        file_contents = f.read()

    birth = re.search(r"\d{1,2}[-\s]\d{1,2}[-\s]\d{4}", file_contents)
    mail = re.search(r'\w+@\w+\.\w+', file_contents)
    p = r"\d{3}[-\s]??\d{3}[-\s]??\d{2}[-\s]??\d{2}|\(\d{3}\)[-\s]??\d{3}[-\s]??\d{2}[-\s]??\d{2}"
    phone = re.search(p, file_contents)

    with open(file_write, 'w') as f:
        f.write(birth.group() + "\n" + mail.group() + "\n" + phone.group())


if __name__ == '__main__':
    search_data('data.txt', 'new_data.txt')
    with open('new_data.txt', 'r') as file:
        print(file.read())
