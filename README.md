To run the program, type python3 TicketList.py in your command line. 
Python ver. 3 should be installed -- I do not know if a lesser version will work.
The Requests library must also be installed. Type pipenv install requests in your command line.
If pipenv is not installed, type pip install pipenv in the command line. 

The program's UI works through the command line. Upon starting, the program will ask for the user's credentials to import ticket data. If successful, the program will then ask input at the command line. 

Typing the number 1 and pressing enter will bring up a paginated list of tickets. The ticket list will only show the
the id number, status, priority, and subject of each ticket. 

The number 2 will bring up a prompt for a ticket ID number, which can then be entered to see the rest of the ticket details. 

Any other input entered besides the numbers 1 and 2 will cause the program to exit the current view (either the ticket list
or the individual ticket viewer) or if at the main menu, will cause the program to completely exit.


-----------------------------------------------------------

I wanted to note that I have not used Python much, and recently learned about the requests library and JSON for this challenge. Hence, I believe my implementation is a bit hackish. If accepted into the Zendesk internship, I promise that I will work hard to be
competent in whatever technologies the company uses by the time the internship starts. Thank you very much 
for reviewing my challenge submission! 
