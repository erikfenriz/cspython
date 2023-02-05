data = []
selected_year_data = []
max_life_data = None
min_life_data = None
year = 0

with open('life-expectancy.csv', 'r', newline='') as raw_data:
    next(raw_data)
    max_life = 0
    min_life = float('inf')
    for row in raw_data:
        entity = row.strip().split(',')
        data.append(entity)
        rate = float(entity[3])
        if(rate > max_life):
            max_life = rate
            max_life_data = entity
        if(rate < min_life):
            min_life = rate
            min_life_data = entity

while True:
    try:
        year = int(input("Enter the year of interest: "))
    except ValueError:
        print("Please, enter a valid year")
        continue
    else:
        break

for entity in data:
    if(int(entity[2]) == year):
        selected_year_data.append(float(entity[3]))

print(f'The overall max life expectancy is: {max_life_data[3]} from {max_life_data[0]} in {max_life_data[2]}')
print(f'The overall min life expectancy is: {min_life_data[3]} from {min_life_data[0]} in {min_life_data[2]}\n')
if(len(selected_year_data) != 0):
    print(f'For the year {year}:')
    print(f'The average life expectancy across all countries was {round(sum(selected_year_data) / len(selected_year_data), 2)}')
    print(f'The max life expectancy was in Norway with {max(selected_year_data)}')
    print(f'The min life expectancy was in Mali with {min(selected_year_data)}')
else:
    print('No data found for selected year')