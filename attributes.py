class user:
	count =  0
	def __init__(self, user_name):
		self.secret_key = 1234
		if "".join(user_name.split()).isalpha():
			self.user_name = user_name
		else:
			self.invalid_name = user_name

	def __str__(self):
		return self.user_name
	def __see_self(self):
		return f"secret_key {self.secret_key}"

user1 = user("Jacob Watua Wanyoyi65")
if hasattr(user1, 'user_name'):
	print("Details captured successfully")
	print(user1.user_name)
elif hasattr(user1, 'invalid_name'):
	print("Check details and try again! Name should not include numeric Characters")
	print(user1.invalid_name)
print(user1._user__see_self())