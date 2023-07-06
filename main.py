# CLASS WORK TASK

age = int(input("Введіть ваш вік: "))
income = int(input("Введіть ваш річний дохід (в долараx): "))


if 18 <= age <= 25 and income <= 20000:
    category = "Студенський кредит"
    max_credit = income * age / 4
    round(max_credit, 0)
elif 26 <= age <= 40 and 20000 < income <=40000:
    category = "Особистий кредит"
    max_credit = income * age / 4
    round(max_credit, 0)
elif 41 <= age <= 60 and income > 40000:
    category = "Поточний кредит"
    max_credit = income * age / 4
    round(max_credit, 0)
else:
    category = "Недопустимий кредит"
    max_credit = 0
print("Вам надано: ", category)
print("Максимальний допустимий кредит: ", max_credit)

friend = bool(input("Чи приводили ви друзів(True or False)? "))

credit_time = int(input("Введіть час для сплати кредиту (місяці мін.:12 макс.:24): "))
if 12 <= credit_time <= 24:
    credit_amount = int(input("Введіть суму кредиту: "))
    if friend:
        if credit_amount <= max_credit:
            credit_per_month = (credit_amount / credit_time) + (credit_amount/100*1.5)
            all_credit = credit_per_month * credit_time
        else:
            print("Вибрана сума за велика!")
    else:
        if credit_amount <= max_credit:
            credit_per_month = (credit_amount / credit_time) + (credit_amount/100*2)
            all_credit = credit_per_month * credit_time
        else:
            print("Вибрана сума за велика!")
elif 0 <= credit_time <12:
    print("Час для сплати кредиту не доходить мінімуму")
elif credit_time < 0:
    print("Час для сплати кредиту не доходить мінімуму")
else:
    print("Час для сплати кредиту за великий")

print("Кредитні виплати на місяць: ", round( credit_per_month, 0))
print("Виплата кредиту за термін: ", round( all_credit, 0))

# TASK №1

number1 = int(input("Введіть перше число: "))
number2 = int(input("Введіть друге число: "))
number3 = int(input("Введіть третє число: "))

product_numbers = "*"
sum_numbers = "+"
action = input("Введіть дію з числами(* або +): ")
if action == product_numbers:
    print(number1*number2*number3)
elif action == sum_numbers:
    print(number1+number2+number3)
else:
    print("Такої дії не існує!")

# TASK №2

number_one = int(input("Введіть перше число: "))
number_two = int(input("Введіть перше друге: "))
number_tree = int(input("Введіть перше третє: "))

more = ">"
less = "<"
middle_inflection = "=="
action1 = input("Виберіть дію з чисел(>, <, ==): ")

if action1 == middle_inflection:
    print((number_one + number_two + number_tree) / 3 )
elif action1 == more:
    if number_one > number_two and number_one > number_tree:
        print("Найбільше: ", number_one)
    elif number_two > number_one and number_two > number_tree:
        print("Найбільше: ", number_two)
    elif number_tree > number_one and number_tree > number_two:
        print("Найбільше: ", number_tree)
    elif number_two > number_tree and number_one > number_tree and number_two == number_one:
        print("Найбільші: ", number_one)
    elif number_tree > number_two and number_one > number_two and number_tree == number_one:
        print("Найбільші: ", number_one)
    elif number_tree > number_one and number_two > number_one and number_tree == number_two:
        print("Найбільші: ", number_two)
    elif number_tree == number_two and number_one == number_two and number_one == number_tree:
        print("Числа є рівними!")
    else:
        print("Незнаю як ти це зробив!")
elif action1 == less:
    if number_one < number_two and number_one < number_tree:
        print("Найменше: ", number_one)
    elif number_two < number_one and number_two < number_tree:
        print("Найменше: ", number_two)
    elif number_tree < number_one and number_tree < number_two:
        print("Найменше: ", number_tree)
    elif number_two < number_tree and number_one < number_tree and number_two == number_one:
        print("Найменші: ", number_one)
    elif number_tree < number_two and number_one < number_two and number_tree == number_one:
        print("Найменші: ", number_one)
    elif number_tree < number_one and number_two < number_one and number_tree == number_two:
        print("Найменші: ", number_two)
    elif number_tree == number_two and number_one == number_two and number_one == number_tree:
        print("Числа є рівними!")
    else:
        print("Незнаю як ти це зробив!")
else:
    print("Іншого варіанту немає!")

# TASK №3

meters = int(input("Введіть кількість метрів: "))
decimeters = "dm"
inches = "in"
miles = "mi"
yards = "yd"
system = input("Введіть тип розмвру(dm, in, yd, mi)")
if system == decimeters:
    print("Дециметри: ", round(meters * 10, 4))
elif system == inches:
    print("Дюйми: ", round(meters * 39.37, 4) )
elif system == yards:
    print("Ярди: ", round(meters * 1.09, 4) )
elif system == miles:
    print("Милі: ", round(meters * 0.0006, 4) )
else:
    print("Іншого варіанту вибору немає!")