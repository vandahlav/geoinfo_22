from PIL import Image, ImageOps

#potřebuju nastavit práh a window size a taky by bylo fajn mít obrázek
threshold = 3500
window_size = 3
image = "lena.tif"

#vstupem do Moravce je šedotónový obraz, takže to převeď
def open_image(image):
    with Image.open(image) as im:
        return ImageOps.grayscale(im)

def moravec (image, window_size, threshold):

    #potřebuju mu říct, ať si načte picture
    im = open_image(image)

    #někam se musí uložit ty rohy 
    #seznam protože pak to chci do file? asi?
    edges_list = []

    #no a teď potřebuju, aby to procházelo pixely im tím oknem
    #v tom případě asi první potřebuje vědět, jak velký je, a že má nějaký vektory?
    u_v = [[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]

    
    suma_diff = []
    
    #iterate přes každý pixel pro to okno
    for pixel in u_v:

        sq_diff = []

        #intenzita rohovitosti je suma druhých mocnin z rozdílu intenzit těch dvou pixelů
        for vector in u_v:

            squared_diff = (image)  #takhle to asi nestačí...
            
            #to okno asi úplně na jednom místě nebude, nějak ho posuň
            
            #squared_diff by se měla taky někam ukládat?
            sq_diff.append(squared_diff)

        #rozdíly intenzit si potřebuješ na sumu uložit - seznam?

        suma_diff.append(sq_diff)

#změna intenzty v bodě je minimální změnou intenzity ve všech směrech
#pokud je intenzita < než prah, pak  se nastaví na nulu
#pokud je minimální intenzita >= prahu, je to roh
"""
if min_intens >= threshold:
    edges_list.append()

potřebuju přidat sloupce i řádky 

else:
    image[row, col] = 0
"""
edges = moravec(image, window_size, threshold)

#nezapomeň, že to potřebuješ taky uložit -> výstup je seznam pixel souřadnic bodů edges