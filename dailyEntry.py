# -*- coding: utf-8 -*-
#!/usr/bin/python3
from notion.client import NotionClient
from notion.block import TextBlock, TodoBlock, PageBlock, HeaderBlock, DividerBlock
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

intentions = daily_entry.children.add_new(HeaderBlock, title="Intentions")

daily_entry.children.add_new(DividerBlock)

happenings = daily_entry.children.add_new(HeaderBlock, title="Happenings")

daily_entry.children.add_new(DividerBlock)

grateful_for = daily_entry.children.add_new(HeaderBlock, title="Grateful for")

daily_entry.children.add_new(DividerBlock)

actions_items = daily_entry.children.add_new(HeaderBlock, title="Action items")

actions_items_todo_block = daily_entry.children.add_new(TodoBlock, title='')
