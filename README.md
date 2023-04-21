# Commit Bot 

## Purpose of The Bot 

    This bot has a simple purpose, commit on a regular basis. By using your personal account information, 
    this bot stays awake on a server you set up and aims to commit at intervals you specify.
    In order for this to work properly and for the bot not to shut itself down, some adjustments need to be made carefully.

## How To Use 🍳 

    Before installing the bot, we need to make some adjustments, first you need to create
    a Github Token, this token acts as a key to automate the usage in your account and to create management permission with commands. 
    To create this token, you can check out my github token creation post 😀. 
    Remember, do not share your token with anyone and save it in a safe place. 

    Lets check the simple flow of the code 
    ⏭ "Choose a random word." ⏭ " Write the word in to commit.txt file at the Daily Commit Repository" ⏭ " Commit it " ⏭ " Wait for the next commit as much as you wish" 

    Now lets start with understanding the code... 

   ![Resim1](https://user-images.githubusercontent.com/80827760/233622801-8fcb93db-fb07-4f8e-bd51-e0dde5af3ba6.png)


    Here we are adding neccesary libraries. And now we are writnig some simple words and creating a list by them. 
    As you know, if there is no change in the repo or if this change is the same as before, Github may not accept this commit because there is no change, to prevent this situation, we choose a random word from our list of a few words and write it to our commit.txt file.
    
![Resim2](https://user-images.githubusercontent.com/80827760/233622822-af94a3f2-2f44-4a98-9e05-e51f86752804.png)

    I am using AWS system EC2 so I have a file path for DailyCommit Repository I have cloned. You have to make the necessary arrangements according to the cloud system you will use and your structure there. After you write your Github username, the name of the repository you want to commit regularly and the message to be added to each commit, you can proceed to the next step. 

  ![Resim3](https://user-images.githubusercontent.com/80827760/233622854-59874bea-df0e-4d68-99e0-a6b1c7641b6d.png)

    
    We complete the settings for Github here and authorize and edit the server you set up, there is no need to make any personal changes here. 
    
![Resim4](https://user-images.githubusercontent.com/80827760/233622869-b7bd04cb-6af1-466e-8fab-344429e1de82.png)

 

    We are installing the changes we have made in the files by applying the terminal commands. Here we write the Github token that will be asked, the token that we created before. How often you want to commit in the last part, you can shorten or extend the time by changing the time.sleep() value.

    
