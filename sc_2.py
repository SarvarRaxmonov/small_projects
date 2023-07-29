from instagram_private_api import Client, ClientCompatPatch
from sc import main
import time
def get_least_6_posts_urls(username, password):
    api = Client(username, password)
    results = []

    try:
        time.sleep(3)
        user_info = api.username_info(username)
        user_id = user_info['user']['pk']
        media = api.user_feed(user_id).get('items', [])[:6]
        print(media)
        for post in media:
            post_url = f"https://www.instagram.com/p/{post['code']}/"
            results.append(post_url)

    except Exception as e:
        print(f"Error {e}")
    return results

if __name__ == "__main__":
      username = "sa.rvar_raxmonov"
      password = "Twistoff"

      post_urls = get_least_6_posts_urls(username, password)

      for url in post_urls:
          time.sleep(3)
          main(url)


