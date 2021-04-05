x_km = int(input("Type start km for sportsmen: "))
y_km = int(input("Type some goal km for sportsmen: "))
day = 1

while x_km < y_km:
    x_km *= 1.1
    day += 1

print("Days he need:", day)
