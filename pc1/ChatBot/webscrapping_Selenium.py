from webdriver_manager.chrome import  ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
ruta = ChromeDriverManager().install()
s = Service(ruta)
driver = webdriver.Chrome(service=s)
website = "https://rpp.pe/politica/gobierno/se-necesita-crear-mayor-conciencia-sobre-el-uso-de-plastico-y-migrar-a-otras-alternativas-dice-ministro-del-ambiente-noticia-1549363"
driver.get(website)
soup = BeautifulSoup(driver.page_source, 'html.parser')
titulo = soup.find("h1", class_="article__title").text 
print("TITULO DE NOTICIA: ", titulo)
driver.quit()


