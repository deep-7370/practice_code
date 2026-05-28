def lcm(num1, num2):
    max_num = max(num1, num2)
    while True:
        if max_num % num1 == 0 and max_num % num2 == 0:
            return max_num
        max_num += 1

print(lcm(12, 18))
