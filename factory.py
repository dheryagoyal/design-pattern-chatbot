from responses import responses
from config import Config

class ResponseHandler:
    def get_response(self, user_input):
        if user_input in responses:
            return responses[user_input]

        return Config.UNKNOWN_RESPONSE

class ResponseFactory:
    def create_handler(self):
        return ResponseHandler()
