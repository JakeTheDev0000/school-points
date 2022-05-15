import PySimpleGUI as sg
import time
from playsound import playsound
import sys

version = "0.4.0"
masterPassword = "hi123"

global pointsFile
global wantsSound
wantsSound = True

# pay = {
#     "math1": 15,
#     "math2": 30,
#     "english1": 60,
#     "science1": 30,        
#     "history1": 30,
#     "religion1": 60,
#     "vocab1" : 15,
#     "spelling1": 60,
# }

# buy = {
#     "15 minutes": 15,
#     "30 minutes": 30,
#     "45 minutes": 45,
#     "1 hour": 60,
#     "1.5 hours": 90,
#     "2 hours": 120,
#     "2.5 hours": 150,
#     "3 hours": 180,
#     "3.5 hours": 210,
#     "4 hours": 240,
# }

def startUp(args1):
    def normalStart():
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
                progressbar.UpdateBar(30)
                time.sleep(0.5)
                progressbar.UpdateBar(60)
                time.sleep(0.1)
                progressbar.UpdateBar(99)
                time.sleep(0.1)
                time.sleep(0.1)
                progressbar.UpdateBar(100)
            except:
                sg.popup("Error: points.txt not found. \nPlease create it and try again.\np.s. its should be in the src folder. and should be named points.txt")
        backgroundThings()
        window.close()
        main()
    def commandLineStart():
        print("starting up...")
        time.sleep(0.5)
        pointsFile = open("src/points.txt", "r+")
        print("30%")
        time.sleep(0.1)
        print("60%")
        time.sleep(0.1)
        timeFile = open("src/time.txt", "r+")
        print("99%")
        global time2
        time2 = timeFile.read()
        time2 = int(time2)
        time.sleep(0.1)
        print("100%")
        global points2
        points2 = int(pointsFile.read())
        time.sleep(0.1)
        print("done")
        def cmdmain():
            global time2
            global points2
            print("\n\nyou have: " + str(points2) + " points\nyou have "+str(time2 / 60)+" hours/min\n\n")
            print("1. get points\n2. buy time\n3. remove points\n4. add points\n5. exit")
            choice1 = input("\n\n>>>")
            if choice1 == "1":
                print("\n1. math quiz - 15\n2. math test - 30\n3. english test - 60\n4. science test - 30\n5. history test - 30\n6. religion test - 60\n7. vocab test - 15\n8. spelling test - 60\n9. exit")
                choice2 = input("\n\n>>>")
                if choice2 == "1":
                    pointsFile.seek(0)
                    points = int(pointsFile.read())
                    pointsFile.seek(0)
                    pointsFile.write(str(points + 15))
                    pointsFile.truncate()
                    print("\n\n+15 points")
                    points2 += 15
                    cmdmain()
                elif choice2 == "2":
                    pointsFile.seek(0)
                    points = int(pointsFile.read())
                    pointsFile.seek(0)
                    pointsFile.write(str(points + 30))
                    pointsFile.truncate()
                    print("\n\n+30 points")
                    points2 += 30
                    cmdmain()
                elif choice2 == "3":
                    pointsFile.seek(0)
                    points = int(pointsFile.read())
                    pointsFile.seek(0)
                    pointsFile.write(str(points + 60))
                    pointsFile.truncate()
                    print("\n\n+60 points")
                    points2 += 60
                    cmdmain()
                elif choice2 == "4":
                    pointsFile.seek(0)
                    points = int(pointsFile.read())
                    pointsFile.seek(0)
                    pointsFile.write(str(points + 30))
                    pointsFile.truncate()
                    print("\n\n+30 points")
                    points2 += 30
                    cmdmain()
                elif choice2 == "5":
                    pointsFile.seek(0)
                    points = int(pointsFile.read())
                    pointsFile.seek(0)
                    pointsFile.write(str(points + 30))
                    pointsFile.truncate()
                    print("\n\n+30 points")
                    points2 += 30
                    cmdmain()
                elif choice2 == "6":
                    pointsFile.seek(0)
                    points = int(pointsFile.read())
                    pointsFile.seek(0)
                    pointsFile.write(str(points + 60))
                    pointsFile.truncate()
                    print("\n\n+60 points")
                    points2 += 60
                    cmdmain()
                elif choice2 == "7":
                    pointsFile.seek(0)
                    points = int(pointsFile.read())
                    pointsFile.seek(0)
                    pointsFile.write(str(points + 15))
                    pointsFile.truncate()
                    print("\n\n+15 points")
                    points2 += 15
                    cmdmain()
                elif choice2 == "8":
                    pointsFile.seek(0)
                    points = int(pointsFile.read())
                    pointsFile.seek(0)
                    pointsFile.write(str(points + 60))
                    pointsFile.truncate()
                    print("\n\n+60 points")
                    points2 += 60
                    cmdmain()
                elif choice2 == "9":
                    cmdmain()
            elif choice1 == "2":
                print("\nyou have " + str(points2) + " points\n1 point = 1 min\n")
                print("\n1. 15 minutes\n2. 30 minutes\n3. 45 minutes\n4. 1 hour - 60\n5. 1.5 hours - 90\n6. 2 hours - 120\n7. 2.5 hours - 150\n8. 3 hours - 180\n9. 3.5 hours - 210\n10. 4 hours - 240\n11. exit")
                choice3 = input("\n\n>>>")
                if choice3 == "1":
                    pointsFile.seek(0)
                    points = int(pointsFile.read())
                    pointsFile.seek(0)
                    pointsFile.write(str(points - 15))
                    pointsFile.truncate()
                    print("\n\n-15 points\n+15 minutes")
                    points2 -= 15
                    time2 += 15
                    timeFile.seek(0)
                    timeFile.write(str(time2))
                    timeFile.truncate()
                    cmdmain()
                elif choice3 == "2":
                    pointsFile.seek(0)
                    points = int(pointsFile.read())
                    pointsFile.seek(0)
                    pointsFile.write(str(points - 30))
                    pointsFile.truncate()
                    print("\n\n-30 points\n+30 minutes")
                    points2 -= 30
                    time2 += 30
                    timeFile.seek(0)
                    timeFile.write(str(time2))
                    timeFile.truncate()
                    cmdmain()   
                elif choice3 == "3":
                    pointsFile.seek(0)
                    points = int(pointsFile.read())
                    pointsFile.seek(0)
                    pointsFile.write(str(points - 45))
                    pointsFile.truncate()
                    print("\n\n-45 points\n+45 minutes")
                    points2 -= 45
                    time2 += 45
                    timeFile.seek(0)
                    timeFile.write(str(time2))
                    timeFile.truncate()
                    cmdmain()  
                elif choice3 == "4":
                    pointsFile.seek(0)
                    points = int(pointsFile.read())
                    pointsFile.seek(0)
                    pointsFile.write(str(points - 60))
                    pointsFile.truncate()
                    print("\n\n-60 points\n+60 minutes")
                    points2 -= 60
                    time2 += 60
                    timeFile.seek(0)
                    timeFile.write(str(time2))
                    timeFile.truncate()
                    cmdmain()
                elif choice3 == "5":
                    pointsFile.seek(0)
                    points = int(pointsFile.read())
                    pointsFile.seek(0)
                    pointsFile.write(str(points - 90))
                    pointsFile.truncate()
                    print("\n\n-90 points\n+90 minutes")
                    points2 -= 90
                    time2 += 90
                    timeFile.seek(0)
                    timeFile.write(str(time2))
                    timeFile.truncate()
                    cmdmain()
                elif choice3 == "6":
                    pointsFile.seek(0)
                    points = int(pointsFile.read())
                    pointsFile.seek(0)
                    pointsFile.write(str(points - 120))
                    pointsFile.truncate()
                    print("\n\n-120 points\n+120 minutes")
                    points2 -= 120
                    time2 += 120
                    timeFile.seek(0)
                    timeFile.write(str(time2))
                    timeFile.truncate()
                    cmdmain()
                elif choice3 == "7":
                    pointsFile.seek(0)
                    points = int(pointsFile.read())
                    pointsFile.seek(0)
                    pointsFile.write(str(points - 150))
                    pointsFile.truncate()
                    print("\n\n-150 points\n+150 minutes")
                    points2 -= 150
                    time2 += 150
                    timeFile.seek(0)
                    timeFile.write(str(time2))
                    timeFile.truncate()
                    cmdmain()
                elif choice3 == "8":
                    pointsFile.seek(0)
                    points = int(pointsFile.read())
                    pointsFile.seek(0)
                    pointsFile.write(str(points - 180))
                    pointsFile.truncate()
                    print("\n\n-180 points\n+180 minutes")
                    points2 -= 180
                    time2 += 180
                    timeFile.seek(0)
                    timeFile.write(str(time2))
                    timeFile.truncate()
                    cmdmain()
                elif choice3 == "9":
                    pointsFile.seek(0)
                    points = int(pointsFile.read())
                    pointsFile.seek(0)
                    pointsFile.write(str(points - 210))
                    pointsFile.truncate()
                    print("\n\n-210 points\n+210 minutes")
                    points2 -= 210
                    time2 += 210
                    timeFile.seek(0)
                    timeFile.write(str(time2))
                    timeFile.truncate()
                    cmdmain()
                elif choice3 == "10":
                    pointsFile.seek(0)
                    points = int(pointsFile.read())
                    pointsFile.seek(0)
                    pointsFile.write(str(points - 240))
                    pointsFile.truncate()
                    print("\n\n-240 points\n+240 minutes")
                    points2 -= 240
                    time2 += 240
                    timeFile.seek(0)
                    timeFile.write(str(time2))
                    timeFile.truncate()
                    cmdmain()
                elif choice3 == "11":
                    cmdmain()
                pass
            elif choice1 == "3":
                howMuchRemoved1 = input("\nHow much do you want to remove?\nor type \'all\' for all to be zero\n\n>>> ")
                if howMuchRemoved1 == "all":
                    print("\n\nremoving all points...")
                    pointsFile.seek(0)
                    points = int(pointsFile.read())
                    pointsFile.seek(0)
                    pointsFile.write(str(0))
                    pointsFile.truncate()
                    print("All points removed")
                    points2 = 0
                    print("\n\nremoveing all time...")
                    timeFile.seek(0)
                    timeFile.write(str(0))
                    timeFile.truncate()
                    time2 = 0
                    print("All time removed")

                    cmdmain()
                else:
                    pointsFile.seek(0)
                    points = int(pointsFile.read())
                    pointsFile.seek(0)
                    pointsFile.write(str(points - int(howMuchRemoved1)))
                    pointsFile.truncate()
                    print("\n\n-", int(howMuchRemoved1), "points")
                    points2 -= int(howMuchRemoved1)
                    choice4 = input("\n\nDo you want to remove time too?\n1. Yes\n2. No\n\n>>> ")
                    if choice4 == "1":
                        howMuchRemoved2 = int(input("\nHow much do you want to remove?\n\n>>> "))
                        timeFile.seek(0)
                        time = int(timeFile.read())
                        timeFile.seek(0)
                        timeFile.write(str(time - howMuchRemoved2))
                        timeFile.truncate()
                        print("\n\n-", howMuchRemoved2, "minutes")
                        time2 -= howMuchRemoved2
                        cmdmain()
                    elif choice4 == "2":
                        cmdmain()
            elif choice1 == "4":
                passwordInput = input("\n\nEnter the master password:\n\n>>> ")
                if passwordInput == masterPassword:
                    howMuchRemovedAdded = int(input("\nHow much do you want to add?\n\n>>> "))
                    pointsFile.seek(0)
                    points = int(pointsFile.read())
                    pointsFile.seek(0)
                    pointsFile.write(str(points + howMuchRemovedAdded))
                    pointsFile.truncate()
                    print("\n\n+", howMuchRemovedAdded, "points")
                    points2 += howMuchRemovedAdded
                    choice4 = input("\n\nDo you want to add time too?\n1. Yes\n2. No\n\n>>> ")
                    if choice4 == "1":
                        howMuchRemovedAdded2 = int(input("\nHow much do you want to add?\n\n>>> "))
                        timeFile.seek(0)
                        time = int(timeFile.read())
                        timeFile.seek(0)
                        timeFile.write(str(time + howMuchRemovedAdded2))
                        timeFile.truncate()
                        print("\n\n+", howMuchRemovedAdded2, "minutes")
                        time2 += howMuchRemovedAdded2
                        cmdmain()
                    elif choice4 == "2":
                        cmdmain()
                else:
                    print("\n\nWrong password")
                    cmdmain()
            elif choice1 == "5":
                exit(0)

            pass
        cmdmain()

    print(args1)

    if args1 == ["--CMD"]:
        commandLineStart()
    elif args1 == ['--help']:
        sg.popup("--CMD: command line mode\n--help: this help message\n--version: version number\n--soundOn: turns on sound\n--soundOff: turns off sound")
    elif args1 == ["--version"]:
        sg.popup(f"Version: {version}")
    elif args1 == ["--soundOn"]:
        global wantsSound
        wantsSound = True
        normalStart()
    elif args1 == ["--soundOff"]:
        wantsSound = False
        normalStart()
    elif args1 == ["--pass"]:
        exit()
    else:
        normalStart()

def main():
    global pointsFile
    global wantsSound



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

    layoutCol3 = [
        [sg.Button("15 minutes", size=(10, 1), font=("Helvetica", 20), key="15min")],
        [sg.Button("30 minutes", size=(10, 1), font=("Helvetica", 20), key="30min")],
        [sg.Button("45 minutes", size=(10, 1), font=("Helvetica", 20), key="45min")],
        [sg.Button("1 hour", size=(10, 1), font=("Helvetica", 20), key="1hour")],
        [sg.Button("1.5 hours", size=(10, 1), font=("Helvetica", 20), key="1.5hour")],
        [sg.Button("2 hours", size=(10, 1), font=("Helvetica", 20), key="2hour")],
        [sg.Button("2.5 hours", size=(10, 1), font=("Helvetica", 20), key="2.5hour")],
        [sg.Button("3 hours", size=(10, 1), font=("Helvetica", 20), key="3hour")],
        [sg.Button("3.5 hours", size=(10, 1), font=("Helvetica", 20), key="3.5hour")],
        [sg.Button("4 hours", size=(10, 1), font=("Helvetica", 20), key="4hour")],
    ]

    layout = [
        [sg.Titlebar(title="school milestones", font=("Helvetica", 10))],
        [sg.Text("Welcome to the Point Tracker!", size=(30, 1), font=("Helvetica", 20), justification="center")],
        [sg.Column(layoutCol1, element_justification="left"), sg.Column(layoutCol2, element_justification="right"), sg.Column(layoutCol3, element_justification="left")],
    ]
    window = sg.Window("Point Tracker", layout, keep_on_top=True, element_justification="center", finalize=True)
    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == "Exit":
            break


        if event == "math1":
            # play sound src/audio/applause.mp3
            playsound("src\\audio\\applause.mp3", wantsSound)
            pointsFile.seek(0)
            points = int(pointsFile.read())
            pointsFile.seek(0)
            pointsFile.write(str(points + 15))
            pointsFile.truncate()

            # now update the points in the GUI
            window.FindElement("points").Update(str(points + 15))

            

    pass

if __name__ == '__main__':
    startUp(sys.argv[1:])