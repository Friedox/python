duration = int(input("Введите числовое значение в секундах: "))
a = []

a.append(duration % 60)
a.append("sec")
duration -= duration % 60
a.append((duration % 3600) // 60)
a.append("min")
duration -= duration % 3600
a.append((duration // 3600) % 24)
a.append("hour")
duration -= duration // 3600
a.append((duration // 86400) % 7)
a.append("day")
duration -= duration // 86400
a.append((duration // 604800) % 4)
a.append("week")
duration -= duration // 604800
a.append((duration // 2629743) % 12)
a.append("month")
duration -= duration // 2629743
a.append(duration // 31556926)
a.append("year")


print(*a)
