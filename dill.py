import requests
from PIL import Image
import io

# URL of the rickroll GIF
url = 'https://media.giphy.com/media/3o0mE7U9EDA20JWwYI/giphy.gif'

# Download the GIF
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Open the image and display it
    image = Image.open(io.BytesIO(response.content))
    image.show()