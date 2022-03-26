def odd_num(to):
    for i in range(1, to + 1, 2):
        yield i


if __name__ == "__main__":
    a_gen = odd_num(15)
    for elem in a_gen:
        print(elem)