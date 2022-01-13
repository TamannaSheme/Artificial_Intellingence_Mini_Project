print('Type of Tax Category: ')
print('1-General case')
print('2-Women and Citizens whose age is greater than 65')
print('3-Disabled')
print('4-Parents of disabled')
print('5-Wounded Freedom Fighter')

# console input of option
n = int(input('Enter option : '))
# console input of income
try:
    income = int(input('Enter the income(k) : '))
except ValueError:
    print("Please Enter Appropriate Value !!")
else:
    print ('No exception occurred')

if (n == 1):
    if (income <= 300):
        tax = 0
    elif (income > 300 and income <= 400):
        tax = (income - 300) * 5 / 100
    elif (income > 400 and income <= 700):
        tax = (300 * 0 / 100) + (100 * 5 / 100) + (income - 400) * 10 / 100
    elif (income > 700 and income <= 1100):
        tax = (300 * 0 / 100) + (100 * 5 / 100) + (300 * 10 / 100) + (income - 700) * 15 / 100
    elif (income > 1100 and income <= 1600):
        tax = (300 * 0 / 100) + (100 * 5 / 100) + (300 * 10 / 100) + (400 * 15 / 100) + (income - 1100) * 20 / 100
    else:
        tax = (300 * 0 / 100) + (100 * 5 / 100) + (300 * 10 / 100) + (400 * 15 / 100) + (500 * 20 / 100) + (
                    income - 1600) * 25 / 100

elif (n == 2):
    if (income <= 350):
        tax = 0
    elif (income > 350 and income <= 450):
        tax = (income - 350) * 5 / 100
    elif (income > 450 and income <= 750):
        tax = (350 * 0 / 100) + (100 * 5 / 100) + (income - 450) * 10 / 100
    elif (income > 750 and income <= 1150):
        tax = (350 * 0 / 100) + (100 * 5 / 100) + (300 * 10 / 100) + (income - 750) * 15 / 100
    elif (income > 1150 and income <= 1650):
        tax = (350 * 0 / 100) + (100 * 5 / 100) + (300 * 10 / 100) + (400 * 15 / 100) + (income - 1150) * 20 / 100
    else:
        tax = (350 * 0 / 100) + (100 * 5 / 100) + (300 * 10 / 100) + (400 * 15 / 100) + (500 * 20 / 100) + (
                    income - 1650) * 25 / 100

elif (n == 3):
    if (income <= 450):
        tax = 0
    elif (income > 450 and income <= 550):
        tax = (income - 450) * 5 / 100
    elif (income > 550 and income <= 850):
        tax = (450 * 0 / 100) + (100 * 5 / 100) + (income - 550) * 10 / 100
    elif (income > 850 and income <= 1250):
        tax = (450 * 0 / 100) + (100 * 5 / 100) + (300 * 10 / 100) + (income - 850) * 15 / 100
    elif (income > 1250 and income <= 1750):
        tax = (450 * 0 / 100) + (100 * 5 / 100) + (300 * 10 / 100) + (400 * 15 / 100) + (income - 1250) * 20 / 100
    else:
        tax = (450 * 0 / 100) + (100 * 5 / 100) + (300 * 10 / 100) + (400 * 15 / 100) + (500 * 20 / 100) + (
                    income - 1750) * 25 / 100

elif (n == 4):
    if (income <= 350):
        tax = 0
    elif (income > 350 and income <= 450):
        tax = (income - 350) * 5 / 100
    elif (income > 450 and income <= 750):
        tax = (350 * 0 / 100) + (100 * 5 / 100) + (income - 450) * 10 / 100
    elif (income > 750 and income <= 1150):
        tax = (350 * 0 / 100) + (100 * 5 / 100) + (300 * 10 / 100) + (income - 750) * 15 / 100
    elif (income > 1150 and income <= 1650):
        tax = (350 * 0 / 100) + (100 * 5 / 100) + (300 * 10 / 100) + (400 * 15 / 100) + (income - 1150) * 20 / 100
    else:
        tax = (350 * 0 / 100) + (100 * 5 / 100) + (300 * 10 / 100) + (400 * 15 / 100) + (500 * 20 / 100) + (
                    income - 1650) * 25 / 100

elif (n == 5):
    if (income <= 475):
        tax = 0
    elif (income > 475 and income <= 575):
        tax = (income - 475) * 5 / 100
    elif (income > 575 and income <= 875):
        tax = (475 * 0 / 100) + (100 * 5 / 100) + (income - 575) * 10 / 100
    elif (income > 875 and income <= 1275):
        tax = (475 * 0 / 100) + (100 * 5 / 100) + (300 * 10 / 100) + (income - 875) * 15 / 100
    elif (income > 1275 and income <= 1775):
        tax = (475 * 0 / 100) + (100 * 5 / 100) + (300 * 10 / 100) + (400 * 15 / 100) + (income - 1275) * 20 / 100
    else:
        tax = (475 * 0 / 100) + (100 * 5 / 100) + (300 * 10 / 100) + (400 * 15 / 100) + (500 * 20 / 100) + (
                    income - 1775) * 25 / 100

print('Total Tax to Pay ', tax, 'Taka')
