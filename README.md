Dipper Task - Scraper
=====================
A python module to track GPS data from different sources
for better functionality.


Dependencies
------------
- ##Selenium
	```py
		pip install selenium
	```

- ##PhantomJS
	[Click here](https://gist.github.com/julionc/7476620)
	**Follow this as any package manager doesnt
	provide the latest version**

The package consists of 
	--> scarper.py
	--> cronjob.sh

Functionality
--------------
- ##index.html
	A basic Login page which collects
	Username
	Password
	Time for Cronjob (minutes:hours:days:months:days_of_week)

- ##controller.rb:
	A ruby script which collects the data and runs the two scripts
	scarper.py and cronjob.py
	
	The scraper.py gets username and password as commandline arguements

	The cronjob gets username and password and the time setting as command 
	line arguements

	Example:

		```ruby 
		system("python scraper.py <username> <password>")
		``` 
		```ruby 
		system("bash cronjob.sh <username> <password> <minutes> <hours> <days> <months> <days_of_week>")
		``` 
- ##scraper.py:
			
			The main file which does the scraping and saves the
			data in a .json file locally
			(Can be changed as needed)
			
- ##cronjob.sh:

			It sets up the cronjob on scraper.py so that it
			regularly scrapes the data.