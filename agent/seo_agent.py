from openai import OpenAI
from config import OPENAI_API_KEY
from agent.prompt import SEO_AGENT_PROMPT

client = OpenAI(api_key=OPENAI_API_KEY)

def run_seo_agent(summary_text):

    response = client.chat.completions.create(
        model="gpt-5.2",
        messages=[
            {"role": "system", "content": SEO_AGENT_PROMPT},
            {"role": "user", "content": summary_text}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content
