
def luhn_validate(final_num):
    # return a boolean which indicates a an id number may be validated against the Luhn algorithm
    return final_num % 10 == 0


def add_check_digit(pre_check):
    # add in the arbitrary checksum integer, in this case we randomly chose 3.  It could be any digit 1-9
    return pre_check + 3


def split_and_add(d_digit):
    """
    for numbers 10, 12, 14, 16, 18
    modulus divide by 10 and 1 to remainder
    Ex:  18 / 10 = 1 remainder 8;  1 + 8 = 9
    """
    return (d_digit % 10) + 1


def doubler(digit):
    """
    double the digit passed to this function
    for digits 0 - 9
    possible return values are
    0 2 4 6 8 10 12 14 16 18
    """
    return digit * 2


def find_indexes(id_number):
    """
    We need to start doubling integers from the right of the id

    Examples:
    For a 6 digit number '123456', we start from 6 and double 5, 3, 1 (indexes 4, 2, 0)
    For a 7 digit number '1234567', we start from 7 and double 6, 4, 2 (indexes 5, 3, 1)

    Therefore we can assume:
    - for any id with a length that is an even number our indexes with start at 0
    - for any id with a length that is an odd number our indexes with start at 1
    Therefore we can actually address the string from left to right instead, which is more logical for most ppl

    comprehension uses range() with starting index determined by even/odd length & step = 2, thus every other index
    """

    # if even number length id, get indexes
    if len(id_number) % 2 == 0:
        return [idx for idx in range(0, len(id_number), 2)]
    # if odd number length id, get indexes
    return [idx for idx in range(1, len(id_number), 2)]


def main(number_string):
    """
    The Luhn formula is a widely used system for validating identification numbers.
    Using the original number, double the value of every other digit starting from the right,
    then add the values of the individual digits together.
    Note that double digits resulting from the doubling process must be treated as two individual digits.
    Add in an extra, predetermined ‘checksum’ digit and then if the sum is divisible by 10, it is ‘valid’.

    """
    # reduced fixed length of 6 digits our indexes are [0, 2, 4]
    idx = find_indexes(number_string)
    print(idx)
    # initialize final value
    final = 0

    for i in range(len(number_string)):
        # coerce character to integer
        num = int(number_string[i])
        if i in idx:
            # if index indicates we double the digit, send to 'doubler'
            doubled = doubler(num)
            # if the doubled digit is a value greater or equal to 10, split and add
            if doubled >= 10:
                summed = split_and_add(doubled)
                final += summed
            else:
                final += doubled
        else:
            final += num

    # add check digit
    final = add_check_digit(final)
    # final sum
    print(final)
    # validate
    print(luhn_validate(final))


if __name__ == '__main__':
    main('123456')
