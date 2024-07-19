import requests

def test_items_page_empty():
    base_url = 'http://127.0.0.1:5000'

    response = requests.get(f'{base_url}/items')

    assert response.status_code == 200, "Failed: Items page did not return status code 200"

    assert "No items found" in response.text, "Failed: 'No items found' message not displayed"

if __name__ == '__main__':
    test_items_page_empty()
