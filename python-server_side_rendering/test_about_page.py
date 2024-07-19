import requests

def test_about_page():
    response = requests.get('http://127.0.0.1:5000/about')
    assert response.status_code == 200, "Failed: About page did not return status code 200"
    content = response.text
    assert '<header>' in content, "Failed: Header not found in About"
    assert '<footer>' in content, "Failed: Footer not found in About"
    print("About page loaded successfully, includes header and footer")

if __name__ == '__main__':
    test_about_page()
