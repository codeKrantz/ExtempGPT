from openai import OpenAI
from docx import Document
client = OpenAI()
# make prompt and input again but this time check the terminal before running
file_name = input("What should the name of the file be?")
article_origin = input("Enter where the artical is from")
prompt = """Write a summary of the following article from the {ARTICLE}, then create a Conservative political take, a Moderate political take, and a Liberal political take:

insert article

""".format(ARTICLE = article_origin)


completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful research assistant for extemporaneous speakers in the NSDA."},
    {"role": "user", "content": str(prompt)},
    {"role": "assistant", "content": str(article_origin)}
  ]
)

text = str(completion.choices[0].message)

document = Document()
document.add_heading("Article from: {ARTICLE}".format(ARTICLE=article_origin))
document.add_paragraph(text)
document.save("{NAME}.docx".format(NAME=file_name))