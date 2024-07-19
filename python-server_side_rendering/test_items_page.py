import requests

def test_items_page():
    response = requests.get('http://127.0.0.1:5000/items')
    assert response.status_code == 200, "Failed: Items page did not return status code 200"
    content = response.text
    assert '<header>' in content, "Failed: Header not found"
    assert '<footer>' in content, "Failed: Footer not found"
    assert '<h1>Items</h1>' in content, "Failed: Items page heading not found"
    assert '<li>Item 1</li>' in content, "Failed: Items not found"
    print("Items page loaded successfully with status code 200 and includes the following: header, footer, and items")

if __name__ == '__main__':
    test_items_page()
