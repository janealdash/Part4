# 4)ContactList
# Создайте класс ContactList, который должен наследоваться от
# встроенного класса list. В нем должен быть реализован метод
# search_by_name, который должен принимать имя, и возвращать список
# всех совпадений. Замените all_contacts = [ ] на all_contacts =
# ContactList(). Создайте несколько контактов, используйте метод
# search_by_name.



class ContactList(list):
	def search_by_name(self):
		all_contacts={'Mommy':00001,'Daddy':00002,'Jane':00003,'Granny':00004}
		name=input('Enter the name:')
		print(all_contacts.get(name))

all_contacts=ContactList()
all_contacts.search_by_name()
