###

def read_content(file):
    return open(file).read()


def num_line_without_char(file: str, char: str) -> int:
    return len(tuple(filter(lambda x: x[0] != char, open(file).readlines())))


def hash_display(file: str) -> str:
    return "".join(map(lambda x: f"{x}#", open(file).read()))


def JTOI(file: str) -> str:
    return "".join(map(lambda x: x if x != "J" else "I", open(file).read()))
