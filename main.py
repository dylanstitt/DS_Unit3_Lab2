# Dylan Stitt
# Unit 3 Lab 2
# n Factorial

def forFactorial(n):
    nums = []
    for i in range(1, n+1):
        nums.append(i)

    ans = nums[0]
    for i in nums[1:]:
        ans *= i
    return ans, "For Factorial"

def whileFactorial(n):
    nums = []
    while n > 0:
        nums.append(n)
        n -= 1

    ans = nums[-1]
    count = 0
    while count < len(nums)-1:
        ans *= nums[count]
        count += 1
    return ans, "While Factorial"

def recursiveFactorial(n):
    if n == 0:
        return 1

    val = recursiveFactorial(n-1)
    return n*val

def main():
    number = 4
    nums = [str(i+1) for i in range(number)][::-1]
    for i in [forFactorial(number), whileFactorial(number)]:
        print(f'Solving for {number}!')
        print(f'{"*".join(nums)} = {i[0]}')
        print(f"Found using the {i[1]}", end='\n--------------------\n')

    r = recursiveFactorial(number)
    print(f'Solving for {number}!')
    print(f'{"*".join(nums)} = {r}')
    print("Found using the Recursive Factorial", end='\n\n')

if __name__ == '__main__':
    main()
