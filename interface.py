from tkinter import *
from tkinter.filedialog import askopenfilename
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

fenetre = Tk()
fenetre.geometry("700x300")

label = Label(fenetre, text="Bienvenu sur le logiciel de régression linéaire\n\n"
                            "Cliquez sur l'un des deux boutons pour choisir quel "
                            "type de régression linéaire vous voulez utiliser", font=15)
label.pack()


def show_gradient():
    fenGradient = Tk()
    fenGradient.geometry("700x300")
    labelGradient = Label(fenGradient, text="Choisissez votre fichier de données", font=15)
    labelGradient.pack()

    with open("values.txt", "r") as f:
        x = list()
        y = list()
        for line in f:
            try:
                line = line.strip()
                data = line.split(chr(9))
                x.append(float(data[0]))
                y.append(float(data[1]))
            except:
                print("Erreur lecture fichier")
                x.clear
                y.clear



    f = Figure(figsize=(5, 5), dpi=100)
    a = f.add_subplot(111)
    a.scatter(x, y)
    a.plot()

    canvas = FigureCanvasTkAgg(f, fenGradient)
    canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

    canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)



    fenGradient.mainloop()



boutonGradient = Button(fenetre, text="Regression par descente de gradient", command=show_gradient)
boutonGradient.pack()


fenetre.mainloop()


