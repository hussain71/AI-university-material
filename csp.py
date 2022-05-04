conf = 1

def getnum(s, my_map):
    num = ''
    for i in s:
        num += str(my_map[i])
    return int(num)

def my_fun(s1, s2, s3, my_map, uniq_str, idx, used_nums):
    if (idx == len(uniq_str)):
        num1 = getnum(s1, my_map)
        num2 = getnum(s2, my_map)
        num3 = getnum(s3, my_map)
        if (num1 + num2 == num3):
            global conf
            print('Possiblity : ' + str(conf))
            print()
            conf += 1
            print('\t', end='')
            for i in s1:
                print(f'{i}({my_map[i]}) ', end='')
            print()
            print('+\t', end='')
            for i in s2:
                print(f'{i}({my_map[i]}) ', end='')
            print()
            print('--------------------------------')
            print('   ', end='')
            for i in s3:
                print(f'{i}({my_map[i]}) ', end='')
            print()
            print('--------------------------------')
            print()
        return

    ch = uniq_str[idx]
    for i in range(0, 10):
        if (used_nums[i] == 0):
            my_map[ch] = i
            used_nums[i] = 1
            my_fun(s1, s2, s3, my_map, uniq_str, idx + 1, used_nums)
            my_map[ch] = -1
            used_nums[i] = 0

print()
s1 = input("Enter String 1 : ")
s2 = input("Enter String 2 : ")
s3 = input("Enter String 3 : ")

print()

my_set = set(s1 + s2 + s3)

if (len(set(my_set)) > 10):
    print("Only 10 Unique Letters Are Allowed")
    exit()

my_map = dict.fromkeys(my_set, -1)
uniq_str = ""
for i in my_set:
    uniq_str += i
idx = 0
used_nums = [0] * 10

my_fun(s1, s2, s3, my_map, uniq_str, idx, used_nums)
