def c_to_f(c):
    return (c * 9 / 5) + 32
def f_to_c(f):
    return (f - 32) * 5 / 9
if __name__ == '__main__':
    choice = input('Convert from (C)elsius or (F)ahrenheit? ').strip().upper()
    if choice == 'C':
        c = float(input('Enter temperature in Celsius: '))
        print(f'{c}°C = {c_to_f(c):.2f}°F')
    elif choice == 'F':
        f = float(input('Enter temperature in Fahrenheit: '))
        print(f'{f}°F = {f_to_c(f):.2f}°C')
    else:
        print('Invalid choice')
