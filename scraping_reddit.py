

import os
import praw
from typing import Union, List, Tuple

class memeGetterReddit(praw.Reddit):
    def __init__(self, **config_settings: Union[str, bool]):
        super().__init__(**config_settings)

    def get_memes(self, how_many = 3, subreddit_name = None) -> List[praw.reddit.Submission]:
        if subreddit_name == None:
            subreddit_name = "memes"
        submission_list = self.subreddit(subreddit_name).top(limit = how_many)
        print(submission_list)
        return list(submission_list)

    def get_image_urls_and_titles(self, how_many = 3, subreddit_name = None) -> Tuple[List[str], List[str]]:
        """
        :param how_many: How many submissions you want to go over in the api
        :param subreddit_name: name of the subreddit you want to go over
        :return: A tuple that contains first the list of image urls, and second the titles
        """
        submission_list = self.get_memes(how_many = how_many, subreddit_name = subreddit_name)
        image_url_list = []
        titles = []
        for k in submission_list:
            current_url = k.url
            if current_url.endswith(".jpg") or current_url.endswith(".png") or current_url.endswith("jpeg"):
                image_url_list.append(current_url)
                titles.append(k.title)

        return (image_url_list, titles)
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

    me = memeGetterReddit(client_id = client_id,
                          client_secret = client_secret,
                          user_agent = user_agent)

    print(me.get_image_urls_and_titles())

    # reddit = praw.Reddit(
    #     client_id=client_id,
    #     client_secret=client_secret,
    #     user_agent=user_agent
    # )
    #
    # print(reddit_username, reddit_password)
