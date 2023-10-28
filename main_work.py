chat_story = ""
command = input("Введите любой символ для начала работы чата (чтобы остановить работу чата, напишите 'end'): ")
while command != "end":
    user_name = input("\nВведите имя пользователя: ")
    command = input("\n1 - Посмотреть текст чата\n2 - Отправить сообщение\n3 - Остановить чат\nВыберете команду: ")
    if command == "1":
        print("\nИстория чата: ", chat_story)
    if command == "2":
        message = input("Введите сообщение: ")
        chat_story += user_name + ": " + message + "\n"
    if command == "3":
        print("Завершение работы чата.")
        break
    if command == " ":
        print("Такой команды нет. Завершение работы чата.")
        break
