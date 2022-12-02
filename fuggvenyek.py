global pizza1[]
global ar1 = 0

def tipus():
    type = input("Kérlek add meg, milyen fajta pizzát szeretnél, a következő számok megadásával: 1 - sajtos, 2 - gombás, 3 - sonkás" )
    if type == "1":
        pizza1.append("sajtos")
        ar1 = 1000
    if type == "2":
        pizza1.append("gombás")
        ar1 = 1100
    if type == "3":
        pizza1.append("sonkás")
        ar1 = 1200
    return pizza1
    return ar1


def meret():
    size = input("Kérlek add meg, milyen méretű pizzát szeretnél, a következő számok megadásával: 1 - kicsi, 2 - normál, 3 - nagy" )
    if size == "1":
        pizza1.append("kicsi")
        ar1 = ar1 * 0.9
    if size == "2":
        pizza1.append("normál")
        ar1 = ar1 * 1
    if size == "3":
        pizza1.append("nagy")
        ar1 = ar1 * 1.1
    return pizza1
    return ar1

def feltet():
    extra = input("Kérsz extra feltétet? Kérlek válaszolj a következő két betű valamelyikével: i - igen, n - nem")
    if extra == "i":
        pizza1.append("extra feltéttel")
        ar1 = ar1 + 50
    if extra == "n":
        pizza1.append("extra feltét nélkül")
        ar1 = ar1 + 0
    return pizza1
    return ar1

