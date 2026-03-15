import requests

def generate_image(prompt, index):

    url = f"https://picsum.photos/seed/{index}/512/512"

    response = requests.get(url)

    path = f"static/images/scene_{index}.png"

    with open(path, "wb") as f:
        f.write(response.content)

    return path