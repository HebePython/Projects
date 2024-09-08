from bs4 import BeautifulSoup as bs
import requests, os, sys
from datetime import datetime

class AlJazeera:
    def __init__(self, url):
        article = requests.get(url).text
        self.soup = bs(article, "html.parser")
        self.body = self.get_body()
        self.title = self.get_title()

    def get_body(self) -> str:
        body = self.soup.find(id='main-content-area' )
        body = [p.text for p in body.find_all('p')]
        return str('\n'.join(body))

    def get_title(self) -> str:
        return self.soup.find('h1').text

class BBC:
    def __init__(self, url):
        article = requests.get(url).text
        self.soup = bs(article, "html.parser")
        self.body = self.get_body()
        self.title = self.get_title()

    def get_body(self) -> str:
        body =  self.soup.find(id='main-content')
        exclude_classes = ['footnote', 'footer__copyright-text', 'PromoHeadline', 'ssrcss-17zglt8-PromoHeadline exn3ah96', 'PromoLink']
        body = self.soup.find_all('p', class_=lambda x: all(exclude not in x for exclude in exclude_classes))
        body = [p for p in body if not p.find('a')]
        body = [p for p in body if not p.find('span')]
        return'\n'.join(sentence.get_text(separator=" ", strip=True) for sentence in body)

    def get_title(self) -> str:
        return self.soup.find('h1').text

def main():

    while True:
        try:
            url = input("Please input an article from BBC or Al Jazeera or simply press enter to exit: ")

            if 'aljazeera.com' in url.lower():
                parsed = AlJazeera(url)
                folder_name = "AlJazeera"
            elif "bbc.com" in url.lower():
                parsed = BBC(url)
                folder_name = "BBC"
            else:
                sys.exit("shutting down...")
        except requests.exceptions.MissingSchema as e:
             print(f"Missing URL schema: {e}")
        else:
            break

    make_txt(parsed.title, parsed.body, url, datetime.today().strftime("%Y-%m-%d"), folder_name)

def make_txt(title, s, source, date_today, folder_name):

    folder_path = os.path.join(os.getcwd(), folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        
    file_path = os.path.join(folder_path, f"{title}.txt")

    if os.path.exists(f"{file_path}"):
        print("Duplicate articles are not permitted.")
    else:
        with open(f"{file_path}", 'w') as file:
            file.write(s)

        with open('Sources', 'a') as s_file:
            s_file.write(source + f', Date: {date_today}' + '\n')



if __name__ == ("__main__"):
    main()
