#git test


from selenium import webdriver
tab1 = ["a", "b", "c", "c"]
tab2 = ["c", "d"]

dik={'klucz1': "aaa", 'klucz2': "bbb", 'klucz3': "ccc"}

print(dik['klucz1'])

for i in dik.keys():
    print(dik[i])


lal=""
if lal:
    print("lalala")




"""
for i in tab1:
    #zmienna = i.low()
    if i.lower() in tab2:
        print("powtorka")
    else:
        print("spoklo")



a="a"
b="b"
c="c"
tab = [a, c, c]

if b in tab:
    print("jest")
   # print(tab)



browser = webdriver.Chrome('D:\projektyPython\chromedriver')
browser.get('https://www.seleniumhq.org/')

#elem = browser.find_element_by_link_text('Download')
elem = browser.find_element_by_partial_link_text('Download')
print(elem.get_attribute('href'))
#elem.click()
#x = elem
#print(x)





series_urls = {}

print(type(series_urls))

#[print(d) for d in tab]



class auto():

    def __init__(self, kola, silnik):
        self.kola = kola
        self.silnik = silnik


samochod1=auto(6, "lpg")
samochod2=auto(8, "diesel")
#print(samochod1.kola)
#print(samochod1.silnik)

tab=[samochod1, samochod2]
if samochod1 in tab:
    print("jest")
"""

#kolka = [c.kola for c in tab]
#print(kolka)
#kolka=[]

#for c in tab:
 #   kolka.append(c.kola)

#print(kolka)


