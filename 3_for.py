"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

score_dicts = [{'school_class': '4a', 'scores': [3,4,4,5,2]},{'school_class': '11a', 'scores': [3,4,5,4,5,5,4]}, 
    {'school_class': '8b', 'scores': [2,4,3,4,2,5,3]}, {'school_class': '2a', 'scores': [5,4,5,4,5,5,4]}]

def print_average_sc_score():
  points = 0
  total_students = 0
  for class_score in score_dicts:
    points += sum(class_score['scores'])
    total_students += len(class_score['scores'])
  average_sc_score = points / total_students
  print('Avarage score in school is: ' + str(round(average_sc_score,2)))

def print_average_class():
  for class_score in score_dicts:
    points = 0
    points = sum(class_score['scores'])
    average_class_score = points / len(class_score['scores'])
    print('In class ' + class_score['school_class'] + f' - avarege point is: {round(average_class_score,2)}')
        
    
def main():

  print_average_sc_score()
  print_average_class()

    
    
if __name__ == "__main__":
    main()
