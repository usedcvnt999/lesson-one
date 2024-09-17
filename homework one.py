
expenses_mon = float(input("Расходы за понедельник:"))
expenses_tue = float(input("Расходы за вторник:"))
expenses_wed = float(input("Расходы за среду:"))
expenses_thu = float(input("Расходы за четверг:"))
expenses_fri = float(input("Расходы за пятницу:"))
expenses_sat = float(input("Расходы за субботу:"))
expenses_sun = float(input("Расходы за воскресенье:"))
overall = expenses_mon + expenses_tue + expenses_wed + expenses_thu + expenses_fri + expenses_sat + expenses_sun
avarage = (expenses_mon + expenses_tue + expenses_wed + expenses_thu + expenses_fri + expenses_sat + expenses_sun) / 7
print("Расходы за всю неделю составили:", overall, "\nВ среднем за день тратили:", round(avarage, 1))
