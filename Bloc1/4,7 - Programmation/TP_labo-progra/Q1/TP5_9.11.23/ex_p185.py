def is_year_leap(n):
    if n % 4 == 0 and n % 100 != 0:  # si l'année est divisible par 4 mais pas par 100
        return True
    elif n % 400 == 0:  # si elle est divisible par 400
        return True
    else:  # dans tous les autres cas, l'année n'est pas bissextile
        return False


def days_in_month(year, month):
    print(year, month)


test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]


for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end=" ")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("KO")
