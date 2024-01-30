

# НАЧАЛО ЭКСПОРТА =======

globals()
DIGIT = '0123456789'
CHAR = 'abcdifghijklmnopqrstuvwxyz'

def decode_instructions(instructions: str) -> str:
    stack: list = []
    i: int = 0
    num1: int = 0
    while i < len(instructions):
        if instructions[i] in DIGIT:

            while i < len(instructions) and instructions[i].isdigit():
                num1 = num1 * 10 + int(instructions[i])
                i += 1
            stack.append(str(num1))
            num1: int = 0

        elif instructions[i] == ']':
            symb: str = ''
            fin: str = ''

            while stack and stack[-1] != '[':
                # print (stack[-1])
                if stack[-1].isalpha():
                    symb = stack.pop() + symb

            stack.pop()

            if str(stack[-1]).isdigit():
                num = stack.pop()
                for n in range(1, int(num) + 1): fin = symb + fin

            stack.append(fin)

            i += 1
        else:
            stack.append(instructions[i])
            i += 1

    return ''.join(stack)


def main ():
    cypher_str = str(input())
    res: str
    res = decode_instructions(cypher_str)
    print(res)

if __name__ == '__main__':
    main()


