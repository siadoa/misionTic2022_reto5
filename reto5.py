import csv


def ask_cityId():
    entry = input()
    entry = entry.split(' ')
    cities = []
    for i in entry:
        cities.append(int(i))
    return sorted(cities)


def find_city(cities):
    with open('data.csv') as f:
        data = csv.DictReader(f)

        city_name = []
        city_dptm = []
        for i in cities:
            for row in data:
                if row['id_city'] == str(i):
                    city_name.append(row['city_name'])
                    city_dptm.append(row['department_name'])
                    break
    return city_name, city_dptm


def icaCalculation(c):
    if c >= 0 and c < 0.060:
        ica = ((50 - 0) / (0.059 - 0))*(c - 0) + 0
    elif c >= 0.060 and c < 0.076:
        ica = ((100 - 51) / (0.075 - 0.060))*(c - 0.060) + 51
    elif c >= 0.076 and c < 0.096:
        ica = ((150 - 101) / (0.095 - 0.076))*(c - 0.076) + 101
    elif c >= 0.096 and c < 0.116:
        ica = ((200 - 151) / (0.115 - 0.096))*(c - 0.096) + 151
    elif c >= 0.116 and c < 0.375:
        ica = ((300 - 201) / (0.374 - 0.116))*(c - 0.116) + 201
    return ica


def alertCalculation(ica):
    if ica >= 0 and ica <= 50:
        alert = 'verde'
    elif ica > 50 and ica <= 100:
        alert = 'amarillo'
    elif ica > 100 and ica <= 150:
        alert = 'naranja'
    elif ica > 150 and ica <= 200:
        alert = 'rojo'
    elif ica > 200 and ica <= 300:
        alert = 'morado'
    elif ica > 300:
        alert = 'marron'
    return alert


def meanCalculation(array):
    if array == []:
        mean = 0
    else:
        summ = 0
        for i in array:
            summ += i
        mean = summ / len(array)
    return mean


def stdCalculation(mean, array):
    std_sum = 0
    for i in array:
        std_sum += (i - mean) ** 2
    std = (std_sum / (len(array)-1)) ** 0.5
    return std


def alertCount(array):
    green = yellow = orange = red = purple = brown = 0
    for i in array:
        if i == 'verde':
            green += 1
        elif i == 'amarillo':
            yellow += 1
        elif i == 'naranja':
            orange += 1
        elif i == 'rojo':
            red += 1
        elif i == 'morado':
            purple += 1
        elif i == 'marron':
            brown += 1

    return green, yellow, orange, red, purple, brown


def execute():
    cities = ask_cityId()

    with open('data.csv') as files:
        data = csv.DictReader(files)

        c_measures = []
        icas = []
        alerts = []

        for _ in cities:
            c_measures.append([])
            icas.append([])
            alerts.append([])

        for row in data:
            for j in range(len(cities)):
                if cities[j] == int(row['id_city']):
                    measure = float(row['measurement'])
                    ica = icaCalculation(measure)
                    alert = alertCalculation(ica)
                    c_measures[j].append(measure)
                    icas[j].append(ica)
                    alerts[j].append(alert)

    for i in range(len(cities)):
        city_name = find_city(cities)[0][i]
        city_dptm = find_city(cities)[1][i]
        count = len(c_measures[i])
        c_mean = meanCalculation(c_measures[i])
        c_std = stdCalculation(c_mean, c_measures[i])
        c_min = min(c_measures[i])
        c_max = max(c_measures[i])
        ica_mean = meanCalculation(icas[i])
        ica_std = stdCalculation(ica_mean, icas[i])
        ica_min = min(icas[i])
        ica_max = max(icas[i])
        alert_count = alertCount(alerts[i])
        print(f'{cities[i]} {city_name} {city_dptm}')
        print(f'count {count}')
        print('c measurement')
        print(f'mean {c_mean:.2f}')
        print(f'std {c_std:.2f}')
        print(f'min {c_min:.2f}')
        print(f'max {c_max:.2f}')
        print('ica')
        print(f'mean {ica_mean:.2f}')
        print(f'std {ica_std:.2f}')
        print(f'min {ica_min:.2f}')
        print(f'max {ica_max:.2f}')
        print('alerts')
        print(f'verde {alert_count[0]}')
        print(f'amarillo {alert_count[1]}')
        print(f'naranja {alert_count[2]}')
        print(f'rojo {alert_count[3]}')
        print(f'morado {alert_count[4]}')
        print(f'marron {alert_count[5]}')


execute()
