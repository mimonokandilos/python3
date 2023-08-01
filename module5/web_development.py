# web_development.py

def create_static_website():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Static Website</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <p>This is a simple static website.</p>
    </body>
    </html>
    """

    with open("index.html", "w") as file:
        file.write(html_content)

    return "Static website created successfully."

