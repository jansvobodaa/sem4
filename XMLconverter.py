from xml.etree import ElementTree as ET
import csv


xml = ET.parse("uzivatele.xml")

f = open("uzivatele.csv",'w',encoding='utf-8')
zapis = csv.writer(f)

zapis.writerow(["vek", "jmeno","registrovan"])

for uzivatel in xml.findall("uzivatel"):
    if(uzivatel):
        vek = uzivatel.get("vek")
        jmeno = uzivatel.find("jmeno")
        reg = uzivatel.find("registrovan")
        radek= [jmeno.text, vek, reg.text]
        zapis.writerow(radek)
        print(radek)
f.close()  
