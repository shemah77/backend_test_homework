fib_list = [1,1]
def fib (firmware_list):
    global fib_list
    if len(firmware_list) < 1 :
        return fib_list
    else:
        fib_list.append(fib_list[-2]+fib_list[-1])
        firmware_list.pop(0)
    return fib(firmware_list)




if __name__ == '__main__':
    firmware: int = int(input())
    firmware_list = []
    for _ in range(firmware + 1):
        firmware_list.append(int(_))
    # print(firmware_list)
    if firmware == 0 or firmware == 1:
        print (1)
    else:
        fib(firmware_list)
        print (fib_list[-3])
