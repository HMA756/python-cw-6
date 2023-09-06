person = {
    'name':'Hoor',
    'age' : 14,
    'hobbies':['gaming','sketching','photoshopping']
}
print(person['name'])
print(person['age'])

person['age']=15
person['country']= 'Australia'
print(person)
print(len(person))

person['hobbies'].append('reading')
print(person)
def check_hobbies(person):
    if len(person['hobbies'])>=3:
        print('WOW YOU ARE AMAZING')
    else :
        print('error')

check_hobbies(person)

