world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

world_champions['2022'] = 'Аргентина'

country = 'Италия'

for years in world_champions.keys():
    print(str(years) + ' - ' + world_champions[years])

countries = list(world_champions.values())
if country in countries:
    print('Италия cтановилась чемпионом мира по футболу в 21 веке!')
else:
    print('Италия не выигрывала чемпионат мира по футболу в 21 веке.')

