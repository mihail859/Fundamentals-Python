year = int(input())
years_start = year + 1

years_start_as_str = str(years_start)

while len(years_start_as_str) != len(set(years_start_as_str)):
    years_start += 1
    years_start_as_str = str(years_start)

else:
    print("{}".format(years_start))