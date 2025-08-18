ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def encode(n: int) -> str:
    list = []
    while n > 0:
        a = n//62
        list.append(ALPHABET[a])
        n = a
    return "".join(list)