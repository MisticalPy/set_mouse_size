# Автоматическое изменение размера курсора мыши с помощью сочетания клавиш

## Описание

Данный проект представляет собой скрипт на Python, который позволяет автоматически изменять размер курсора мыши при нажатии сочетания клавиш `Alt + M`. При первом нажатии курсор увеличивается, а при повторном — уменьшается до изначального размера.

## Идея проекта

Создание удобного инструмента для пользователей, которым необходимо быстро изменять размер курсора мыши для лучшей видимости или удобства работы. Этот скрипт позволяет избежать постоянных переходов в настройки операционной системы для изменения размера курсора, что экономит время и упрощает работу.

## Как это работает

1. Установите необходимые библиотеки:
   - `keyboard`
   - `mouse`

   Вы можете установить их с помощью pip:
   ```bash
   pip install keyboard mouse

2. Запустите скрипт. При нажатии Alt + M размер курсора в первый раз увеличится, а при повторном нажатии — уменьшится до минимального значения (обычного).

## Установка

1. Клонируйте репозиторий:

   git clone https://github.com/MisticalPy/set_mouse_size.git
   cd имя_репозитория

2. Установите зависимости, если они не установлены:

   pip install keyboard mouse

3. Запустите скрипт:

   python ваш_скрипт.py

## Использование

- Нажмите Alt + M, чтобы изменить размер курсора мыши.
- Повторно нажмите Alt + M, чтобы вернуть курсор к исходному размеру.

## Примечания

- Скрипт может требовать прав администратора для корректной работы, так как взаимодействует с системными настройками.
- Убедитесь, что у вас установлены Python и необходимые библиотеки.

## Лицензия

Этот проект лицензирован под MIT License - смотрите файл LICENSE для подробностей.
