def write_sale(argv):
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        program, *args = argv
        for el in args:
            f.write(f'{el:>12}\n')
        return 0

if __name__ == '__main__':
    import sys
    sys.exit(write_sale(sys.argv))