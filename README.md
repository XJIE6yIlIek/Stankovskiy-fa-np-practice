# NP Сетевые системы и приложения - ВТОРОЙ СЕМЕСТР

# Страничка семинаров ПИ22-1 ПИ22-2 ПИ22-3 ПИ22-4




Основные темы практики:
---

Первый семестр:

* ~~[ОСНОВЫ LINUX](https://github.com/VladimirAndropov/fa-os-practice/README.md)~~



Второй семестр:

 * [Сетевые приложения](#брс) 




Материалы курса
---
Вы можете познакомиться с материалами курса - презентациями к лекциям, методических рекомендациям к лабораторным работам на [github](http://koroteev.site/os/).

 Плейлист с видео по данному курсу досупен на [YouTube](https://www.youtube.com/playlist?list=PLhgyvraU60gU8OAhjtcipU_sO7UYvkQl9). 


# План семинарных занятий


- Системы контроля версий
  - Вначале мы изучаем git для совместной разработки
  - Учимся настраивать синхронизацию проектов через GitHub
 
- Использование сокетов
  - Затем создаем простейшее серверное приложение, которое отправляет потоковое видео

- Веб-сервер
  - Развиваем предыдущий опыт в сокетах до создания простейшего http веб-сервера 
  - Добавляем функционал многопоточности для http веб-сервера 
  - Добавляем функционал многопроцессности для ускорения http веб-сервера 
  - Добавляем библиотеки асинхронного программирования для http веб-сервера


Вторая половина семестра
- Развертывание сетевых приложений
  - Пакуем в контейнер - развертываем http асинхронный параллельный веб-сервер на удаленном ресурсе (hub.docker.com)



# БРС

Второй семестр

| дата № п/п  | Вид учебной деятельности| Максимум  за семестр |
| :---         |     :---:      |          ---: |
| [05.02-11.02 Аудиторная работа ](0_git_basics/README.md)  | Работа с Git     | 1    |
| -   | запушить изменения в проект 1_echo на github     | 1    |
| -   | сделать форк этого репозитория и открыть его в IDE| 1    |
| [задание 2 Лабораторная работа-0.2](7_TCP_server)   | настроить .gitignore, удалить лишнее| 1    |
| -   | примонтировать один из проектов как субмодуль| 1    |
| [12.02-18.02 Лабораторная работа-1.1 ](1_echo_server/задание2/README.md)   |  echo-сервер    | 1    |
| [задание 2 Лабораторная работа-1.2](1_echo_server/задание2/README.md)   | TCP-клиент + telnet/putty     | 1    |
| [задание 3 Лабораторная работа-1.3](1_echo_server/README.md)   |  live stream video server    | 1    |
| [Лабораторная работа-5.1](5_FTP_server/README.md)  | ftp-сервер (файлы output+file1)     | 1    |
| [задание 2 Лабораторная работа-5.2](5_FTP_server/задание2/README.md)  | файловый менеджер    | 1    |
| [ 19.02-25.02 Лабораторная работа-4.1](4_requests)  | Postman  (запросы к ruz.fa.ru)   | 1    |
| [задание 2 Лабораторная работа-4.2](4_requests)   | код http-клиента из Postman   | 1    |
| [ 26.02-3.03 Лабораторная работа-6.1](6_Web_server/README1.md)  | Веб-сервер HTTP Часть1 (webserver1)  | 1    |
| [задание 2 Лабораторная работа-6.2](6_Web_server/задание2/README.md)   | Низкоуровневая работа с веб  | 1    |
| [задание 3 Лабораторная работа-6.3](6_Web_server/README2.md)   | Веб-сервер HTTP  Часть2 (фреймворк+вебсервер)  | 1    |
| [ 04.03-10.03 Лабораторная работа-2.1](6_Web_server/README3.md)   | threaded Веб-сервер HTTP  Часть3 (fork)    | 1    |
| [задание 2 Лабораторная работа-2.2 ](2_threaded_server/задание2/README.md)  | threaded server    | 1    |
| [задание 3 Лабораторная работа-2.3 ](2_threaded_server/README.md)  | threaded+async server    | 1    |
| [ 11.03-17.03 Лабораторная работа-7.1](https://github.com/VladimirAndropov/7_TCP_server)  | UDP/TCP-threaded-сервер      | 1    |
| [задание 2 Лабораторная работа-7.2 ](7_TCP_server/README.md)  | субмодуль UDP/TCP-threaded     | 1    |
| ---------------------- |Вторая половина семестра|----------------------|
| Аудиторная работа  | настройка env   | 1    |
| -  | настройка pip   | 1    |
| [Лабораторная работа-3.1](3_Parallelism)  | multiprocessing   | 1    |
| [Лабораторная работа-3.2 ](3_Parallelism) | перемножение матриц  | 1    |
| [Лабораторная работа-8.1](8_Assymmetric_ciphers_2022/README.md)  |  SSL  | 1    |
| [Лабораторная работа-8.2 ](8_Assymmetric_ciphers_2022/ftp)   | сервер (asyncio.io)  | 1    |
| [Лабораторная работа-9.1 ](9_flask_app_2022/README.md)   |  app в docker  |1    |
| [Лабораторная работа-9.2 ](9_flask_app_2022/README.md)   |  1_echo_server в docker |1    |
| [Лабораторная работа-9.3 ](9_flask_app_2022/README.md)   |  5_FTP_server в docker |1    |
| [Лабораторная работа-9.4 ](9_flask_app_2022/README.md)   |  6_Web_server в docker |1    |
| [Лабораторная работа-9.5 ](11_Celery_Rabbit/README.md)   | Celery_Rabbit  | 1    |
| [Лабораторная работа-10.1 ](10_apache_nginx/README.md)   | apache  |1    |
| [Лабораторная работа-10.2 ](10_apache_nginx/README.md)   | nginx  |1    |
| [Лабораторная работа-11.1 ](11_Celery_Rabbit/README.md)   | балансировка в docker  | 1    |
| [Лабораторная работа-11.2 ](11_Celery_Rabbit/README.md)   | Celery Workers + Queue  |1    |
| -  | Тестовые опросы  | 5    | 


## Пояснение:
- Доля измеримых видов контроля самостоятельной
работы обучающихся, исключающих субъективное суждение = 30 баллов
- Самостоятельная работа обучающегося = 10 баллов 
- Посещение занятия = 0.3 балла
- Повторение действий преподавателя = 0.7 баллов
- Интерактивные формы проведения занятий = 10 баллов

от 7 до 20 баллов, считается
аттестованным

# Примерные задания для подготовки к экзамену
1. Напишите программу, которая создает нить. Родительская и вновь созданная нити должны распечатать десять строк текста. [README](exam/1.md)
2. Напишите простой эхо-сервер, использующий неблокирующие сокеты и клиент к нему.[README](18sem-fs/socket_example.c)
3. Напишите простой многопоточный загрузчик URL. Список URL скрипт принимает как аргументы командной строки.[README](2017/20-socket/README.md)
4. Реализуйте простой HTTP-клиент. Он принимает один параметр командной строки - URL. Клиент делает запрос по указанному URL и выдает тело ответа на терминал как текст.
5. Напишите программу, которая вычисляет число Пи при помощи ряда Эйлера. Количество потоков программы должно определяться параметром командной строки. 
6. Дана функция calculate(x, y). Напишите программу, которая создает пул из 5 процессов и распределяет в этом пуле вычисление функции на промежутке х от 0 до 1 с шагом 0,1. у равняется 2 всегда.[README](2017/24-stdthread/README.md)
7. Напишите программу, которая проверяет все числа от 0 на простоту и выводит простые числа на экран по мере нахождения. Числа должны проверяться в различных потоках (или процессах, по выбору студента) Программа должна работать до тех пор, пока ее не остановит пользователь.
8. Напишите программу, которая обходит все файлы в директории, переданной ей как параметр и выводит на экран имена тех, чей размер задан как второй параметр. Реализовать рекурсивный обход поддиректорий.[README](12sem-fs/README.md)
9. Напишите программу, которая выводит на экран список номеров открытых портов на данной машине. Использовать команду netstat.
10. Напишите программу, которая копирует файл с удаленного хоста в текущую папку по SSH. Имя файла и адрес хоста принимать как параметры.


# Пример экзаменационного билета
Экзаменационный билет №

1. Понятие потокобезопасности. Причины, проблематика, способы обеспечения. (20 баллов)
2. Доступ к общим ресурсам в многопоточной программе. Механизмы блокировки ресурсов модуля threading. (20 баллов)
3. Напишите программу, которая создает четыре нити, исполняющие одну и ту же функцию. Эта функция должна распечатать последовательность текстовых строк, переданных как параметр. Каждая из созданных нитей должна распечатать различные последовательности строк. (20 баллов)

