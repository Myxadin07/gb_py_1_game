import string

print ('Приветствуем Вас в игре Shooting bubles')

gamer = {'name': input('Как вас зовут?\n'),
         'age': int(input('Сколько тебе лет?\n')),
         'sex': input('Вы мужчина или женщина?\n'),
         'pet_name': input('Как зовут Вашего домашнего питомца?\n'),
         'like_to_play': input('Любите ли вы играть, да или нет?\n'),

         }
if gamer['like_to_play'] == 'Да':
    gamer ['like_to_play'] = True
else:
    gamer ['like_to_play'] = False

if gamer['age'] < 18:
    print(gamer['name'], 'тебе нельзя играть, потому что ты молодой')

elif gamer['age']>90:
    print(gamer['name'], 'эта игра может быть утомительна для Вас')
    gamer_over_90_answer = input ('Хотите ли вы играть все равно?\n')
    if gamer_over_90_answer == "Да":
        gamer_over_90_answer_two = input('Вы уверены?\n')
        if gamer_over_90_answer_two == "Да":
            print ('Хорошо, тогда начнем игру')
        else:
            print ('До свидания,', gamer['name'])



else:
    print ('Я могу назвать буквы алфавита,которых нет в твоем имени и произнести их в слух')


alphabet_lower = [chr(ord("а") + i) for i in range(32)]

even = [y for y in alphabet_lower if y not in list (gamer ['name'].lower())]

print (even)
