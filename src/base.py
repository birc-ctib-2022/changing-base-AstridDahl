"""Changing bases."""

digits = {}

for i in range(0, 10):
    digits[i] = str(i)

digits[10] = 'A'
digits[11] = 'B'
digits[12] = 'C'
digits[13] = 'D'
digits[14] = 'E'
digits[15] = 'F'


def change_to_base(n: int, b: int) -> str:
    """
    Return `n` in base `b`.

    The base `b` must be in the range 2 to 16.

    >>> change_to_base(1, 2)
    '1'
    >>> change_to_base(31, 2)
    '11111'
    >>> change_to_base(31, 8)
    '37'
    >>> change_to_base(31, 16)
    '1F'
    """
    assert 2 <= b <= 16

    n_base = []
    negative = False

    if n == 0:
        n_base.append('0')

    elif n < 0:
        negative = True
        n *= -1

    while n:
        n_base.append(digits[n % b])
        n //= b
    
    if negative == True:
        n_base.append('-')

    # reverse string
    n_str = ''
    n_str = ''.join(n_base[::-1])


    return n_str  # FIXME: return n in the right base


print(change_to_base(31, 16))