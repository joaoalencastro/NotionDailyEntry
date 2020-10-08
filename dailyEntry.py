# -*- coding: utf-8 -*-
#!/usr/bin/python3
from notion.client import NotionClient
from notion.block import TextBlock, TodoBlock, PageBlock, HeaderBlock, DividerBlock, NumberedListBlock
from datetime import datetime
from os import environ

# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in session on Notion.so
client = NotionClient(token_v2=environ['NOTIONTOKEN'])

# Replace this URL with the URL of the page you want to edit
#page = client.get_block(environ['NOTIONPAGE'])
cv = client.get_collection_view(environ['NOTIONPAGE'])

# Now create a new page for the Daily Entry
#daily_entry = page.children.add_new(PageBlock, title=str(datetime.now())[:10])
daily_entry = cv.collection.add_row()
daily_entry.title = str(datetime.now())[:10]

# Down here is the page's customization

daily_dream = daily_entry.children.add_new(HeaderBlock, title="Sonhei com")

# Pular linha
daily_entry.children.add_new(TextBlock, "")

intentions = daily_entry.children.add_new(HeaderBlock, title="Intenções")

# Pular linha
daily_entry.children.add_new(TextBlock, "")

happenings = daily_entry.children.add_new(HeaderBlock, title="Acontecimentos")

# Pular linha
daily_entry.children.add_new(TextBlock, "")

grateful_for = daily_entry.children.add_new(HeaderBlock, title="Sou grato")

daily_entry.children.add_new(NumberedListBlock, "Pela minha família, que é presente e abençoada.")
daily_entry.children.add_new(NumberedListBlock, "Pela minha boa condição de vida.")
daily_entry.children.add_new(NumberedListBlock, "Pelos meus amigos que se importam demais comigo.")

actions_items = daily_entry.children.add_new(HeaderBlock, title="A fazeres")

actions_items_todo_block_1 = daily_entry.children.add_new(TodoBlock, title='Ler no mínimo dois artigos/notícias. Medium ou Feedly.')

daily_entry.children.add_new(DividerBlock)

# Pular linha
daily_entry.children.add_new(TextBlock, "")

health = daily_entry.children.add_new(HeaderBlock, title="Saúde")
