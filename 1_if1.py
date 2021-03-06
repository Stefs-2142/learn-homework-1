def distributor():
    """Распределяет куда тебе идти в зависимости от возвраста."""
    
    while True:            # Праверка на валидность введённых данных.
        try:
            age = abs(int(input('Введи свой возвраст, пожалуйста: ')))
            if age:
                break
            else:
                print("Попробуйте ещё раз.")
        except ValueError:
            print('Попроубйте ещё раз.')


    if age <= 6:
        if age == 1:
            return f'Так как, тебе только {age} год, ты должен ходить в садик.'
        elif age < 5:
            return f'Так как, тебе только {age} года, ты должен ходить в садик.'  
        else:
            return f'Так как, тебе только {age} лет, ты должен ходить в садик.'
    elif age > 6 and age <= 18:
        return f'Так как, тебе {age} лет, ты должен учиться в школе.'
    elif age > 18 and age <= 22:
        return f'Так как, тебе {age} лет, ты должен учиться в университете.'
    elif age > 22:
        return f'Ты уже взрослый, начинай работать.'

def main():
    user_age = distributor()
    print(user_age)

if __name__ == "__main__":
    main()
