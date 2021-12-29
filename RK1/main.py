from operator import itemgetter


class Driver:
    """Класс Водитель"""

    def __init__(self, id, second_name, first_name, salary, carcarstation_id):
        self.id = id
        self.second_name = second_name
        self.first_name = first_name
        self.salary = salary
        self.carstation_id = carcarstation_id


class Carstation:
    """Класс Автопарк"""

    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address


class CarstationDrivers:
    """Класс Водители автопарка"""

    def __init__(self, carstation_id, driver_id):
        self.carstation_id = carstation_id
        self.driver_id = driver_id


# Автопарки
carstations = [
    Carstation(1, "Автопарк № 1", "ул. Ленина, д. 7"),
    Carstation(2, "Автопарк № 2", "Московский пр-кт, д. 35"),
    Carstation(3, "Автопарк № 3", "ул. Демченкова, д. 228"),
    Carstation(4, "AutoExpress", "Яузская наб., д. 2"),
    Carstation(5, "Aerocars", "Карачаровский пр-д, д. 54")
]

# Водители
drivers = [
    Driver(1, "Коллапсов", "Магомед", 18000000, 1),
    Driver(2, "Аверьянов", "Юрий", 75000, 2),
    Driver(3, "Пивоваров", "Роман", 67000, 4),
    Driver(4, "Болотов", "Антон", 73000.37, 3),
    Driver(5, "Абрамов", "Илья", 64999.99, 3),
    Driver(6, "Бойко", "Артём", 82000, 1),
    Driver(7, "Ангелов", "Пётр", 79000, 5)
]

# Водители автопарков
drivers_of_carstation = [
    CarstationDrivers(1, 1),
    CarstationDrivers(1, 3),
    CarstationDrivers(1, 5),
    CarstationDrivers(2, 1),
    CarstationDrivers(2, 2),
    CarstationDrivers(2, 4),
    CarstationDrivers(3, 3),
    CarstationDrivers(3, 6),
    CarstationDrivers(4, 7),
    CarstationDrivers(4, 1),
    CarstationDrivers(5, 2),
    CarstationDrivers(5, 6)
]


def main():
    # Соеденение данных один-ко-многим
    one_to_many = [(d.second_name, d.first_name, d.salary, cs.name, cs.address)
                   for cs in carstations
                   for d in drivers
                   if cs.id == d.carstation_id]

    # Соеденение данных многие-ко-многим
    many_to_many_temp = [(cs.name, cs.address, dcs.carstation_id, dcs.driver_id)
                         for cs in carstations
                         for dcs in drivers_of_carstation
                         if cs.id == dcs.carstation_id]

    many_to_many = [(d.second_name, d.first_name, d.salary, cs_name, cs_address)
                    for cs_name, cs_address, cs_id, d_id in many_to_many_temp
                    for d in drivers
                    if d_id == d.id]

    print("Задание E1")
    res1 = [(tpl[3], tpl[0:3])
            for tpl in one_to_many
            if "Автопарк" in tpl[3]]
    print(res1)

    print("Задание E2")
    res2 = []
    # Перебор всех автопарков
    for cs in carstations:
        # Список водителей автопарка
        dr_cs = list(filter(lambda i: i[3] == cs.name, one_to_many))

        if len(dr_cs) > 0:
            # Зарплаты водителей автопарка
            cs_sals = [sal for _, _, sal, _, _ in dr_cs]
            # Средняя зарплата водителей автопарка
            cs_sals_avg = round(sum(cs_sals) / len(cs_sals), 2)
            res2.append((cs.name, cs_sals_avg))
    # Сортировка списка по зарплате
    res2.sort(key=itemgetter(1))
    print(res2)

    print("Задание E3")
    res3 = list(filter(lambda sn: sn[0][0] == 'А', many_to_many))
    res3.sort()
    print(res3)


if __name__ == '__main__':
    main()