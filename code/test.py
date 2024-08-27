import datetime
dato = datetime.datetime.now().isoformat()
print(dato[0:11])
dato1 = dato[0:11] + "00:00:00"

print(dato1)


"2024-08-26T00:00:00"