import os
import subprocess
import time
import random
while True:
    # Commit changes to repo by the random words in commit.txt
    
    cmt= open('/home/ubuntu/Commit/Second-Task-CAS/commit.txt', "w")
    words =("Hi","hello","Trying to commit","my life is good","Commit for timleine","In progress....")

    word = random.choice(words)
    word2 = random.choice(words)
    word3 = random.choice(words)

    cmt.write(word)
    cmt.write(word2)
    cmt.write(word3)
    

    cmt.close()
    


    # Replace these with your own values

    repo_path = '/home/ubuntu/Commit/Second-Task-CAS'

    github_username = 'hasan-kayan'
    github_repo = 'Second-Task-CAS'
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
    github_token = 'Github Token'

    subprocess.run(['git', 'push', f'https://{github_token}@github.com/{github_username}/{github_repo}.git'])
   
    time.sleep(52000)     
