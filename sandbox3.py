fib_list = []
def fib (firmware_list):
    while len(firmware_list)>0:
        a = firmware_list[0]
        b = firmware_list[1]
        fib_sum = a+b
        fib_list.append(fib_sum)
        firmware_list.pop(0)
        firmware_list.pop(1)
        fib(firmware_list)
    return fib_list



firmware: int = int(input())
firmware_list = []
for _ in range(firmware+1):
    firmware_list.append(int(_))


if  firmware_list:
    print(firmware_list)


