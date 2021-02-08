from mycroft import MycroftSkill, intent_file_handler


class AimlChatbot(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('chatbot.aiml.intent')
    def handle_chatbot_aiml(self, message):
        self.speak_dialog('chatbot.aiml')


def create_skill():
    return AimlChatbot()

