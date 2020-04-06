from bs4 import BeautifulSoup
from plyer import notification
import time
import requests


class Notification:
    def __init__(self):
        pass

    def notify(self, title, msg):
        notification.notify(title=title, message=msg, app_icon="icon.ico", timeout=10)

    def data_collect(self, url):
        a = requests.get(url)
        return a.text

    def parser(self):
        data = self.data_collect("https://www.mohfw.gov.in/")
        sp = BeautifulSoup(data, 'html.parser')
        my_data = ""
        for tr in sp.find_all('tbody')[0].find_all('tr'):
            my_data += tr.get_text()
        my_data = my_data[1:]
        items = my_data.split('\n\n')

        state_list = ["Bihar", "Delhi", "Haryana"]
        for item in items[0:30]:
            data1 = item.split("\n")
            if data1[1] in state_list:
                print(data1)
                nTitle = 'Update of COVID-19'
                ntext = f"State : {data1[1]}\nTotal Cases : {data1[2]}\nDischarged : {data1[3]}\nDeaths : {data1[4]}"
                self.notify(nTitle, ntext)
                time.sleep(2)


a = Notification()
a.parser()