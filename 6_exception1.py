"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""
q_a_dict = {"Что делаешь?":"Программирую","Как дела?":"Нормально","Выходил сегодня на улицу?":"Нет, сидел дома.",
            "Как ты себя чувствуешь?":"Отлично!"}


def ask_user_dict(user_dict):
  
  
    while True:
      try:
        ask = input()
        if ask in q_a_dict.keys():
          return q_a_dict[ask]
        else:
          continue
      except KeyboardInterrupt:
        print('Пока')
        break
    
if __name__ == "__main__":
    ask_user_dict(q_a_dict)
