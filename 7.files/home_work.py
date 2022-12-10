
class Homework:
    def __init__(self, cook_book_file=None):
        self.cook_book = {}


    """
    Должен получится следующий словарь

    cook_book = {
        'Омлет': [
            {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
            {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
            {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
            ],
        'Утка по-пекински': [
            {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
            {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
            {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
            {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
            ],
        'Запеченный картофель': [
            {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
            {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
            {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
            ]
    }
    """

    def read_cookbook_from_file(self, filename=None):
        cook_book = {}
        with open(filename, encoding="utf8") as file:
            for line in file:
                line = line.strip()
                if line.rfind("|") < 0 and not line.isdigit() and line != '':
                    item = line
                    cook_book[item] = []
                elif line.rfind('|') > 0:
                    ingredient_dict = line.split(' | ')
                    cook_book[item].append({
                        'ingredient_name': ingredient_dict[0],
                        'quantity': int(ingredient_dict[1]),
                        'measure': ingredient_dict[2]
                    })
        self.cook_book = cook_book
        return cook_book

    """
    Задача №2
    Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить
        get_shop_list_by_dishes(dishes, person_count)
    На выходе мы должны получить словарь с названием ингредиентов и его количества для блюда. Например, для такого вызова
        get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
    Должен быть следующий результат:
        {
            'Картофель': {'measure': 'кг', 'quantity': 2},
            'Молоко': {'measure': 'мл', 'quantity': 200},
            'Помидор': {'measure': 'шт', 'quantity': 4},
            'Сыр гауда': {'measure': 'г', 'quantity': 200},
            'Яйцо': {'measure': 'шт', 'quantity': 4},
            'Чеснок': {'measure': 'зубч', 'quantity': 6}
        }
    Обратите внимание, что ингредиенты могут повторяться
    """

    def get_shop_list_by_dishes(self, dishes, person_count: int):
        output = {}
        for dish in dishes:
            for item in self.cook_book.get(dish):
                if output.get(item['ingredient_name']) is None:
                    output[item['ingredient_name']] = {'measure': item['measure'],
                                                       'quantity': item['quantity'] * person_count
                                                       }
                else:

                    output[item['ingredient_name']] = {'measure': item['measure'],
                                                       'quantity': int(
                                                           output[item['ingredient_name']].get('quantity')) +
                                                                   int(item['quantity']) * person_count
                                                       }
        return output
    """
    В папке лежит некоторое количество файлов. Считайте, что их количество и имена вам заранее известны, пример для выполнения домашней работы можно взять тут
    Необходимо объединить их в один по следующим правилам:
        1.  Содержимое исходных файлов в результирующем файле должно быть отсортировано по количеству строк в них (то есть первым нужно записать файл с наименьшим количеством строк, а последним - с наибольшим)
        2.  Содержимое файла должно предваряться служебной информацией на 2-х строках: имя файла и количество строк в нем
    
    Пример Даны файлы: 
    1.txt
        Строка номер 1 файла номер 1
        Строка номер 2 файла номер 1
    2.txt
        Строка номер 1 файла номер 2
    
    Итоговый файл:
        2.txt
        1
        Строка номер 1 файла номер 2
        1.txt
        2
        Строка номер 1 файла номер 1
        Строка номер 2 файла номер 1
    """
    def join_in_advance(self, files: dict, output_file=None):
        file_chart = []
        for filename in files:
            with open(filename, encoding="utf8") as file:
                text = file.readlines()
                file_chart.append((filename,len(text),text))

        with open(output_file,'w',encoding='utf8') as out_file:
            for file in sorted(file_chart, key=lambda file_: file_[1]):
                out_file.write(str(file[0])+ '\n')
                out_file.write(str(file[1])+ '\n')
                out_file.writelines(file[2])
                out_file.write('\n')



if __name__ == "__main__":
    homework = Homework()
    #print("Задача №1:")
    #print(homework.read_cookbook_from_file('recipes.txt'))
    #print("Задача №2:")
    #print(homework.get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2))
    print(homework.join_in_advance(['sorted\\1.txt','sorted\\2.txt','sorted\\3.txt'],"sorted.txt"))
