import requests


# -----------------------------------------------
# Method to import and prepare JSON data.
# -----------------------------------------------

def getTickets(domainName, user, pwd): 
    # Set request parameters
    url = 'https://' + domainName + '/api/v2/requests.json'

    # Do the HTTP get request 
    response = requests.get(url, auth=(user, pwd)) 

    # Check for HTTP codes other than 200 
    if response.status_code != 200: 
        print('Status:', response.status_code, 'Problem with the request. Perhaps the Zendesk API is unavailable. Exiting.') 
        exit() 

    # Decode the JSON response into a dictionary and use the data
    data = response.json() 
    data = data['requests']

    # Create dictionary based on id's. 
    dataDict = {}
    for item in data:
        dataDict[item['id']] = item
    
    return dataDict


# -----------------------------------------------
# Define methods for printing ticket data. 
# -----------------------------------------------


# Print function for a single ticket based on the ID.
# Takes a dictionary of the JSON data, and an ID key. 
def printTicket(dataDict, ID): 
    print('\n--------------------------------------\n')
    print("Here is the ticket with ID: ", ID, "\n") 
    for key in dataDict[ID]: 
        print(key, ":", dataDict[ID][key])
    print('\n--------------------------------------\n')  

# Print function to show list of tickets.
# Must press a key to show another 25 tickets.
# Take a dictionary of the JSON data. 
def printTicketList(dataDict): 
    counter = 0
    for key in dataDict: 
        if counter % 25 == 0 and counter != 0: 
            print('Enter 1 to continue to next 25 tickets. Enter any other key to exit to the main menu.\n')
            inputNum = input('Now enter a key: ')
            if inputNum != '1': 
                break 
        print('id', ':', dataDict[key]['id']) 
        print('status', ':', dataDict[key]['status']) 
        print('priority', ':', dataDict[key]['priority'])
        print('subject', ':', dataDict[key]['subject']) 
        print('\n--------------------------------------\n')  
        counter += 1
    print('\n--------------------------------------\n')  


# -----------------------------------------------
# Run UI and wait for user input. 
# -----------------------------------------------

if __name__ == '__main__': 

    print('\n####-------------------TICKET VIEWER-------------------####\n') 
    
    print('First, we need to import some ticket data. Please follow the prompts.\n')

    # Import ticket data. 
    domainName = input('Please enter your domain name, i.e. fred.zendesk.com: ') 
    user = input('Now enter your username, typically an email address: ') 
    pwd = input('Finally, enter your password please: ') 
    dataDict = getTickets(domainName, user, pwd) 
    
    print('\nThank you! Now onto the ticket viewer. =)\n') 

    inputNum = '1'

    while inputNum == '1' or inputNum == '2': 
        
        print('Enter 1 to show the list of tickets.\n') 
        print('Enter 2 followed by an ID to generate an individual ticket.\n') 
        print('Enter any other value to exit the program.') 

        print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n') 

        inputNum = input('Enter a command: ') 

        if inputNum == '1':  
            print('\n--------------------------------------\n')  
            printTicketList(dataDict) 
        elif inputNum == '2':
            ID = input('\nNow enter an ID: ') 
            if int(ID) in dataDict.keys(): 
                printTicket(dataDict, int(ID)) 
            else:
                print('\n---That is not a valid ID. Please retry at the main menu and enter a valid ID next time.---')  
                print('\n--------------------------------------\n')  


