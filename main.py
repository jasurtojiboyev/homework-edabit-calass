class User:
    def __init__(self, username, user_count):
        self.username = username
        self.user_count = user_count

    def check_user_count(self):
        if self.user_count < 100:
            print("Foydalanuvchilar soni tez-tez o'zgardi.")
        elif self.user_count < 1000:
            print("Foydalanuvchilar soni normal darajada.")
        else:
            print("Foydalanuvchilar soni ko'p.") 

# Sinfdan obyekt yaratish
user1 = User("foydalanuvchi1", 50)
user2 = User("foydalanuvchi2", 500)
user3 = User("foydalanuvchi3", 5000)
# Foydalanuvchilar sonini tekshirish
user1.check_user_count()  # Foydalanuvchilar soni tez-tez o'zgardi.
user2.check_user_count()  # Foydalanuvchilar soni normal darajada.
user3.check_user_count()  # Foydalanuvchilar soni ko'p.
