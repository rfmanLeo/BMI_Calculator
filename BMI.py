height = input('Please enter your height(cm): ')
weight = input('Please enter your weight(kg): ')
height = float(height)
weight = float(weight)

height = height / 100
bmi = weight/(height**2)

print('Your BMI is', bmi)
if bmi < 18.5:
	print('You are underweight')

elif 18.5 <= bmi < 24.9:
	print('You are normalweight')

elif 25 <= bmi < 29.9:
	print('You are overweight')

elif 30 < bmi:
	print('You are obese')