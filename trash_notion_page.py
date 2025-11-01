import requests
import json

NOTION_TOKEN = "" # Enter here your Notion token
DATABASE_ID = "" # Enter here your database ID

if not NOTION_TOKEN or not DATABASE_ID:
    print("NOTION_TOKEN or DATABASE_ID is not set. Exiting.")
    exit(1)

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def get_pages_from_database(property: str, property_name: str, property_value: str):
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    
    data = {
        "filter": {
            "property": f"{property_name}",
            f"{property}": {
                "equals": f"{property_value}"
            }
        }
    }

    print(f"Request URL: {url}")
    print(f"Request body: {json.dumps(data)}")
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        pages = response.json().get("results", [])
        print(f"Pages fetched: {json.dumps(pages, indent=2)}")
        return pages
    else:
        print(f"Error while requesting data: {response.status_code}")
        print(f"Response body: {response.text}")
        return []

def trash_page(page_id):
    url = f"https://api.notion.com/v1/pages/{page_id}"

    payload = {
        "in_trash": True
    }

    print(f"Attempting to trash page with ID: {page_id}")
    
    response = requests.patch(url, headers=headers, json=payload)

    if response.status_code == 200:
        print(f"Page {page_id} successfully trashd.")
    else:
        print(f"Error while archiving page {page_id}: {response.status_code}")
        print(f"Response body: {response.text}")

def trash_pages_by_status(property: str, property_name: str, property_value: str):
    pages = get_pages_from_database(property, property_name, property_value)

    for page in pages:
        page_properties = page["properties"]

        if property_name in page_properties:
            status_property = page_properties[property_name]
            if status_property[property] and status_property[property]["name"] == property_value:
                page_id = page["id"]
                print(f"Found page to trash with ID: {page_id}")
                trash_page(page_id)

if __name__ == "__main__":
    trash_pages_by_status("status", "Status", "Done") # Example