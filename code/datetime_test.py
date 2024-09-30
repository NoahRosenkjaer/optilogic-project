import datetime
import datetime as dt


dato = datetime.datetime.now().isoformat()
print(dato[0:11])
dato1 = dato[0:11] + "00:00:00"

print(dato1)


"2024-08-26T00:00:00"

timenr = (dt.datetime.now().strftime('%H'))
dato2 = datetime.datetime.now().isoformat()
dagsdato = dt.datetime.now().strftime("%d-%m-%Y %H")

print(timenr)
print(dato2)

print("1.25", f'"{dagsdato}"')



