# test_module5.py

from web_development import create_static_website
import os

def test_create_static_website():
    result = create_static_website()
    assert result == "Static website created successfully."

    # Verify that the file was created
    assert os.path.exists("index.html")

    # Verify the content of the file
    with open("index.html", "r") as file:
        content = file.read()
        assert "<title>My Static Website</title>" in content
        assert "<h1>Hello, World!</h1>" in content
        assert "<p>This is a simple static website.</p>" in content

if __name__ == "__main__":
    test_create_static_website()
    print("All test cases passed successfully.")

