# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import json
import re

class ReadTxt:
    '''
    Объект класса read_txt репрезентует данные одного человека из заданного файла
    Нужен для записи из текстового файла
    '''
    Email: str
    Height: float
    Inn: str
    Passport_series: str
    Occupation: str
    Age: int
    Academic_degree: str
    Worldview: str
    Address: str

    def __init__(self, email, height, inn, passport_series, occupation, age, academic_degree, worldview, address):
        self.Email = email
        self.Height = height
        self.Inn = inn
        self.Passport_series = passport_series
        self.Occupation = occupation
        self.Age = age
        self.Academic_degree = academic_degree
        self.Worldview = worldview
        self.Address = address

    def fwrite(self, wfile):
        wfile.write('email:')
        wfile.write(self.Email)
        wfile.write('\n')
        wfile.write('height:')
        sHeight = str(self.Height)
        wfile.write(sHeight)
        wfile.write('\n')
        wfile.write('inn:')
        wfile.write(self.Inn)
        wfile.write('\n')
        wfile.write('passport_series:')
        wfile.write(self.Passport_series)
        wfile.write('\n')
        wfile.write('occupation:')
        wfile.write(self.Occupation)
        wfile.write('\n')
        wfile.write('age:')
        sAge = str(self.Age)
        wfile.write(sAge)
        wfile.write('\n')
        wfile.write('academic_degree:')
        wfile.write(self.Academic_degree)
        wfile.write('\n')
        wfile.write('worldview:')
        wfile.write(self.Worldview)
        wfile.write('\n')
        wfile.write('address:')
        wfile.write(self.Address)
        wfile.write('\n')
        wfile.write('\n')

    def print_data(self):
        print(self.Email)
        print(self.Height)
        print(self.Inn)
        print(self.Passport_series)
        print(self.Occupation)
        print(self.Age)
        print(self.Academic_degree)
        print(self.Worldview)
        print(self.Address, '\n')


class Validator:
    users_data: ReadTxt = []

    def __init__(self, users_data):
        self.users_data = users_data

    def check_email(self, email: str) -> bool:
        '''
        Выполняет проверку корректности адреса электронной почты.

        Если в строке присутствуют пробелы, запятые, двойные точки,
        а также неверно указан домен адреса, то будет возвращено False.

        Parameters
        ----------
          email : str
            Строка с проверяемым электронным адресом

        Returns
        -------
          bool:
            Булевый результат проверки на корректность
        '''
        pattern = "^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$"
        if re.match(pattern, email):
            return True
        return False

    def check_height(self, height: float):
        pattern1 = "^1\.\d{2}$"
        pattern2 = "^2\.[0-7]{1}\d{1}$"
        pattern3 = "^0\.[6-9]{1}\d{1}$"
        if re.match(pattern1, str(height)):
            return True
        if re.match(pattern2, str(height)):
            return True
        if re.match(pattern3, str(height)):
            return True
        return False

    def check_inn(self, inn: str) -> bool:
        pattern = "\d{12}"
        if re.match(pattern, str(inn)):
            return True
        return False

    def check_passport_series(self, passport_series: str) -> bool:
        pattern = "\d{2}\s\d{2}"
        if re.match(pattern, str(passport_series)):
            return True
        return False

    def check_occupation(self, occupation: str) -> bool:
        pattern1 = "Мерчендайзер|Окулист|Пожарный|Диктор|Дегустатор|Прозектор|Повар|Диджей|Супервайзер|Редактор|Кинолог"
        pattern2 = "Преподаватель|Флорист|Билетный кассир|Официант|Рыбак|Промышленный альпинист|Бренд-менеджер|Грузчик"
        pattern3 = "Монтажник|Web-дизайнер|Сапожник|Ювелир|Реставратор|Гинеколог|Менеджер по продажам"
        pattern4 = "Секретарь-стенографистка|Писатель|Оператор call-центра|Бригадир железнодорожного пути|Психолог"
        pattern5 = "Маркетолог|Контент-менеджер|Банковский кассир-операционист|Венеролог|Политолог|Шлифовщик|Религиовед"
        pattern6 = "Продавец-консультант|Кондитер|Бондарь|Педиатр|Агент по туризму|Изобретатель|Проходчик|Фальцовщик"
        pattern7 = "Проктолог|Ассистент менеджера по продажам|Фотомодель|Реабилитолог|Web-интегратор"
        pattern8 = "Менеджер по закупкам|Журналист|Оператор машинного доения|Бортмеханик|Слесарь|Востоковед"
        pattern9 = "Мусоропроводчик|Главный конструктор|Сценарист|Художник|Инфекционист|Врач скорой помощи|Уролог"
        pattern10 = "Электромонтажник|Бизнес-консультант|Бульдозерист|Нефролог|Телохранитель|Дизайнер-модельер"
        pattern11 = "Крановщик|Штукатур|Геодезист|Кладовщик|Нанотехнолог|Вирусолог|Тестировщик|Экономист|Месильщик"
        pattern12 = "Стоматолог|Финансовый аналитик|Охранник|Фрезеровщик|Бортпроводник|Автомеханик|Комбайнер|Литейщик"
        pattern13 = "Иллюстратор|Постановщик трюков|Тележурналист|Медицинская сестра|Композитор|Детектив|Киномеханик"
        pattern14 = "Дерматовенеролог|Сварщик|Пастух|Мастер|Мультипликатор|Маклер|Лингвист|Животновод|Кассир|Брокер"
        pattern15 = "Менеджер по логистике|Библиограф|Кинодраматург|Маникюрша|Бухгалтер|Технолог|Конструктор"
        pattern16 = "Консультант по туризму|Бармен|Винодел|Художник по костюму|Учитель|Космонавт"
        pattern17 = "Специалист по стрижке овец|Инженер-конструктор|Терапевт|Дипломат|Спортивный врач|Психиатр"
        pattern18 = "Администратор гостиницы|Биоинженер|Режиссер|Главный технолог|Педагог|Лаборант|Сексолог|Ортопед"
        pattern19 = "Адвокат|Швея|Секретарь-референт|Генный инженер|Плотник|Бизнес-аналитик|Зоолог|Металлург"
        pattern20 = "Тюремный надзиратель|Менеджер по работе с клиентами|Оториноларинголог|Системный администратор"
        pattern21 = "Реаниматолог|Шеф-повар|Следователь|Модель|Массажист|Химик|Охотник|Закройщик|Акушер|Бренд-дизайнер"
        pattern22 = "Аудитор|Уборщица|Автослесарь|Сталевар|Радиомеханик|Косметолог|Летчик|Лоббист|Таксист|Хореограф"
        pattern23 = "Садовник|Стрелочник|Шахтер|HTML-верстальщик|Историк|Заведующий складом|Риелтор|Водитель|Статистик"
        pattern24 = "Капитан судна|Мусорщик|Тифлопедагог|Фотограф|Токарь|Манекенщица|Диспетчер|Правовед|Банкир|Биохимик"
        pattern25 = "Администратор ресторана|Каменщик|Штурман|Типограф|Дизайнер|Нотариус|Программист|Оценщик|Электрик"
        pattern26 = "Администратор базы данных|Матрос|Оператор ПКЛандшафтный дизайнер|Метеоролог|Спортивный тренер"
        pattern27 = "Офтальмолог|Ботаник|Менеджер по рекламе|Артист цирка|Библиотекарь|Специалист по ВЭД|Каскадер"
        pattern28 = "Сантехник|Анестезиолог|Инкассатор|Отделочник|Проводник|Печатник|Конвоир|Кардиохирург|Генетик"
        pattern29 = "Авиадиспетчер|Логист|Дистрибутор|Копирайтер|Референт|Кровельщик|Главный инженер|Философ"
        pattern30 = "Палеонтолог|Невролог|Пекарь|Цветочница|Строитель|Торговый представитель|Дизайнер рекламы|Геолог"
        pattern31 = "Стюардесса|Картограф|Микробиолог|Инженер|Столяр|Менеджер по PR|Бортинженер|Кинооператор|Астроном"
        pattern32 = "Почтальон|Краснодеревщик|Горняк|Дирижер|Менеджер торгового зала|Выпускающий редактор|Звукооператор"
        pattern33 = "Хирург|Визажист|Товаровед|Судебный пристав|Скотник|Судья|Финансист|Фермер|Воздухоплаватель"
        pattern34 = "Мануалист|Налоговый инспектор|Машинист|Критик|Водолаз|Энергетик|Эндокринолог|Биофизик|Физик|Радист"
        pattern35 = "Моряк|Татуировщик|Гидролог|Кинорежиссер|Социолог|Кардиолог|Нейрохирург|Почвовед|Ремонтник"
        pattern36 = "Архитектор-проектировщик|Аппаратчик-оператор|Ихтиолог|Настройщик музыкальных инструментов"
        pattern37 = "Иммунолог|Менеджер|Священнослужитель|Ветеринар|Облицовщик|Издатель|Автогонщик|Министр|Стилист"
        pattern38 = "Невропатолог|Архивариус|Проректор|Дорожный инспектор|Портной|Переплетчик|Экспедитор"
        pattern39 = "Консультант телефона доверия|Врач-диетолог|Администратор предприятия торговли|Инженер-химик|Эколог"
        pattern40 = "Машинистка|Агроном|Юрист|Геоэколог|Дерматолог|Продавец|Прокурор|Тракторист|Теолог|Инженер-технолог"
        pattern41 = "Переводчик|Медиа-байер|Корректор|Маляр|Этнограф|Web-программист|Имиджмейкер|Администратор сайта"
        pattern42 = "Рихтовщик|Холодильщик|Делопроизводитель|Искусствовед|Офис-менеджер|Логопед|Монах|Зубной техник"
        pattern43 = "Слесарь-механик|Наладчик|Психотерапевт|Андролог|Трейдер|Фармацевт|Балетмейстер|Скульптор"
        pattern44 = "Звукорежиссер|Вышивальщица|Культуролог|Химик-технолог|Промоутер|Парикмахер|Доярка|Травматолог"
        pattern45 = "Археолог|Моторист|Дворник|Снабженец|Упаковщик|Сурдопедагог|Менеджер по персоналу|Испытатель"
        pattern46 = "Верстальщик|Менеджер по туризму|Токсиколог|Страховой агент|Ректор|Кризис-менеджер|Курьер"
        pattern47 = "Технический писатель|Маркшейдер|Актер|Дефектолог|Биолог|Мясник|Спичрайтер|Продюсер|Диетолог"
        pattern48 = "Булочник|Полицейский|Архитектор|Администратор салона красоты|Драпировщик|Пчеловод|Бизнес-тренер"
        pattern49 = "Прораб|Телеграфист|Музыкант|Гид-переводчик|Сметчик|Аниматор|Онколог|Фельдшер|Орнитолог|Спортсмен"
        if re.match(pattern1, occupation):
            return True
        if re.match(pattern2, occupation):
            return True
        if re.match(pattern3, occupation):
            return True
        if re.match(pattern4, occupation):
            return True
        if re.match(pattern5, occupation):
            return True
        if re.match(pattern6, occupation):
            return True
        if re.match(pattern7, occupation):
            return True
        if re.match(pattern8, occupation):
            return True
        if re.match(pattern9, occupation):
            return True
        if re.match(pattern10, occupation):
            return True
        if re.match(pattern11, occupation):
            return True
        if re.match(pattern12, occupation):
            return True
        if re.match(pattern13, occupation):
            return True
        if re.match(pattern14, occupation):
            return True
        if re.match(pattern15, occupation):
            return True
        if re.match(pattern16, occupation):
            return True
        if re.match(pattern17, occupation):
            return True
        if re.match(pattern18, occupation):
            return True
        if re.match(pattern19, occupation):
            return True
        if re.match(pattern20, occupation):
            return True
        if re.match(pattern21, occupation):
            return True
        if re.match(pattern22, occupation):
            return True
        if re.match(pattern23, occupation):
            return True
        if re.match(pattern24, occupation):
            return True
        if re.match(pattern25, occupation):
            return True
        if re.match(pattern26, occupation):
            return True
        if re.match(pattern27, occupation):
            return True
        if re.match(pattern28, occupation):
            return True
        if re.match(pattern29, occupation):
            return True
        if re.match(pattern30, occupation):
            return True
        if re.match(pattern31, occupation):
            return True
        if re.match(pattern32, occupation):
            return True
        if re.match(pattern33, occupation):
            return True
        if re.match(pattern34, occupation):
            return True
        if re.match(pattern35, occupation):
            return True
        if re.match(pattern36, occupation):
            return True
        if re.match(pattern37, occupation):
            return True
        if re.match(pattern38, occupation):
            return True
        if re.match(pattern39, occupation):
            return True
        if re.match(pattern40, occupation):
            return True
        if re.match(pattern41, occupation):
            return True
        if re.match(pattern42, occupation):
            return True
        if re.match(pattern43, occupation):
            return True
        if re.match(pattern44, occupation):
            return True
        if re.match(pattern45, occupation):
            return True
        if re.match(pattern46, occupation):
            return True
        if re.match(pattern47, occupation):
            return True
        if re.match(pattern48, occupation):
            return True
        if re.match(pattern49, occupation):
            return True


    def check_age(self, age: int) -> bool:
        pattern1 = "\d{1,2}"
        pattern2 = "1[0-2]{1}\d{1}"
        if re.match(pattern1, str(age)):
            return True
        if re.match(pattern2, str(age)):
            return True
        return False

    def check_academic_degree(self, academic_degree: str) -> bool:
        pattern = "Бакалавр|Кандидат наук|Магистр|Специалист|Доктор наук"
        if re.match(pattern, academic_degree):
            return True
        return False

    def check_worldview(self, worldview: str) -> bool:
        pattern = "Секулярный гуманизм|Агностицизм|Иудаизм|Пантеизм|Католицизм|Конфуцианство|Деизм|Атеизм|Буддизм"
        if re.match(pattern, worldview):
            return True
        return False

    def check_address(self, address: str) -> bool:
        pattern1 = "^(ул\.\s){1}([А-ЯЁ]{1}[а-яё]+\s)+(\d\-я\s){0,1}(\d+)$"
        pattern2 = "^(Аллея\s){1}([А-ЯЁ]{1}[а-яё]+\s)+(\d\-я\s){0,1}(\d+)$"
        if re.match(pattern1, address) or re.match(pattern2, address):
            return True
        return False



rpath = 'C:\\Lab_2\\23.txt'
wpath = 'C:\\Lab_2\\23valid.txt'
data_list_of_dict = json.load(open(rpath))
users_list = []
occupation_list = []
worldview_list = []
email_flag:bool = False
height_flag:bool = False
inn_flag:bool = False
passport_series_flag:bool = False
occupation_flag:bool = False
age_flag:bool = False
academic_degree_flag:bool = False
worldview_flag:bool = False
address_flag:bool = False
email_counter:int = 0
height_counter:int = 0
inn_counter:int = 0
passport_series_counter:int = 0
occupation_counter:int = 0
age_counter:int = 0
academic_degree_counter:int = 0
worldview_counter:int = 0
address_counter:int = 0
valid_counter:int = 0
for i in data_list_of_dict:
    users_list.append(ReadTxt(i['email'], i['height'], i['inn'], i['passport_series'], i['occupation'], i['age'], i['academic_degree'], i['worldview'], i['address']))
validator = Validator(users_list)
wfile = open(wpath, 'w')
for i in range(len(users_list)):

    for j in worldview_list:
        if validator.users_data[i].Worldview == j:
            worldview_flag = True
    if not worldview_flag:
        worldview_list.append(validator.users_data[i].Worldview)

    if validator.check_email(validator.users_data[i].Email):    # check email
        email_flag = True
    else:
        email_counter += 1

    if validator.check_height(validator.users_data[i].Height):    # check height
        height_flag = True
    else:
        height_counter += 1

    if validator.check_inn(validator.users_data[i].Inn):    # check inn
        inn_flag = True
    else:
        inn_counter += 1

    if validator.check_passport_series(validator.users_data[i].Passport_series):    # check passport series
        passport_series_flag = True
    else:
        passport_series_counter += 1

    if validator.check_occupation(validator.users_data[i].Occupation):  # check occupation
        occupation_flag = True
    else:
        occupation_counter += 1

    if validator.check_age(validator.users_data[i].Age):    # check age
        age_flag = True
    else:
        age_counter += 1

    if validator.check_academic_degree(validator.users_data[i].Academic_degree):  # check academic degree
        academic_degree_flag = True
    else:
        academic_degree_counter += 1

    if validator.check_worldview(validator.users_data[i].Worldview):  # check worldview
        worldview_flag = True
    else:
        worldview_counter += 1

    if validator.check_address(validator.users_data[i].Address):  # check address
        address_flag = True
    else:
        address_counter += 1

    if email_flag and height_flag and inn_flag and passport_series_flag and occupation_flag and age_flag and academic_degree_flag and worldview_flag and address_flag:
        validator.users_data[i].fwrite(wfile)
        valid_counter += 1
    email_flag: bool = False
    height_flag: bool = False
    inn_flag: bool = False
    passport_series_flag: bool = False
    occupation_flag: bool = False
    age_flag: bool = False
    academic_degree_flag: bool = False
    worldview_flag: bool = False
    address_flag: bool = False

print("count of valid data:", valid_counter, "\nfalse mail:", email_counter, "\nfalse height:", height_counter,
      "\nfalse inn:", inn_counter, "\nfalse passport series:", passport_series_counter, "\nfalse occupation:",
      occupation_counter, "\nfalse age:", age_counter, "\nfalse academic degree:", academic_degree_counter,
      "\nfalse worldview:", worldview_counter, "\nfalse address:", address_counter)

print("\n", worldview_list)
print("\n", len(worldview_list))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
