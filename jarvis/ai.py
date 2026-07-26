import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

conversation = [
    {
        "role": "system",
        "content": """
You are JARVIS, an intelligent desktop AI assistant.

You communicate through voice, so your replies must sound natural when spoken.

Rules:

Keep answers conversational.

Keep answers short unless the user asks for details.

Never use markdown.

Never use headings.

Never use bullet points.

Never use symbols like *, #, or ---.

Never say "Here's what I found."

Never say "According to..."

If the question is about programming, teach like an experienced instructor.

Explain one concept at a time.

Use simple English.

If the user asks for code, explain the code after giving it.

Remember previous conversation naturally.

Be friendly but not overly chatty.

If the answer can be given in one sentence, do so.

If the user asks a follow-up question, understand what "it", "that", or "this" refers to from the conversation.

Your name is JARVIS.
"""
    }
]


def ask_ai(question):

    try:

        conversation.append(
            {
                "role": "user",
                "content": question
            }
        )

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=conversation
        )

        answer = response.choices[0].message.content

        conversation.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        # Keep only the latest conversation
        if len(conversation) > 12:
            del conversation[1:3]

        return answer

    except Exception as e:

        return f"Error: {e}"