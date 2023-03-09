import os
import subprocess
import time
import random
while True:
    
    cmt= open('/home/ubuntu/commit/DailyCommit/commit.txt', "w")
    words =("Hi","hello","Trying to commit","my life is good","Commit for timleine","In progress....")
    word = random.choice(words)
    cmt.write(word)

    cmt.close()
    
    # Replace these with your own values
    repo_path = '/home/ubuntu/DailyCommit'

    github_username = 'hasan-kayan'
    github_repo = 'DailyCommit'
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
    times = (14400, 21600, 28800, 36000, 43200, 50400, 57600, 64800, 72000, 79200)
    a =random.choice(times)
    print("I will be wating for the commit for", a, "seconds,which is eqaul to", a/3600, "hours")
    time.sleep(a)     
