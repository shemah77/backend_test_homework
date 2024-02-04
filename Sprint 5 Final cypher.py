
# Яндекс контест № задачи 106243150

import string

DIGIT: str = string.digits
CHAR: str = string.ascii_letters
CONST_RAZR: int = 10


def decode_instructions(instructions: str) -> list:
    stack: list = []
    i_count: int = 0
    num1: int = 0
    while i_count < len(instructions):
        if instructions[i_count] in DIGIT:

            while i_count < len(instructions) and instructions[i_count].isdigit():
                num1 = num1 * CONST_RAZR + int(instructions[i_count])
                i_count += 1
            stack.append(str(num1))
            num1: int = 0

        elif instructions[i_count] == ']':
            symb: str = ''
            fin: str = ''

            while stack and stack[-1] != '[':

                if stack[-1].isalpha():
                    symb = stack.pop() + symb

            stack.pop()

            if str(stack[-1]).isdigit():
                num: str = stack.pop()
                for n in range(1, int(num) + 1):
                    fin = symb + fin

            stack.append(fin)

            i_count += 1
        else:
            stack.append(instructions[i_count])
            i_count += 1

    return stack


def main():
    cypher_str: str = str(input())
    res: list = decode_instructions(cypher_str)
    print(*res, sep='')


if __name__ == '__main__':
    main()
