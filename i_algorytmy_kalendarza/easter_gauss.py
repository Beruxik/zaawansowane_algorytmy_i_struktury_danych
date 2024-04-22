from datetime import datetime, timedelta

def easter_date(year):
    a = year % 19
    b = year % 4
    c = year % 7

    if year <= 1582:
        A = 15
        B = 6
    
    if 1583 <= year <= 1699:
        A = 22
        B = 2
    
    if 1700 <= year <= 1799:
        A = 23
        B = 3
    
    if 1800 <= year <= 1899:
        A = 23
        B = 4
    
    if 1900 <= year <= 2099:
        A = 24
        B = 5
    
    if 2100 <= year <= 2199:
        A = 24
        B = 6
    
    if 2200 <= year <= 2299:
        A = 25
        B = 0
    
    if 2300 <= year <= 2399:
        A = 26
        B = 1
    
    if 2400 <= year <= 2499:
        A = 25
        B = 1
    
    d = (a * 19 + A) % 30
    e = (2 * b + 4 * c + 6 * d + B) % 7

    if d == 29 and e == 6:
        days_to_easter = 28
    elif d == 28 and e == 6:
        days_to_easter = 27
    else:
        days_to_easter = d + e
    
    date_march = datetime(year, 3, 22)
    date_easter = date_march + timedelta(days=days_to_easter)

    return date_easter.strftime('%d-%m-%Y')

year = int(input('Put year: '))
print(f'Easter will be on {easter_date(year)}')