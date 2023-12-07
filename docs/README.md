# Описание
Имеется 4 программы с фунциями вычисления периметра и площади геометрических фигур с заданными параметрами   
Программы работают со следующими геометрическими фигурами:  
* Круг
* Прямоугольник
* Квадрат
* Треугольник

## Круг
### Площадь
Функция **area** принимает следующие параметры:  
1. r (int) - радиус круга
Возвращает площадь круга с заданным радиусом
> print(area(3))
> ___
> 28.274333882308138

### Периметр
Функция **perimeter** принимает следующие параметры:  
1. r (int) - радиус круга
Возвращает периметр круга с заданным радиусом
> print(perimeter(3))
> ___
> 18.84955592153876

## Прямоугольник
### Площадь
Функция **area** принимает следующие параметры:  
1. a (int) - длина прямоугольника
2. b (int) - ширина прямоугольника
Возвращает площадь прямоугольника с заданными сторонами
> print(area(3, 2))
> ___
> 6

### Периметр
Функция **perimeter** принимает следующие параметры:  
1. a (int) - длина прямоугольника
2. b (int) - ширина прямоугольника
Возвращает периметр прямоугольника с заданными сторонами
> print(perimeter(3, 2))
> ___
> 10

## Квадрат
### Площадь
Функция **area** принимает следующие параметры:  
1. a (int) - сторона квадрата
Возвращает площадь квадарата с заданной стороной
> print(area(3))
> ___
> 9

### Периметр
Функция **perimeter** принимает следующие параметры:  
1. a (int) - сторона квадрата
Возвращает периметр квадарата с заданной стороной
> print(perimeter(3))
> ___
> 12

## Треугольник
### Площадь
Функция **area** принимает следующие параметры:  
1. a (int) - длина основания треугольника
2. h (int) - длина высоты опущенной к заданному основанию
Возвращает площадь треугольника с заданными основанием и высотой
> print(area(3, 2))
> ___
> 3

### Периметр
Функция **perimeter** принимает следующие параметры:  
1. a (int) - первая сторона треугольника
2. b (int) - вторая сторона треугольника
3. c (int) - третья сторона треугольника
Возвращает периметр треугольника с заданными сторонами
> print(perimeter(3, 2, 3))
> ___
> 8

# История репозитория:
1. (8ba9aeb) создание репозитория
2. (d078c8d) L-03: Docs added
3. (fa02a71) добавлен файл rectangle.py
4. (946af79) исправлена ошибка вычисления периметра в rectangle.py и добавлен файл triangle.py
5. (dd2e25a) Update README.md  
             Добавлено описание всех функций
6. (df00ca7) Добавлениы описания функций
7. (ded1b43) Merge https://github.com/remix292/geometric_lib
8. (e37315c) Переделал комментарии

# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah \ 2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c