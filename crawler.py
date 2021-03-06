#! /usr/bin/python2.7
from bs4 import BeautifulSoup
import urllib2

class Crawler:
    def __init__(self):
        self.count = 0

    def mostrarConfig(self):
        print "Direccion url: "
        print self.url
        print "Profundidad: "
        print self.profundidad

    def recuperarInf(self,url,prof):
        html = self.obtenerHtml(url)
        soup = BeautifulSoup(html,'html.parser')

        if prof == 0:
            data = soup.get_text()
            print data
            self.count += 1

        if prof > 0:
            data = soup.get_text()
            print data
            self.count += 1
            paginas = self.obtenerPag(soup)
            for pagina in paginas:
                niv = prof
                self.recuperarInf(pagina,niv-1)

    def obtenerPag(self,soup):
        res = []
        for url in soup.find_all('a'):
            res.append(url.get('href'))
        return res


    def obtenerHtml(self,url):
        html = str(urllib2.urlopen(url).read()) 
        return html






