#!/usr/bin/python3
# -*- coding: utf-8 -*-

import praw, pdb, re, os

reddit = praw.Reddit('SchuldVanSossenBot') # Make an instance of the Reddit object
subreddit = reddit.subreddit("Belgium")    # Make an instance of the subreddit /r/Belgium with the Reddit instance
nameWhitelistFile = "posts_replied_to.txt"
message = "Het is de schuld van de sossen!"

# Keywords used to target specific posts, containing one of more of this keywords
# not only this keywords explicitly, but also very similar words. For example: "ban" --> "banned" is also used to target
keywords = ("ban",
            "stolen", "steel", "stelen", "vole", "volé",
            "falling apart",
            "fined", "boet", "beboet",                          
            "schuldig", "guilty", "coupable",
            "failli", "bankrupt")

# Posts on which the comment already has been posted, shouldn't be targeted a second time
if not os.path.isfile(nameWhitelistFile):
    posts_replied_to = []
else:
    with open(nameWhitelistFile, "r") as f:
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
            submission.reply(message)
            posts_replied_to.append(submission.id)

# Posts which first didn't have the comment but now do, get whitelisted too
with open(nameWhitelistFile, "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
