def greet_user(username):
    print('hello' + username.title() + '!')


greet_user('jesse')


def describe_pet(pet_name,animal_type='dog'):
    print('\n I have a '+animal_type+'.')
    print('My '+animal_type + 's name is '+pet_name.title() + '.')


describe_pet('willie')
describe_pet(pet_name='willie')

n = {'pet_name' : 'harry','animal_type' : 'hamster'}
describe_pet(**n)
describe_pet(animal_type='hamster',pet_name='harry')


def get_formatted_name(first_name,last_name,middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi','hendrix')
print(musician)


def build_person(first_name,last_name,age = ''):
    person = {'first':first_name, 'last':last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi','hendrix',age=27)
print(musician)


def greet_users(*names):
    for name in names:
        msg = 'hello, ' + name.title() + '!'
        print(msg)


usernames = ['hannah','ty','margot']
greet_users(*usernames)