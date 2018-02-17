import urllib.request, urllib.error

f = open('names1.txt', 'r')
output = open('websiteNames.txt', 'a')

def htmlCheck(url):
    try:
	    conn = urllib.request.urlopen(url)
		
    except urllib.error.HTTPError as e:
        kk = "bad"
        #print('HTTPError: {}'.format(e.code))
    except urllib.error.URLError as e:
        #print('URLError: {}'.format(e.reason))
        kk = "bad"
    else:
        #print('good')
        kk = "good"
    return kk	


while True:   # include a end conditional -- if not text: break   https://stackoverflow.com/questions/6277107/parsing-text-file-in-python
    text = f.readline()
    #print(text)
	
    if not text:
	    break
		
    names = text.split()
    #print(names)
	
    for list in names:
        #
        url = ("http://www.skynet.ie/~"+list)
        #print(""+url)
        result = htmlCheck(url)
        if result == 'good':
            #print("Good: "  + url)
            output.write("Good: "  + url +"\n")
			
	
	
f.close()


	


	



# skynet.ie/~username/ name of website format