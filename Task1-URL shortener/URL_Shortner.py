import requests

def shorten_link(full_link, link_name):
    API_KEY = "API KEY"
    BASE_URL = 'https://cutt.ly/api/api.php'

    payload = {'key': API_KEY, 'short': full_link, 'name': link_name}
    request = requests.get(BASE_URL, params=payload)
    data = request.json()

    print('')

# shorten_link('https://www.google.com/search?q=apples', 'appdsjrgfius')

    try:
        title = data['url']['title']
        short_link = data['url']['shortLink']

        print('Title:', title)
        print('Link:', short_link)
    except:
        status = data['url']['status']
        print('Error Status:', status)


link = input('Enter a Link ---> ')
name = input('Give your link name ---> ')

shorten_link(link, name)







