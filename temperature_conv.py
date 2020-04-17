#Python program that will convert temperatures back and forth from the Celsius and Fahrenheit.

# (10°C × 9/5) + 32 = 50°F -------- Celcius to Fahrenheit
# (50°F − 32) × 5/9 = 10°C -------- Fahrenheit to Celcius

temp= input('Input temperature is in cel or far?: ')
if temp=='cel':
    temp_C=float(input('Enter temperature in Celcius: '))
    temp_F= (temp_C*9/5) +32
    print(f'{temp_C} ℃ is {round(temp_F,2)} °F')
    temp_f = float(input('Enter temperature in Fahrenheit: '))
    temp_c = (temp_f-32) * 5/9
    print(f'{temp_f} °F is {round(temp_c,2)} ℃')
elif temp=='far':
    temp_F = float(input('Enter temperature in Fahrenheit: '))
    temp_C = (temp_F-32)*5/9
    print(f'{temp_F} °F is {round(temp_C,2)} ℃')
    temp_c = float(input('Enter temperature in Celcius: '))
    temp_f = (temp_c * 9 / 5) + 32
    print(f'{temp_c} °C is {round(temp_f,2)} °F')
else:
    print('unknown input')
