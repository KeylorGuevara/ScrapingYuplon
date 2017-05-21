# encoding: utf-8

import urllib
from bs4 import BeautifulSoup
from unidecode import unidecode
import operator


listaDeObjetos=[]#lista final con los objetos creados

def crearObjeto(listaAux,listaAux2):
    miDiccionario= dict(zip(listaAux2,listaAux))
    #Agregamos el objeto a la lista donde se encuentran todos almacenados
    global listaDeObjetos
    listaDeObjetos.append(miDiccionario)
    #for clave, valor in miDiccionario.items():
    #    print "%s -> %s" % (clave, valor)
    print len(listaDeObjetos)

    i=0
    for dic in listaDeObjetos:
        print listaDeObjetos[i]
        i+=1

def obtenerDatos():
    n = 1
    for i in range(10):
        url = "http://www.yuplon.com/heredia/Ofertas-y-Descuentos/detalle/{0}".format(i+82862) #pagina Random de Yuplon

        # listas necesarias para manejo de los datos
        listaAuxliar = []  # lista que se llenara para convertirse en un objeto y guardarlo en la lista de objetos
        listaAuxliar2 = []

        html = urllib.urlopen(url)  # link de la pagina de la que tomaremos los datos
        bsObj = BeautifulSoup(html, "lxml")  # objeto de la clase bs4

        for child in bsObj.findAll("div", {"id": "main-right-content"}):  # para poder tomar la imagen del libro
            listaParaImagen = child.find("div", {"id": "slideshow"}).findAll("img", {"alt": ""})#Obtenemos la imagen de la pagina, como son varias por anuncio, solo escogemos 1

            for valor in listaParaImagen:#tomamos la primer imagen encontrada
                imagenActual=listaParaImagen[0]
                break



            listaDeInfo = child.find("div", {"id": "main-right-yellowbox"}).findAll("span")#Lista donde se almacenan el resto de los datos requeridos
            m = 0
            contador=0
            for element in listaDeInfo:
                if contador<10:
                    str1 = "key{0}".format(m)
                    valorActual=listaDeInfo[m]
                    valorActualText= valorActual.get_text()
                    listaAuxliar2.append(str1)
                    t = unidecode(valorActualText)
                    t.encode("ascii")
                    listaAuxliar.append(t)
                    m+=1
                    contador+=1
                else:
                    break
            str1 = "key{0}".format(m)

            #almacenamos por separado la imagen
            imagenString= imagenActual.get('src').encode('utf-8')
            listaAuxliar.append(str(imagenString))
            listaAuxliar2.append(str1)


            crearObjeto(listaAuxliar,listaAuxliar2)#Llamamos al metodo que crea el diccionario
        print (n, "------------------------------------------------------------------------------------------------")
        n=n+1
    

if __name__ == '__main__':
    obtenerDatos()