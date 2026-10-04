from factory import ResponseFactory
from logger import Logger
from config import Config

class Chatbot:
    def __init__(self, strategy):
        self.factory = ResponseFactory()
        self.logger = Logger()
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def get_response(self, user_input):
        user_input = user_input.lower().strip()

        if user_input in ["hello", "hi", "how are you", "what is your name", "help", "bye"]:
            response = self.strategy.respond(user_input)
        else:
            handler = self.factory.create_handler()
            response = handler.get_response(user_input)

        self.logger.log("User: " + user_input)
        self.logger.log("Bot: " + response)

        return response
