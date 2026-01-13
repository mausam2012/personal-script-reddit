import os
import praw
from dotenv import load_dotenv

load_dotenv()

def get_reddit_client():
    return praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        username=os.getenv("REDDIT_USERNAME"),
        password=os.getenv("REDDIT_PASSWORD"),
        user_agent=os.getenv("REDDIT_USER_AGENT"),
    )

def fetch_top_posts(subreddit_name, limit=5):
    reddit = get_reddit_client()
    subreddit = reddit.subreddit(subreddit_name)

    posts = []
    for post in subreddit.top(limit=limit, time_filter="day"):
        posts.append({
            "title": post.title,
            "score": post.score,
            "comments": post.num_comments,
            "url": post.url
        })

    return posts

if __name__ == "__main__":
    data = fetch_top_posts("technology", limit=3)
    for item in data:
        print(item)
