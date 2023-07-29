import requests
from bs4 import BeautifulSoup
import random
import time
def get_instagram_post_html(url):
    response = requests.get(url)
    return response.text if response.status_code == 200 else None


def extract_image_url(html):
    time.sleep(2)
    soup = BeautifulSoup(html, 'html.parser')
    image_tag = soup.find('meta', property='og:image')
    return image_tag['content'] if image_tag else None


def download_image(image_url, save_path):
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        return True
    return False

def main(post_url):
    html_content = get_instagram_post_html(post_url)

    if html_content:
        image_url = extract_image_url(html_content)
        if image_url:
            download_image(image_url, f'{random.random()}.jpg')
            print("Image downloaded successfully.")
        else:
            print("Could not extract image URL.")
    else:
        print("Failed to fetch post content.")




if __name__ == "__main__":
    main()


