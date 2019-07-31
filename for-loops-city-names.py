citiesList = ['los angeles', 'denver', 'boston', 'helsinki', 'berlin']

for city in citiesList:
    #print (city)
    #capitalizedCity = city.capitalize()
    #print(capitalizedCity)
    if (city == 'denver' or city == 'boston'):
        capitalizedCity = city.capitalize()
        print(capitalizedCity)
    else:
        print('not denver or boston')