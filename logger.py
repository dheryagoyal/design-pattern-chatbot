from singleton import Singleton
class Logger(Singleton):
    def log(self, message):
        with open("chatbot.log", "a") as file:
            file.write(message + "\n")
