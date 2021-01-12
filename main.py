class Lid:

	def __init__(self, name, phone, stat, mail, responsible):
		self.name = name
		self.phone = phone
		self.stat = stat
		self.mail = mail
		self.responsible = responsible

	def change_responsible(self, name):
		print(f'Ответственный за пользователя {self.name} изменен!')
		self.responsible = name

	def change_stat(self, new_stat):
		print(f'Статус пользователя {self.name} изменен!')
		self.stat = new_stat

	def change_mail(self, new_mail):
		print(f'Почта пользователя {self.name} изменена!')
		self.mail = new_mail

	def change_number(self, new_phone):
		print(f'Номер телефона пользователя {self.name} изменен!')
		self.phone = new_phone

	def info(self):
		print(f'Имя: {self.name}')
		print(f'Номер телефона: {self.phone}')
		print(f'Статус: {self.stat}')
		print(f'Почта: {self.mail}')
		print(f'Ответственный за пользователя: {self.responsible}')
		print('\n\n\n')


man1 = Lid('Олег', 89294657645, 'staus', 'oleg1997@mail.ru', 'Евгений Обрамов')
man1.info()
man1.change_mail('oleg2@mail.ru')
man1.info()
man1.change_stat('new_status')
man1.info()
man1.change_responsible('Анатолий Глушко')
man1.info()
man1.change_number(89241232334)
man1.info()
input()