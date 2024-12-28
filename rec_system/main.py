from Dialog_System.colors import Colors
from Dialog_System.rec_system import (
    drawManhattanDistance,
    drawEuclideanDistance,
    drawCosDistance,
    drawColorDistance,
    drawCountryDistance,
    drawJacquardDistance,
    drawTreeDistance,
    drawCompinedDistance,
    task1,
    task2,
    task3,
    ui_lab4
)

MSG = """
    \t%sМеню\n
    1.  Манхэттенское расстояние;
    2.  Евклидово расстояние;
    3.  Расстояние по странам;
    4.  Расстояние по цветам;
    5.  Косинусное сходство;
    6.  Мера Жаккара
    7.  Расстояние по дереву;
    8.  Комбинированное расстояние;

    9.  Задача 1;
    10. Задача 2;
    11. Задача 3;
    12. UI;

    0.  Выход.\n
    %sВыбор: %s""" %(Colors.YELLOW, Colors.GREEN, Colors.BASE)


def inputOption():
    try:
        option = int(input(MSG))
    except:
        option = -1

    if option < 0 or option > 12:
        print("%s\nОжидался ввод целого числа от 0 до 12%s" % (Colors.RED, Colors.BASE))

    return option

def main():
    option = -1
    while option != 0:
        option = inputOption()
        match option:
            case 1:
                drawManhattanDistance()
            case 2:
                drawEuclideanDistance()
            case 3:
                drawCountryDistance()
            case 4:
                drawColorDistance()
            case 5:
                drawCosDistance()
            case 6:
                drawJacquardDistance()
            case 7:
                drawTreeDistance()
            case 8:
                drawCompinedDistance()
            case 9:
                task1()
            case 10:
                task2()
            case 11:
                task3()
            case 12:
                ui_lab4()



if __name__ == '__main__':
    main()