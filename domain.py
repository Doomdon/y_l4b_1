import re





def domain_name(url):
    
    ''' Сравниваем url с регулярным выражением и записываем в переменную. После меняем символы. '''
    
    result = re.search(r'[./]?(?:www.)?\w+\-?\w+[.]', url)
    s = result[0]
    s = s.replace('www', '')
    s = s.replace('.', '')
    s = s.replace('/', '')
    return s


# тесты
assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"

print(domain_name("http://google.com"))
print(domain_name("http://google.co.jp"))
print(domain_name("www.xakep.ru"))
print(domain_name("https://youtube.com"))
