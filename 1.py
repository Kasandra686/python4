from sys import argv

try:
    script_name, hour, salary, prize = argv
    result = (int(hour) * int(salary)) + int(prize)
    print(result)
except ValueError:
    print("Необходимо вводить три числа!")
