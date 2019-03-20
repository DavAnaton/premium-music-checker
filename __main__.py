import requests
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style

sites = [
	{
		'name': 'Spotify - IL',
		'url': 'https://www.spotify.com/il/premium/',
		'selector': ["p", {"class": "subhead bellow-headline"}],
		'expectation': 'Try Premium free for 30 days. Only ₪19.90/month after.*'
	},
	{
		'name': 'Spotify - FR',
		'url': 'https://www.spotify.com/fr/premium/',
		'selector': ["p", {"class": "subhead bellow-headline"}],
		'expectation': 'Essayez Spotify Premium gratuitement pendant 30 jours. Seulement 9,99 €/mois ensuite.*'
	},
	{
		'name': 'Spotify - EN',
		'url': 'https://www.spotify.com/en/premium/',
		'selector': ["p", {"class": "subhead bellow-headline"}],
		'expectation': 'Try Premium free for 30 days. Only ₪19.90/month after.*'
	},
	{
		'name': 'Deezer - FR',
		'url': 'https://www.deezer.com/fr/offers/',
		'selector': ["div", {"class": "offers-link"}],
		'expectation': 'Essayer pendant 30 jours'
	},
	{
		'name': 'Deezer - EN',
		'url': 'https://www.deezer.com/en/offers/',
		'selector': ["div", {"class": "offers-link"}],
		'expectation': 'Start your 30 day trial'
	}
]
for site in sites:
	page = requests.get(site['url'])
	soup = BeautifulSoup(page.content, 'html.parser')
	price_line = soup.find(*site['selector'])
	result = price_line.getText().strip()
	if 'clean_function' in site:
		result = site['clean_function'](result)
	if result == site['expectation']:
		print(Fore.RED + site['name'] + Style.RESET_ALL)
	else:
		print(Fore.GREEN + site['name'] + '\n\t' + result + Style.RESET_ALL)
