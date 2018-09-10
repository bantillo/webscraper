from bs4 import BeautifulSoup
import requests
import re

bethematch = "https://bethematch.org/tcdirectory/search/advanced/"

halo = requests.get(bethematch)
page = BeautifulSoup(halo.content, 'lxml')

scripts = page.find_all('script')

for script in scripts:
    if 'tcDirectory.bind' in script.text:
        results = script.text
        print("RESULTS", results, '\n\n\n\n')
        temp = results.split('request:', 1)[1]
        data = temp.split('Metadata')

title = ' '
url = ' '
for entry in data:
        results = entry.split(',')

        print(title, ', ', url, '\n\n')

        for result in results:

            result = result.replace('"', '')
            result = result.replace('\\u0026', '')
            result = result.replace('\\u0027s', '')
            if 'Title' in result:
                title = result.split(':', 1)[1]

            if 'AbsoluteUrlEncoded' in result:
                url = result.split(':', 1)[1]

# call second function with url as argument


    # call the second page here

        #halo = requests.get(url)
        #page = BeautifulSoup(halo.content, 'lxml')

        #print("NEW PAGE: ", page)







#print('TEMP FIRST: ', data[0], '\n\n')

#print('TEMP LAST: ', data[len(data) - 2], '\n\n')

#print('TEMP LAST: ', data[len(data) - 1], '\n\n')


print('NUM RESULTS: ', len(data))





print("COMPLETE")
