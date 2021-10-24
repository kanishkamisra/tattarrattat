import itertools
import string

A = ['a', 'b', 'c', 'd']

def palindrome(alphabet, length, separator = ' '):
    '''
    Given a list of alphabets and length, generate a 
    list of palindromes constructed using the alphabets
    '''
    if length == 1:
        return alphabet
    elif length == 2:
        palindromes = [f'{a} {a}' for a in alphabet]
        return palindromes
    elif length % 2 == 0:
        # even X{} + reversed({})X
        palindromes = []
        # combs = list(itertools.product(alphabet, repeat =  int((length / 2) - 2)))
        # pairs = itertools.product(alphabet, repeat = 2)
        combs = list(itertools.product(alphabet, repeat =  int((length - 1) / 2)))
        for a in alphabet:
            for combination in combs:
                middle_half = separator.join(combination)
                middle_other_half = separator.join(reversed(combination))
                palindromes.append(f'{a}{separator}{middle_half}{separator}{middle_other_half}{separator}{a}')
        return palindromes
    else:
        # odd {} X rev({})
        palindromes = []
        combs = list(itertools.product(alphabet, repeat =  int((length - 1) / 2)))
        for a in alphabet:
            for combination in combs:
                prefix = separator.join(combination)
                suffix = separator.join(reversed(combination))
                palindromes.append(f'{prefix}{separator}{a}{separator}{suffix}')

        return palindromes


print(palindrome(A, 1))
print(palindrome(A, 2))
print(palindrome(A, 3))
print(palindrome(A, 6))

for i in range(1, 6):
    print(f'Number of palindromes of length {i}: {len(palindrome(A, i))}')