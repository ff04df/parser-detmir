HEADERS : dict[str, str] = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.6',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

MAX_PAGES : int = 200 # should be 200

CATALOGS : list[dict] = [
    {
        'name' : 'Игрушки и игры',
        'urls' : ['https://www.detmir.ru/catalog/index/name/konstruktory/',
                  'https://www.detmir.ru/catalog/index/name/kukly_i_aksessuary/',
                  'https://www.detmir.ru/catalog/index/name/myagkie_igrushki/'
                  'https://www.detmir.ru/catalog/index/name/transport/',
                  'https://www.detmir.ru/catalog/index/name/radioupravlyaemye_igrushki/',
                  
                #   'https://www.detmir.ru/catalog/index/name/rolevye_nabory/',
                
                  'https://www.detmir.ru/catalog/index/name/detskoe_oruzhie/',
                  'https://www.detmir.ru/catalog/index/name/posuda_toys/',
                  'https://www.detmir.ru/catalog/index/name/bitovaja_tehnika/',
                  'https://www.detmir.ru/catalog/index/name/professional/',
                  'https://www.detmir.ru/catalog/index/name/detskie_kuhni/',
                  'https://www.detmir.ru/catalog/index/name/play_store/',
                  'https://www.detmir.ru/catalog/index/name/beauty_salon/',
                  'https://www.detmir.ru/catalog/index/name/syuzhetno_rolevye_nabory/',
                  
                #   'https://www.detmir.ru/catalog/index/name/igrushki_dlya_malyshey/',
                
                  'https://www.detmir.ru/catalog/index/name/mashinki_dlya_malishey/',
                  'https://www.detmir.ru/catalog/index/name/musical_instruments_kids/',
                  'https://www.detmir.ru/catalog/index/name/razvivayushchie_kovriki/',
                  'https://www.detmir.ru/catalog/index/name/razvivayushchie/',
                  'https://www.detmir.ru/catalog/index/name/interaktivnye/',
                  'https://www.detmir.ru/catalog/index/name/pogremushki/',
                  'https://www.detmir.ru/catalog/index/name/katalki/',
                  'https://www.detmir.ru/catalog/index/name/developing_walker/',
                  'https://www.detmir.ru/catalog/index/name/mobili/',
                  'https://www.detmir.ru/catalog/index/name/nightlights_projectors/',
                  'https://www.detmir.ru/catalog/index/name/hanging_educational_toys/',
                  
                  'https://www.detmir.ru/catalog/index/name/muzulkalnye_instrumenty/',
                  'https://www.detmir.ru/catalog/index/name/playsets_figures/',
                  'https://www.detmir.ru/catalog/index/name/nastolnye_igry/',
                  'https://www.detmir.ru/catalog/index/name/appliances_childrens/',
                #   'https://www.detmir.ru/catalog/index/name/electronics_kids/',
                  
                  'https://www.detmir.ru/catalog/index/name/kids_tablet/',
                  'https://www.detmir.ru/catalog/index/name/detskie_komputery/',
                  'https://www.detmir.ru/catalog/index/name/cases-phones/',
                  'https://www.detmir.ru/catalog/index/name/naushniki/',
                  'https://www.detmir.ru/catalog/index/name/batteries1/',
                  'https://www.detmir.ru/catalog/index/name/trinkets/',
                  'https://www.detmir.ru/catalog/index/name/igry_xbox/',
                  'https://www.detmir.ru/catalog/index/name/labyrinth/',
                  'https://www.detmir.ru/catalog/index/name/game_walkie-talkies/',
                  'https://www.detmir.ru/catalog/index/name/camera/',
                  'https://www.detmir.ru/catalog/index/name/elektronnye_igry/',]
    },
    
    # ! other do by yourself
    
    {
        'name' : 'Гигиена и уход',
        'urls' : ['https://www.detmir.ru/catalog/index/name/household_chemicals/']
    },
    
    {
        'name' : 'Детская комната',
        'urls' : []
    },
    
    {
        'name' : 'Питание и кормление',
        'urls' : []
    },
    
    {
        'name' : 'Прогулки и путешествия',
        'urls' : []
    },
    
    {
        'name' : 'Одежда и обувь',
        'urls' : []
    },
    
    {
        'name' : 'Спорт и отдых',
        'urls' : []
    },
    
    {
        'name' : 'Школа',
        'urls' : []
    },
    
    {
        'name' : 'Хобби и творчество',
        'urls' : []
    },
    
    {
        'name' : 'Продукты для здоровья и спорта',
        'urls' : []
    },
    
    {
        'name' : 'Дом',
        'urls' : []
    },
    
    {
        'name' : 'Бытовая техника и электроника',
        'urls' : []
    },
    
    {
        'name' : 'Для родителей',
        'urls' : []
    },
    
    {
        'name' : 'Книги',
        'urls' : []
    },
]
