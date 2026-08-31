# Проект FitLife - MVP версия 1.0
WATER_PER_KG = 30   # стандартная величина воды в мл на 1 кг
WATER_LITR = 1000   # содержание милилитров в 1 литре по сиситеме СИ


print("Добро пожаловать в 'FitLife MVP\'")   #приветствие пользователя
print("*"*38)

user_name = input("Пожалуста напишите ваше имя: ")  #ввод данных- Имени
user_name = user_name.title()

try:
    user_age = int(input('Укажите ваш возраст(полных лет): '))  
except ValueError:
    print("Пожалуйста пишите цифры.")
    user_age = int(input('Укажите ваш возраст(полных лет): '))
      
try:      
    user_gravity = float(input('Запишите ваш вес в килограммах(указать через точку): '))
except ValueError:
    print("Пожалуйста пишите цифры.") 
    user_gravity = float(input('Запишите ваш вес в килограммах(указать через точку): '))
      
user_height = float(input('Какой у вас рост в метрах?(указать через точку): '))
bmi = user_gravity/(user_height**2)            #рассчет индекса массы тела 
bmi = round(bmi,1)                              #округление индекса до десятых

water_ml = user_gravity * WATER_PER_KG               #вычесление колличества милилитров для указанного веса чела
water_l = water_ml / WATER_LITR                  #перевод мили в литры
water_l = round(water_l,1)                    #округление бухалово воды до 2 знаков после запятой    полп
 
print()
print(f"Отчет для пользователя: {user_name} ({user_age} г.) ")
print("="*38)
print(f"Твой Индекс Массы Тела: {bmi}")     
print(f"Рекомендуемая норма воды,для подержания вашего состояния: {water_l:.1f} л. в день")
print("="*38)
print ("Расчет окончен. Будьте здоровы!;)")