try:
    num = float(input('Enter a number: '))
    print('Good job. The entered number is: ', num)

except ValueError:
    print('This is not a number.')
