import requests
from bs4 import BeautifulSoup

response = requests.get('http://naver.com')
dom = BeautifulSoup(response.text, 'html.parser')
rank_table_element = dom.select_one("#realrank")
rank_elements = rank_table_element.select('li a')
for i in rank_elements:
    #
    # rank_element 하나는 bs4.element.tag객체,  attrs는
    # 태그의 attribute(속성)을 dictionary 형태로 가져온다.
    #
    print(i.attrs['title'])
