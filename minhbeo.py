import math
def number_breakdown(num):
    lib = {}
    x = 2
    while num > 1:
        if is_prime(x):
            a = 0
            while num % x == 0:
                num = num / x
                a += 1
                if num % x != 0:
                    lib[x] = a
        match x:
            case 2:
                x += 1
            case _:
                x += 2
    return lib





def is_prime(number):
    n = [2,3,5,7,11,13,15,17,19,23,29,31,37]
    if number not in n:
        for x in range(2, int(math.sqrt(number) + 1)):
            if number % x == 0:
                return False
    else:
        return True
    return True


if __name__ == '__main__':
    default = 1
    lst = number_breakdown(int(input()))
    print(lst)
    for x in lst:
        default = default * (lst[x] + 1)
    print(default)



