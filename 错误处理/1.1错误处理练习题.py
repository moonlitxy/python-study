from functools import reduce


def str2num(s):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError as e:
            raise ValueError(f'Invalid input:\'{s}\'  is neither nor a float.')


def calc(exp):
    try:
        ss = exp.split('+')
        ns = map(str2num, ss)
        return reduce(lambda acc, x: acc + x, ns)
    except Exception as e:
        print("error:{exp},{e}")
        return None


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


main()
