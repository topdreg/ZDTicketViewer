I do not know what qualifies as good happy path tests, but here's my attempt.

----------------------------------------------------------------------------------

Happy path tests:

Tested the program on input '1' for several individual ticket requests between the values of 
2 to 101, including both IDs 2 and 101. Got the full range of ticket details back
for each one. Good. 

IDs tested: 
2
25
50
60 
80 
101

Tested the program on input '1' for negative IDs, 102, and several numbers above 102. All requests to the program
reported that an ID could not be found. Good.
 
IDs tested:
-1 
1
120 
150

Tested the program on input '2'. IDs 2 to 101 were returned in successive order. ID 1 was not returned, 
meaning it was not returned on the request API. That makes sense because the ticket with ID 1 is merely an introductory 
ticket to the agent. 


Also tested the program on several input commands aside '1' or '2' to see if the program would exit.
The program does indeed exit on 'z', 'p', '3', 'abc', and several other input commands. 
