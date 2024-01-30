def cypher(word):
    cypher_str = str(word)
    cypher_list = list(cypher_str)
    number_list: list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    indexes_list = []
    index_number = ''
    index_in_str = ''
    final_str = ''
    Final_array = []
    stek = []
    skobki_list_L = []
    skobki_list_R = []
    for i in range(len(cypher_list)):

        # числа до 300 могут быть вкючительно
        if cypher_list[i] in number_list:
            index_number = index_number + cypher_list[i]
            cypher_list[i] = False
            if cypher_list[i + 1] in number_list:
                index_number = index_number + cypher_list[i + 1]
                cypher_list[i + 1] = False
                if cypher_list[i + 2] in number_list:
                    index_number = index_number + cypher_list[i + 2]
                    cypher_list[i + 2] = False

            indexes_list.append(index_number)
            # print(indexes_list)
            index_number = ''

        if cypher_list[i] == '[':
            stek.append(cypher_list[i])
            indexL = i
            skobki_list_L.append(indexL)



        elif cypher_list[i] == ']':
            indexR = i
            skobki_list_R.append(indexR)
            if len(stek) > 0:
                last_item_stek = stek.pop(-1)
                if last_item_stek == '[':
                    indexL = skobki_list_L.pop(-1)
                    indexR = skobki_list_R.pop(-1)
                    index_in_str = indexes_list.pop(-1)
                    # print (index_in_str)
                    # print(cypher_str[indexL:indexR+1])
                    a = str(index_in_str + cypher_str[indexL:indexR + 1])
                    # print (a)
                    # print (f' we find  at {cypher_str.find(a)}')

                    final_str = ''
                    for n in range(1, int(index_in_str) + 1):
                        final_str = final_str + cypher_str[indexL + 1:indexR]

                    if '['  in final_str and ']' in final_str:
                        return cypher(final_str)
    return final_str


def parenthetic_contents(string):
    """Generate parenthesized contents in string as pairs (level, contents)."""
    stack = []
    for i, c in enumerate(string):
        if c == '[':
            stack.append(i)
        elif c == ']' and stack:
            start = stack.pop()
            yield (len(stack), string[start + 1: i])


def parse(expr):
    def _helper(iter):
        items = []
        for item in iter:
            if item == '[':
                result, closeparen = _helper(iter)
                if not closeparen:
                    raise ValueError("bad expression -- unbalanced parentheses")
                items.append(result)
            elif item == ']':
                return items, True
            else:
                items.append(item)
        return items, False
    return _helper(iter(expr))[0]

# =========== польская обратная нотация =========

# НАЧАЛО ЭКСПОРТА =======

globals()
DIGIT = '0123456789'
CHAR = 'abcdifghijklmnopqrstuvwxyz'



def decode_instructions(instructions: str) -> str:
    stack: list = []
    # stack_dig = []
    # stack_char = []
    # fin = ''
    symb = ''
    fin = ''
    i: int = 0
    while i < len(instructions):
        if instructions[i] in DIGIT:
            # num = DIGIT.index(instructions[i])
            num = num * 10 + int(instructions[i])
            i += 1
            stack.append(str(num))

        elif instructions[i] == ']':
            symb = ''
            fin = ''

            while stack and stack[-1] != '[':
                # print (stack[-1])
                if stack[-1].isalpha():
                    symb  = stack.pop() + symb

            stack.pop()

            if str(stack[-1]) in DIGIT:
                num = stack.pop()
                for n in range(1, int(num) + 1): fin = symb  + fin

            stack.append(fin)

            i += 1
        else:
            char = instructions[i]
            stack.append(char)
            i += 1

    # return ''.join(stack)
    return ''.join(stack)




def main ():
    cypher_str = str(input())
    # a_level = parse(cypher_str)
    b_level = []
    # print(a_level)
    abc = decode_instructions(cypher_str)

    print(abc)

if __name__ == '__main__':
    main()


