from curl_cffi.requests import Session

from bs4 import BeautifulSoup

from openpyxl import Workbook
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE

import config

def valueFromString(s : str) -> str:
    s = s.replace(',', '.').replace('\u2009', '')
    
    wasDec = False
    start, end = 0, 0
    for en, i in enumerate(s):
        if not wasDec and i.isdecimal():
            start = en
            wasDec = True
            continue
        elif wasDec and (not i.isdecimal() and not i == '.'):
            end = en
            break
    return s[start:end] if end != 0 else '0'

def mainP():
    session = Session(headers = config.HEADERS, impersonate = 'chrome110')
    wb = Workbook()
    wb.remove(wb.active) # type: ignore
    
    for catalog in config.CATALOGS:
        if not catalog['name'] or not catalog['urls']:
            continue
        
        ws = wb.create_sheet(catalog['name'])
        ws.append(['Название', 'Цена', 'Цена с акцией', 'Ссылка'])
        for url in catalog['urls']:
            shouldForceNextUrl = False
            url : str
            
            
            print(url)
            
            for page in range(1, config.MAX_PAGES):
                if shouldForceNextUrl:
                    break
                
                print(f'{url}page/{page}')
                
                res = session.get(f'{url}page/{page}')
                if res.status_code != 200:
                    print(f'\n{url}\ngave code: {res.status_code}\n')
                    break
                
                for prod in BeautifulSoup(res.content, 'html.parser').select('section.H_1.H_5.B_9'):
                    name = prod.find('a', class_ = 'Ib')
                    link = name['href'] # type: ignore
                    name = name.text # type: ignore

                    try:
                        price = int(valueFromString(prod.find('span', class_ = 'bgu').text)) # type: ignore
                    except:
                        try:
                            price = int(valueFromString(prod.find('div', class_ = 'bgr').text)) # type: ignore
                        except:
                            shouldForceNextUrl = True
                            break
                    try:
                        price2 = int(valueFromString(prod.select_one('span.bgs.bgt').text)) # type: ignore
                    except:
                        price2 = 0
                    
                    try:
                        ws.append([name, price, price2, link])
                    except:
                        ws.append([ILLEGAL_CHARACTERS_RE.sub(r'', name), price, price2, link])
                        
    wb.save('out.xlsx')



if __name__ == '__main__':
    mainP()
