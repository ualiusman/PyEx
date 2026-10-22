import openai


def generate_tweet(client, topic):
    try:
        completion = client.chat.completions.create(
            model="deepseek-flash",
            messages=[
                {
                    "role": "system",
                    "content":"You are a social media expert skilled at creating engaging tweets."
                },
                {
                    "role":"user",
                    "content": f"Write a one sentence tweet about {topic}. Include relevant emojis."
                }
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"An error occured: {str(e)}"


def main():
    print("Welcome to the Tweet Generator!")

    client = openai.OpenAI(
        api_key="",
        base_url="https://api.deepseek.com"
    )

    while True:
        topic = input("Enter a topic for your tweet (or quit to exit)")
        if(topic == 'quit'):
            break
        tweet = generate_tweet(client,topic)
        print(tweet)
        print("\n" + "-"*50 + "\n")

main()