import urllib.request, urllib.error

input = open('names1.txt', 'r')            # Can be changed to whatever txtfile with skynet usernames.
output = open('websiteNames.txt', 'a')     # Can be changed to any blank txtfile or even an old one with previously checked web names.

def htmlCheck(url):
    try:
	    conn = urllib.request.urlopen(url)
		
    except urllib.error.HTTPError as e:
        response = "bad"
        #print('HTTPError: {}'.format(e.code))
    except urllib.error.URLError as e:
        #print('URLError: {}'.format(e.reason))
        response = "bad"
    else:
        #print('good')
        response = "good"
    return response	


while True:  
    text = input.readline()
	
    if not text:
	    break
		
    names = text.split()
	
    for username in names:
        #  # skynet.ie/~username/ name of website format
        url = ("http://www.skynet.ie/~"+username)
        result = htmlCheck(url)
        if result == 'good':
            output.write("Good: "  + url +"\n")
	
input.close()
output.close()
