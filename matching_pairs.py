import math

def matching_pairs(s, t):
    out = 0

    # For i & j, indices are selected to encompass the full envelope of swap combinations.
    for i in range(len(s)-1):
        for j in range(i+1, len(t)):
            # For each swap, a temporary string is generated reflecting "s" with indices i & j switched.
            tmp_str = "".join((s[:i], s[j], s[i+1:j], s[i], s[j+1:]))
            tmp_max = 0
            # Pairs of strings of which exist (with swapped 's' & 't') in the same column and match with each other are counted.
            for k in range(len(tmp_str)):
                if t[k] == tmp_str[k]:
                    tmp_max += 1
            # The tally of matching pairs for each string swap are compared to the running maximum & updated accordingly.
            if tmp_max > out:
                out = tmp_max
    return out

def printInteger(n):
    print('[', n, ']', sep='', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printInteger(expected)
        print(' Your output: ', end='')
        printInteger(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    s_1, t_1 = "abcde", "adcbe"
    expected_1 = 5
    output_1 = matching_pairs(s_1, t_1)
    check(expected_1, output_1)

    s_2, t_2 = "abcd", "abcd"
    expected_2 = 2
    output_2 = matching_pairs(s_2, t_2)
    check(expected_2, output_2)

    s_3, t_3 = "mno", "mno"
    expected_3 = 1
    output_3 = matching_pairs(s_3, t_3)
    check(expected_3, output_3)
