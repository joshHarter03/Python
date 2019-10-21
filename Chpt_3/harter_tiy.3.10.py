countries = ['canada','america','mexico']
print(countries[0])
print(countries[1])
print(countries[2])
countries[0]='france'
print(countries)
countries.insert(1,'australia')
print(countries)
countries.append('uk')
print(countries)
print(sorted(countries))
countries.sort(reverse=True)
print(countries)
poppedcountries=countries.pop(-1)
print(f'{poppedcountries} is a pretty cool place')
del countries[0]
del countries[0]
del countries[0]
del countries[0]
print(countries)
