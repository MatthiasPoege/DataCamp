# print desired amount of Fibunacci numbers

# Ask how many numbers
num_fibo = eval(input("How many Fibunacci numbers do you want to have: "))

# define first two numbers
num1 = 0
num2 = 1

print(num2)

for i in range(num_fibo):
    # caclulate current number
    current_num = num1 + num2
    print(current_num)
    # update numbers
    num1 = num2
    num2 = current_num
