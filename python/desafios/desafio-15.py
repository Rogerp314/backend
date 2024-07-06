cel = float(input('Qual a temperatura em °C: '))
kelvin = cel + 273
faren = (cel * 9/5) + 32
print('{:.2f}°C vale {:.2f}K e {:.2f}°F'.format(cel, kelvin, faren))