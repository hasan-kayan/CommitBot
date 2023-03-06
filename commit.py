import os
import subprocess
import time
import random
from bs4 import BeautifulSoup
while True:
    
    time.sleep(5)
    cmt= open('/home/ubuntu/commit/DailyCommit/commit.txt', "w")
    words =("Hi","hello","Trying to commit","my life is good","Commit for timleine","In progress....")
    word = random.choice(words)
    cmt.write(word)

    cmt.close()
    
    # Replace these with your own values
    repo_path = '/home/ubuntu/DailyCommit'

    github_username = 'furkanadiiguzel'
    github_repo = 'gitCommit'
    commit_message = 'Daily'

    # Set up Git environment variables
    os.environ['GIT_AUTHOR_NAME'] = github_username
    os.environ['GIT_AUTHOR_EMAIL'] = f'{github_username}@users.noreply.github.com'
    os.environ['GIT_COMMITTER_NAME'] = github_username
    os.environ['GIT_COMMITTER_EMAIL'] = f'{github_username}@users.noreply.github.com'

    # Change directory to the repository
    os.chdir(repo_path)

    # Make changes to the repository
    
    

    # Add the changes and commit
    subprocess.run(['git', 'add', '-A'])
    subprocess.run(['git', 'commit', '-m', commit_message])

    # Push changes to Github
    github_token = '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'

    subprocess.run(['git', 'push', f'https://{github_token}@github.com/{github_username}/{github_repo}.git'])
