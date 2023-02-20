# imports
import math

# inputs
steps_amount = int(input())
computer_1 = input().split(' - ')
computer_2 = input().split(' - ')

# calculation for computer 1
time_computer_1 = 0.0

if computer_1[3] == '2n^2':
    time_computer_1 = (2 * (steps_amount ** 2)) / int(computer_1[1])
elif computer_1[3] == 'n.logn':
    time_computer_1 = (steps_amount * math.log10(steps_amount)
                       ) / int(computer_1[1])
elif computer_1[3] == '2^n':
    time_computer_1 = (2 ** steps_amount) / int(computer_1[1])
elif computer_1[3] == 'n':
    time_computer_1 = steps_amount / int(computer_1[1])

# calculation for computer 2
time_computer_2 = 0.0

if computer_2[3] == '2n^2':
    time_computer_2 = (2 * (steps_amount ** 2)) / int(computer_2[1])
elif computer_2[3] == 'n.logn':
    time_computer_2 = (steps_amount * math.log10(steps_amount)
                       ) / int(computer_2[1])
elif computer_2[3] == '2^n':
    time_computer_2 = (2 ** steps_amount) / int(computer_2[1])
elif computer_2[3] == 'n':
    time_computer_2 = steps_amount / int(computer_2[1])

# outputs

print(f'Velocidade do {computer_1[0]}: {time_computer_1:,.2f} segundos')
print(f'Velocidade do {computer_2[0]}: {time_computer_2:,.2f} segundos')
if time_computer_1 > time_computer_2:
    print(f'O {computer_2[0]} foi mais rápido!')
else:
    print(f'O {computer_1[0]} foi mais rápido!')
