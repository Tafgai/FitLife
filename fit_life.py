# Проект FitLife - MVP версия 1.0

WATER_PER_KG = 30   # стандартная величина воды в мл на 1 кг
WATER_LITR = 1000   # содержание милилитров в 1 литре по сиситеме СИ
LINE_ELEMENT = 38   # колличество элементов на печать для разделения

print("Добро пожаловать в 'FitLife MVP\'")
print("*" * LINE_ELEMENT)
# ввод данных- Имени
user_name = input("Пожалуста напишите ваше имя: ")
user_name = user_name.title()

while True:
    user_age = (input('Укажите ваш возраст(полных лет): '))
    try:
        age = int(user_age)
        break
    except ValueError:
        print("Пожалуйста пишите цифры.Например - 18,25,89")

while True:
    user_gravity = (input('Запишите ваш вес в '
                          'килограммах(указать через точку): '))
    try:
        gravity = float(user_gravity)
        break
    except ValueError:
        print("Пожалуйста пишите цифры.Например - 30 или 75.6 ")


user_height = float(input('Какой у вас рост в метрах?(указать через точку): '))

# рассчет индекса массы тела + округление индекса до десятых
bmi = round(gravity / (user_height**2), 3)
# вычесление колличество милилитров для указанного веса чела
water_ml = gravity * WATER_PER_KG
water_l = round(water_ml / WATER_LITR, 2)       # перевод мили в литры

print()
print(f"Отчет для пользователя: {user_name} ({user_age} г.) ")
print("=" * LINE_ELEMENT)
print(f"Твой Индекс Массы Тела: {bmi}")
print('Рекомендуемая норма воды,для подержания вашего '
      f"состояния: {water_l} л. в день")
print("=" * LINE_ELEMENT)
print("Расчет окончен.Будьте здоровы!;)")
