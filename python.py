rate = float(input('what is your rate of pay?'))
hours = float(input('how many hours did you work?'))
if hours <= 37.5:
    pay = hours * rate
else:
    pay = hours*rate*1.5
print('your pay is £' + str(pay) + ' per week')

