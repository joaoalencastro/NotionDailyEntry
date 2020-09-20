
from notion.client import NotionClient
from notion.block import TextBlock, TodoBlock, PageBlock
from datetime import datetime
from os import environ

# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in session on Notion.so
client = NotionClient(token_v2=environ['NOTIONTOKEN'])

# Replace this URL with the URL of the page you want to edit
page = client.get_block(environ['NOTIONPAGE'])

# Now create a new page for the Daily Entry
daily_entry = page.children.add_new(PageBlock, title=str(datetime.now())[:10])

todo_block = daily_entry.children.add_new(TodoBlock, title="Criar o script de Daily Log")
todo_block.checked = True