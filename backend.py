import openai


class Chatbot:
    def __init__(self):
        openai.api_key = "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"

    def get_response(self, user_input):
        response = openai.completions.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=3000,  # length of response by bot
            temperature=0.5,  # randomness of bot's response
        ).choices[0].text
        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Tell me the weather in Deva city of Romania.")
    print(response)
