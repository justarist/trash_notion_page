# Notion Page Trash Automation

This Python program automates the process of moving pages to trash in a Notion database based on specific properties. It connects to the Notion API, fetches pages from a database, and moves pages to the trash based on a given status.

## Requirements

Before running the program, make sure you have the following:

- Python 3.x installed

- requests library installed. You can install it via pip:
```bash
pip install requests
```

- A valid Notion API token (NOTION_TOKEN)

- The database ID (DATABASE_ID) of the Notion database you want to interact with

## Setup

### 1. Create a Notion Integration Token

Go to the [Notion Developers](https://www.notion.so/profile/integrations "Notion Developers") page.

Create a new integration to get your Integration Token.

Share access to your database with the integration (ensure the integration has permission to read and update the database).

### 2. Retrieve the Database ID

Open your Notion database in a web browser.

The URL should look like this:

<https://www.notion.so/your_username/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx?v=vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv>

The long string after the last slash and before ?v= (in this case, xxxxxxxxxxxxxxxxxxxxxxxxxx) is the Database ID.

### 3. Update the Script

Update the script with the following information:

NOTION_TOKEN: Your API integration token.

DATABASE_ID: The ID of the database you want to target.

```python
NOTION_TOKEN = "your-notion-token"
DATABASE_ID = "your-database-id"
```

### 4. Customize the trash_pages_by_status Function (Optional)

You can customize the trash_pages_by_status function to target different properties and values. By default, it looks for pages where the Status property is set to "Done".

```python
trash_pages_by_status("status", "Status", "Done")
```

You can modify it to check for other properties or values if needed.

## How It Works

The program queries the Notion database for pages that have a specific status property.

If the page matches the provided status value, the program moves the page to the trash.

Example Usage:

```python
# Fetch pages with "Status" set to "Done" and move them to trash
trash_pages_by_status("status", "Status", "Done")
```

## Functions

- `get_pages_from_database(property, property_name, property_value)`: Fetches pages from the Notion database that match the specified property name and value.

- `trash_page(page_id)`: Moves a specific page to the trash.

- `trash_pages_by_status(property, property_name, property_value)`: Fetches pages from the database and moves the ones with the matching status property value to the trash.

## Error Handling

The script will print errors if it encounters any issues while interacting with the Notion API, including invalid API tokens or database IDs.

Example Output:

```plaintext
Request URL: https://api.notion.com/v1/databases/your-database-id/query
Request body: {"filter": {"property": "Status", "status": {"equals": "Done"}}}
Pages fetched: [
  {
    "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "properties": {
      "Status": { "id": "xxxx", "name": "Done" },
      "Title": { "title": [{ "text": { "content": "Task 1" }}] }
    }
  }
]
Found page to trash with ID: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
Attempting to trash page with ID: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
Page xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx successfully trashed.
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
