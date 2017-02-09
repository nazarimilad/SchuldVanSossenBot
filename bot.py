#!/usr/bin/python3
# -*- coding: utf-8 -*-

import praw, pdb, re, os

reddit = praw.Reddit('SchuldVanSossenBot')
subreddit = reddit.subreddit("Belgium")
keywords = ("ban",
            "stolen", "steel", "stelen", "vole", "volé",
            "falling apart",
            "fined", "boet", "beboet",
            "schuldig", "guilty", "coupable"
           )

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

for submission in subreddit.hot(limit=5):
    if submission.id not in posts_replied_to:
        isKeywordInTitle = False
        for keyword in keywords:
            if re.search(keyword, submission.title, re.IGNORECASE):
                isKeywordInTitle = True

        if isKeywordInTitle:
            submission.reply("Het is de schuld van de sossen!")
            print("SchuldVanSossenBot replying to: ", submission.title)
            posts_replied_to.append(submission.id)

with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
