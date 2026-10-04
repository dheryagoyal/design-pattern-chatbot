from personalities import formal_responses, informal_responses

class PersonalityStrategy:
    def respond(self, user_input):
        return "Sorry, I don't understand that yet."

class FormalStrategy(PersonalityStrategy):
    def respond(self, user_input):
        if user_input in formal_responses:
            return formal_responses[user_input]

        return "I am sorry, but I do not understand that yet."

class InformalStrategy(PersonalityStrategy):
    def respond(self, user_input):
        if user_input in informal_responses:
            return informal_responses[user_input]

        return "Sorry, I don't get that yet!"
