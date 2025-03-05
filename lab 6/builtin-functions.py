import math
import time

def mul_list(nums):
    return math.prod(nums)

def count_case(s):
    u = sum(1 for c in s if c.isupper())
    l = sum(1 for c in s if c.islower())
    return u, l

def is_palin(s):
    return s == s[::-1]

def sqrt_after_ms():
    x = int(input().strip())
    ms = int(input().strip())
    time.sleep(ms / 1000)
    print(f"Square root of {x} after {ms} milliseconds is {math.sqrt(x)}")

def all_true(t):
    return all(t)

 # Тест
if __name__ == "__main__":
    print("1) mul_list:", mul_list([2, 3, 4]))
    up, low = count_case("Hello World!")
    print("2) count_case: Upper =", up, ", Lower =", low)
    print("3) is_palin('racecar'):", is_palin("racecar"))
    sqrt_after_ms()
    print("5) all_true((True, 1, 'ok')):", all_true((True, 1, "ok")))
    print("5) all_true((True, 0, 'no')):", all_true((True, 0, "no")))
