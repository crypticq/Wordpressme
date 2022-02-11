#/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import warnings
import pyfiglet
import argparse


class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

warnings.filterwarnings('ignore', message='Unverified HTTPS request')

banner = pyfiglet.figlet_format("Wordpressme ")
print(banner)
print('Wordpress checker ..')
print('Coded By Eng Yazeed , Happy hacking')
print('target Region ex , ir , file to save  ... ')

link = []

cookies = {
    'SUID': 'M',
    'MUIDB': '30E2147FEC586F712E4C0538ED8A6EB0',
    '_EDGE_V': '1',
    'SRCHD': 'AF=NOFORM',
    'SRCHUID': 'V=2&GUID=6902FE94E7B8400BBE634DB5C66AF96A&dmnchg=1',
    'SRCHUSR': 'DOB=20220210&T=1644468118000',
    'SRCHHPGUSR': 'SRCHLANG=en&BRW=W&BRH=S&CW=1440&CH=510&SW=1440&SH=900&DPR=1&UTC=-300&DM=1&HV=1644468353&EXLTT=13&WTS=63780064957',
    '_HPVN': 'CS=eyJQbiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyMi0wMi0xMFQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIkRmdCI6bnVsbCwiTXZzIjowLCJGbHQiOjAsIkltcCI6Mn0=',
    '_RwBf': 'ilt=18&ihpd=1&ispd=17&rc=85&rb=0&gb=0&rg=200&pc=80&mtu=0&rbb=0&g=0&cid=&clo=0&v=18&l=2022-02-09T08:00:00.0000000Z&lft=20220209&aof=0&o=2&p=&c=&t=0&s=0001-01-01T00:00:00.0000000+00:00&ts=2022-02-10T04:45:53.2773532+00:00&rwred=0',
    'BCP': 'AD=1&AL=1&SM=1',
    '_EDGE_S': 'SID=1F4AC9DDDC46680E1FF8D89ADD94698B',
    '_SS': 'R=85&RB=0&GB=0&RG=200&RP=80',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:96.0) Gecko/20100101 Firefox/96.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0',
}


def wordpressme(site):
    r = requests.get(f"http://{site}" , headers=headers, verify=False)
    s = BeautifulSoup(r.text , 'lxml')
    try:
        for link in s.findAll('link'):
            f = link.get('href')
            if "plugins" in f:
                print(style.CYAN + '[*] Found wordpress site ... [*] ')
                print(style.GREEN+ f"http://{site}")
    except:
        pass 




def main(region , file):

    i = 0
    while i <= 1001:
        i = i + 11
        params = (
            ('q', f'site:{region} author/admin'),
            ('qs', 'n'),
            ('sp', '-1'),
            ('pq', f'site:{region} author/admin'),
            ('sc', '0-20'),
            ('sk', ''),
            ('cvid', 'B3DC30D3DE8F4539AFE32F4E3D908774'),
            ('first', i),
            ('FORM', 'PERE'),
        )

        response = requests.get('http://www.bing.com/search', headers=headers, params=params, cookies=cookies)
       
        s = BeautifulSoup(response.text , 'lxml')

        for s in s.findAll('a'):
            try:
                
                x = s.get('href')
                sit = []
                condition = 'https'
                if 'https' in x and x not in sit:
                    sit.append(x)
                    for http in sit:
                        f = http.split("/")[2]
                        if region in f:

                            with open(file , 'a') as infile:
                                infile.write("\n")
                                infile.write(f)
                            wordpressme(f)
            
            except:

                pass
        

                
def get_args():
    parser = argparse.ArgumentParser(description='Dns enumeration')
    parser.add_argument('-r', '--region', dest="region", required=True, action='store', help='Target Region for example .ir ')
    parser.add_argument('-f', '--file', dest="file", required=True, action='store', help='fie name to save output.')

    args = parser.parse_args()
    return args

args = get_args()
region = args.region
fileo = args.file

if __name__ == '__main__':
    main(region , fileo)
    print(style.RED + f'Websites Saved at {fileo}') 
