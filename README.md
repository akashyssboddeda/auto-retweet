AUTO-RETWEET
===

This simple script is used to automatically retweet messages from the
[Discord insoumis](http://discord.insoumis.online/) to ensure a strong online
presence for the ["Unsubmissive France"](https://jlm2017.fr/) movement.

---

### INSTALLATION

You need Python 3.5 or higher to use the script as well as, of course, a
Discord account.  
After cloning the repository, run the following command in a terminal:

```
# pip install -r requirements.txt
```

You will need to create a Twitter app connected to your Twitter account in
order to get the appropriate credentials. [Follow this guide to learn about
creating a Twitter app.](https://python-twitter.readthedocs.io/en/latest/getting_started.html#create-your-app)

Once you have successfully created your Twitter app, complete the file
`credentials.py` with your Twitter access tokens, as well as your Discord
login.

### USAGE

Simply run

```
$ python auto-retweet.py
```

in a terminal.

---

### TODO

 - Modify the parser so that the code can be reused to automatically retweet
   with different conditions
 - Offer the possibility to increase or decrease the amount of missed tweets
   to retweet when logging back

---

*For the [Discord Insoumis](http://discord.insoumis.online/) — Copyright © 2017
 Crudités, distributed under the
 [MIT license](https://tldrlegal.com/license/mit-license).* 
