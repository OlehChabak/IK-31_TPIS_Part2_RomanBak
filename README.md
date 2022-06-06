# **Лабораторна робота №1**
---
## Необхідні ресурси: 
- Встановлена бібліотека `pydocstyle`.
- Встановлений компілятор для Python.

## Інформація про пакет програми:
* Знайшов пакет `num2words` на PYPI , який може перетворювати числа в слова .
* Додано `requirements.txt` в якому знаходяться бібліотеки.
* Створино пакет з логікою який розподілений між кількома модулями.
* Додано документацію, яка відповідає стандартним правилам `pydocstyle`.
* Налаштовано виконання за допомогою команди `python -m ConNumtoWord`.

## Макет Python проекту
```text
.                           <- the root project directory
├── ConNumtoWord            <- a package
│   ├── __init__.py         <- special module, says "ConNumtoWord" is the package
│   ├── __main__.py         <- a default execution
│   ├── module1             <- an inner package
│   │   └── __init__.py     <- special module, says "module1" is the inner package for "ConNumtoWord"
│   │── example.py          <- a module of "ConNumtoWord" package
│   └─ requirements.txt     <- used packages
└──────README.md            <- a description

```

* Перевірка чи відповідає проект стандартним правилам `pydocstyle` не виявила жодної помилки
```text
PS D:\Student\Roman Bak labs> python3 -m pydocstyle ConNumtoWord
```


## Приклад запуску програми у PowerShell:
* При введені коректних значень виводиться число записане словом:
``` text
PS D:\Student\Roman Bak labs> python3 -m ConNumtoWord
Hello!
Please, enter a floating point number: 51.3
Number to Word: fifty-one point three
```
* При введені некоректних значень виводиться напис "Could not convert data to an type 'float'. Please, enter a floating point number.", а в новому рядку записується цифра "0" у вигляді слова:
```text
PS D:\Student\Roman Bak labs> python3 -m ConNumtoWord
Hello!
Please, enter a floating point number: oleh
Could not convert data to an type 'float'. Please, enter a floating point number.
Number to Word: zero
PS D:\Student\Roman Bak labs>
```
