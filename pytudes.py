# vim: find an replace in all lines after the current one (range from current
# to eof:
#     :.,$s/foo/bar/g

# Terminology:
# sequence: list, tuple
# iterable: set

import logging as log

log.basicConfig(
    level=log.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


# Sums all multiples of a set of numbers (union or intersection) below
# a defined threshold.

# Backlog:
# TODO investigate why eval(expression) evaluates the way it does when
# using binary logic operators
# TODO alternative implementation with meta-programming
def calculate_multiples(factors: set, threshold: int, logic_op: str):
    # convert all set elements into string to enable concatenation
    #   XXX for factor in factors: # factor is value, not address
    #   XXX   factor = str(factor)
    for factor in factors:
        stringified_factors = [str(factor) for factor in factors]

    # this way you avoid needing to use meta-programming to avoid a repetitive
    # conditional
    # however these symbols actually make a bitwise comparison in the binary
    # representation of these numbers, so perhaps I should use raw "ands" and
    # "ors" instead of their bitwise logic counterparts.
    logic_symbols = {"intersection": "and", "union": "or"}
    # That's how you'd do it if it were a list.
    #            expression = f"{factor[1]}"
    #            for factor in factors[1:]:
    #                expression += f"{logic_symbols["and"]} {factor}"

    multiples: set = set()
    for i in range(1, threshold):
        modulo_divisions = [f" {i} % {factor} == 0 "
                            for factor in stringified_factors]
        expression = f" {logic_symbols[logic_op]} ".join(modulo_divisions)

        log.debug(expression)
        log.debug(eval(expression))
        if eval(expression) is True:
            log.debug(f"Expression true for: {i}")
            multiples.add(i)

    eval(expression)

    log.debug(f"Multiples of {str(factors)} up to {str(threshold)} " +
              f"with {logic_op} " +
              f"operation: {str(multiples)}")
    return multiples


def calculate_fibonacci(threshold: int):
    sequence: list = [1, 2]
    while sequence[-1] < threshold:
        next = sequence[-1] + sequence[-2]
        sequence.append(next)
    log.debug(f"Sequence is {str(sequence)}")
    return sequence


def find_even(array: list):
    even: list = []
    for array_item in array:
        if array_item % 2 == 0:
            even.append(array_item)
    return even
