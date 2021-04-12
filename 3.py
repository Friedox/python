percent = int(input("Введите число: "))
if 1 < percent < 5:
    print(percent, "процента")
elif percent == 1:
    print(percent, "процент")
elif 4 < percent < 20 or percent == 0:
    print(percent, "процентов")
else:
    print("число не соответствует условию задачи")
