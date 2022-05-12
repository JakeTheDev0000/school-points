import PySimpleGUI as sg
import os, time
import threading
import winsound

def startUp():
    layout1 = [
        [sg.Text("starting up...", size=(30, 1), font=("Helvetica", 20), justification="center")],
        [sg.ProgressBar(100, orientation="h", size=(30, 20), key="progressbar")]

    ]
    window = sg.Window("Starting up...", layout1, keep_on_top=False, grab_anywhere=True, no_titlebar=True, element_justification="center", finalize=True)
    progressbar = window.FindElement("progressbar")
    progressbar.UpdateBar(0)
    
    def backgroundThings():
        try:
            global pointsFile
            pointsFile = open("src/points.txt", "r+")
            progressbar.UpdateBar(50)
            time.sleep(0.5)
            progressbar.UpdateBar(90)
            time.sleep(0.1)
            progressbar.UpdateBar(100)
        except:
            sg.popup("Error: points.txt not found. \nPlease create it and try again.\np.s. its should be in the src folder. and should be named points.txt")
    backgroundThings()
    window.close()
    main()

def main():
    global pointsFile

    pay = {
        "math1": 15,
        "math2": 30,
        "english1": 60,
        "science1": 30,        
        "history1": 30,
        "religion1": 60,
        "vocab1" : 15,
        "spelling1": 60,
    }

    buy = {
        "15 minutes": 15,
        "30 minutes": 30,
        "45 minutes": 45,
        "1 hour": 60,
        "1.5 hours": 90,
        "2 hours": 120,
        "2.5 hours": 150,
        "3 hours": 180,
        "3.5 hours": 210,
        "4 hours": 240,
    }

    layoutCol2 = [
        [sg.Text("Points:", size=(10, 1), font=("Helvetica", 20), justification="center"), sg.Text(text=pointsFile.read(), size=(10, 1), font=("Helvetica", 20), justification="center", key="points")],
    ]

    layoutCol1 = [
        [sg.Button("math quiz", size=(10, 1), font=("Helvetica", 20), key="math1")],
        [sg.Button("math test", size=(10, 1), font=("Helvetica", 20), key="math2")],
        [sg.Button("english test", size=(10, 1), font=("Helvetica", 20), key="english1")],
        [sg.Button("science test", size=(10, 1), font=("Helvetica", 20), key="science1")],
        [sg.Button("history test", size=(10, 1), font=("Helvetica", 20), key="history1")],
        [sg.Button("religion test", size=(10, 1), font=("Helvetica", 20), key="religion1")],
        [sg.Button("vocab quiz", size=(10, 1), font=("Helvetica", 20), key="vocab1")],
        [sg.Button("spelling test", size=(10, 1), font=("Helvetica", 20), key="spelling1")],
    ]

    layout = [
        [sg.Titlebar(title="school milestones", font=("Helvetica", 10))],
        [sg.Text("Welcome to the Point Tracker!", size=(30, 1), font=("Helvetica", 20), justification="center")],
        [sg.Column(layoutCol1, element_justification="left"), sg.Column(layoutCol2, element_justification="right")],
    ]
    window = sg.Window("Point Tracker", layout, keep_on_top=False, element_justification="center", finalize=True)
    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        if event == "math1":
            winsound.Beep(343, 500)
            pointsFile.seek(0)
            points = int(pointsFile.read())
            pointsFile.seek(0)
            pointsFile.write(str(points + pay["math1"]))
            sg.popup("You earned " + str(pay["math1"]) + " points!")
            
            # now update the points on the GUI
            window.FindElement("points").Update(str(points))
        if event == "math2":
            winsound.Beep(343, 500)
            pointsFile.seek(0)
            points = int(pointsFile.read())
            pointsFile.seek(0)
            pointsFile.write(str(points + pay["math2"]))
            sg.popup("You earned " + str(pay["math2"]) + " points!")
            
            # now update the points on the GUI
            window.FindElement("points").Update(str(points))
        if event == "english1":
            winsound.Beep(343, 500)
            pointsFile.seek(0)
            points = int(pointsFile.read())
            pointsFile.seek(0)
            pointsFile.write(str(points + pay["english1"]))
            sg.popup("You earned " + str(pay["english1"]) + " points!")
            
            # now update the points on the GUI
            window.FindElement("points").Update(str(points))
        if event == "science1":
            winsound.Beep(343, 500)
            pointsFile.seek(0)
            points = int(pointsFile.read())
            pointsFile.seek(0)
            pointsFile.write(str(points + pay["science1"]))
            sg.popup("You earned " + str(pay["science1"]) + " points!")
            
            # now update the points on the GUI
            window.FindElement("points").Update(str(points))
        if event == "history1":
            winsound.Beep(343, 500)
            pointsFile.seek(0)
            points = int(pointsFile.read())
            pointsFile.seek(0)
            pointsFile.write(str(points + pay["history1"]))
            sg.popup("You earned " + str(pay["history1"]) + " points!")
            
            # now update the points on the GUI
            window.FindElement("points").Update(str(points))
        if event == "religion1":
            winsound.Beep(343, 500)
            pointsFile.seek(0)
            points = int(pointsFile.read())
            pointsFile.seek(0)
            pointsFile.write(str(points + pay["religion1"]))
            sg.popup("You earned " + str(pay["religion1"]) + " points!")
            
            # now update the points on the GUI
            window.FindElement("points").Update(str(points))
        if event == "vocab1":
            winsound.Beep(343, 500)
            pointsFile.seek(0)
            points = int(pointsFile.read())
            pointsFile.seek(0)
            pointsFile.write(str(points + pay["vocab1"]))
            sg.popup("You earned " + str(pay["vocab1"]) + " points!")
            
            # now update the points on the GUI
            window.FindElement("points").Update(str(points))
        if event == "spelling1":
            winsound.Beep(343, 500)
            pointsFile.seek(0)
            points = int(pointsFile.read())
            pointsFile.seek(0)
            pointsFile.write(str(points + pay["spelling1"]))
            sg.popup("You earned " + str(pay["spelling1"]) + " points!")
            
            # now update the points on the GUI
            window.FindElement("points").Update(str(points))





        


    pass

if __name__ == '__main__':
    startUp()