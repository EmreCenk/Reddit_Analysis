

import os
import praw
from typing import Union, List

class memeGetterReddit(praw.Reddit):
    def __init__(self, **config_settings: Union[str, bool]):
        super().__init__(**config_settings)

    def get_memes(self, how_many = 100, subreddit_name = None) -> List[praw.reddit.Submission]:
        if subreddit_name == None:
            subreddit_name = "memes"
        submission_list = self.subreddit(subreddit_name).top(limit = how_many)
        return list(submission_list)

    def get_image_urls_and_titles(self):
        submission_list = self.get_memes()
        image_url_list = []
        titles = []
        for k in submission_list:
            current_url = k.url
            if current_url.endswith(".jpg") or current_url.endswith(".png") or current_url.endswith("jpeg"):
                image_url_list.append(k)
                titles.append(k.title)

        return image_url_list
if __name__ == '__main__':

    # I have saved my reddit username and password as environment variables
    # Retrieving the username and password from environment variables:
    from dotenv import load_dotenv
    load_dotenv()
    reddit_username = os.environ["reddit_username2"]
    reddit_password = os.environ["reddit_password2"]
    client_secret = os.environ["reddit_client_secret"]
    client_id = os.environ["reddit_client_id"]
    user_agent = os.environ["reddit_user_agent"]

    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent
    )

    print(reddit_username, reddit_password)
