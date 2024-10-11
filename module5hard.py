import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = hash(password)
        self.age = int(age)

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = int(duration)
        self.time_now = int(time_now)
        self.adult_mode = bool(adult_mode)

    def __str__(self):
        return self.title


    def __repr__(self):
        return self.title

class UrTube():
    users = []
    videos = []
    current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and password == user.password:
                self.current_user = user

    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f'Пользователь {nickname} уже существует')
        else:
            user = User(nickname, password, age)
            self.users.append(user)
            self.log_out()
            self.log_in()

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        if args in self.videos:
            print('Видео с таким названием уже существует')
        else:
            self.videos.append(args)

    def get_videos(self, text):
        list_videos = []
        for video in self.videos:
            if text.lower() in video.title.lower():
                list_videos.append(video.title)
        return list_videos

    def watch_video(self, title):
        if self.current_user and self.current_user.age < 18:
            print('Вам нет 18, пожалуйста покиньте страницу')
        elif self.current_user:
            for video in self.videos:
                if title in video.title:
                    for i in range(len(video.duration)):
                        print(i, end=' ')
                        time.sleep(1)
                    print('Конец видео')
        else:
            print('Войдите в акаунт, чтобы смотреть видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')









# user1 = User('Palina', 'pol', 19)
# v1 = Video('Video', 10, 3)
# print(user1.nickname, user1.password, user1.age)
# print(v1.title, v1.duration, v1.time_now, v1.adult_mode)