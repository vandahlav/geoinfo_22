from PIL import Image, ImageOps
from math import inf

#potřebuju nastavit práh a window size a taky by bylo fajn mít obrázek
threshold = 3500
window_size = 3
image = "D:\Škůla\PřF UK\Geoinformatka\geoinfo_22\lena.tif" #PAK UPRAV

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

    min_intens = inf
    suma_diff = []
    
    #iterovat x a y (respektive řádky a sloupce tady?)
    """
    for colum in něco
    for row in něco?
    najednou by to asi neštymovalo...
    """

    #iterate přes každý pixel pro to okno
    for pixel in u_v:

        sq_diff = []

        #intenzita rohovitosti je suma druhých mocnin z rozdílu intenzit těch dvou pixelů
        for vector in u_v:

            squared_diff = (image)  #takhle to asi nestačí...
            
            """
            #to okno asi úplně na jednom místě nebude, nějak ho posuň
            shift_x = řádek + pixel [0]+ vector [0]
            shift_y = sloupec + pixel [1] + vector [1]

            kde vezmu ten řádek a sloupec??
            """
            
            #squared_diff by se měla taky někam ukládat?
            sq_diff.append(squared_diff)

        #rozdíly intenzit si potřebuješ na sumu uložit - seznam?

        suma_diff.append(sq_diff)

#změna intenzty v bodě je minimální změnou intenzity ve všech směrech
#pokud je intenzita < než prah, pak  se nastaví na nulu - na něco inicializovat! nekonečno?
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
def write_edge_coords (image, output_file):
    with open(output_file, "w") as file:
        for i in image:
            line = str(i[0]) + ", " + str(i[1])
            file.write(line)

output = "D:\Škůla\PřF UK\Geoinformatka" #PAK UPRAV
write_edge_coords (edges, output)

#nebylo by fajn si to taky pak nějak vizualizovat?