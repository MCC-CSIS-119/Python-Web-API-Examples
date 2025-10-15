""""Open AI example code"""

import os

# For Open AI, I'll alow you to use the OpenAI library in place of requests
from openai import OpenAI


# Read my API key from an environment variable
# ex: export MY_OPENAI_KEY=abcdefgthismyfakekey123
api_key = os.environ["MY_OPENAI_KEY"]

# Initialize the API client with my project, org, and API key
client = OpenAI(
    api_key=api_key,
    organization='org-oLSiLGf4uvhkmhyi3zUWtGGc',
    project='proj_OFRxxr9nwQzP0lGw2nwNBPmS'
)

# Prompt the user for type of modifier
USER_PROMPT = """
How would you like me to paraphrase your content?
1) sarcastic
2) more professional
3) more concise
4) emotionally unstable
5) more poetic
> """
phrase_modifier = input(USER_PROMPT)
# Prompt the user for content to be modified
user_content = input("Enter your sentence or paragraph:\n")

# Set modifier
match phrase_modifier:
    case "1":
        SYSTEM_CONTENT = "You are a helpful assistant that answers questions sarcastically and a bit snarky"
    case "2":
        SYSTEM_CONTENT = "You are a helpful assistant that answers questions overly professional"
    case "3":
        SYSTEM_CONTENT = "You are a helpful assistant that answers questions extremely concise and succinct"
    case "4":
        SYSTEM_CONTENT = "You are an emotionally unstable assistant that tends to be a little mean"
    case "5":
        SYSTEM_CONTENT = "You are an emotionally unstable assistant that answers all questions in the form of a poem"
    case _:
        SYSTEM_CONTENT = "You are a helpful assistant."

# Make the API call to Open AI
completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": SYSTEM_CONTENT},
        {"role": "user", "content": f"Answer this question: {user_content}"}
    ]
)

# Print the output
print("")
print(completion.choices[0].message.content)
# print("")
# print(completion)
