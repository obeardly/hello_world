# hello_world

I bought "Hello World: Computer Programming for Kids and Other Beginners" for a friends son.  I also bought a copy for myself to help him work through the exercises.  This is the culmination of that project. I'll be putting top-level notes here; things like setting up git. 

Setting up git via a Linux terminal.  

On Devuan/Debian based distributions, you can simply install git via apt. 

	apt-get install git

Set your user.name and user.email.

	git config --global user.name "Linux O'Beardly"
	git config --global user.email "linux.obeardly@gmail.com"
	git config --global core.editor vi #or emacs if you're a loser

Generate a new ssh key. 

	ssh-keygen -t rsa -b 4096 -C "linux.obeardly@gmail.com"

Check this site for specifics:

https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/

Add your ssh key to your github account. Copy the output of: 

	cat ~/.ssh/id_rsa.pub

Then go to the github.com via a web browser. After logging in, in the right upper corner, select your profile, then go to "Settings > SSH and GPG Keys." Click "Add SSH Key," insert a name in the "Title" field, then paste your public key in "Key" field.  Save it.  

Return to the terminal and verify your account. 

	ssh -T git@github.com

You should see: 

	Hi obeardly! You've successfully authenticated, but GitHub does not 
	provide shell access.` 

Now, you can start using git to view and share your code. Create a directory for your code and add it as a repo at github.  

	mkdir hello_world
	cd hello_world
	git init

Write some code, preferably some of the exericises from the "Hello World" programming book, commit it to github, then upload it. 

	git add *.py
	git commit -m 'First upload'
	git push
	
Now you're ready to do some serious coding. 
