import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
# import pywhatkit as kit
import smtplib
# import phonenumbers
# import sports
import time
import cv2
import sys
import psutil
import PyPDF2
# from plyer import notification
# from phonenumbers import geocoder
# from phonenumbers import carrier

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")

    elif hour>=12 and hour<18:
        speak("good afternoon!")

    else:
        speak("good evening!")

    speak("I am Autobot 2point0. please tell me how may i help you?")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('YOUR GMAIL HERE', 'YOUR PASS HERE')
    server.sendmail('YOUR GMAIL HERE', to, content)
    server.close()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        speak("Say that again plaese...")
        return "None"
    return query

# def phoneNumber(): 
#     speak("Sir,please enter the mobile number you want to track")
#     number = input("Enter the mobile number you want to track: ")
#     ch_nmber = phonenumbers.parse(number, "CH")
#     speak(geocoder.description_for_number(ch_nmber, "en"))
#     print(geocoder.description_for_number(ch_nmber, "en"))

#     service_nmber = phonenumbers.parse(number, "RO")
#     speak(carrier.name_for_number(service_nmber, "en"))
#     print(carrier.name_for_number(service_nmber, "en"))

def pdf_reader():
    book = open('python.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(book) 
    pages = pdfReader.numPages
    speak(f"Total numbers of pages in this book {pages} ")
    speak("sir please enter the page number i have to read")
    pg = int(input("Please enter the page number: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)

# def cricketScore():
#     try:
#         i=sports.get_match(cricket, india, mumbai)
#         notification.notify(
#             title="Cricket Score Updates",
#             message=str(i),
#             timeout=10,
#         )
#         time.sleep(10)
#         speak("Sir,i sent you a notification of live cricket score")

#     except Exception as f:
#                 speak("Sorry sir there is no live cricket match for india or mumbai")


if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif "open notepad" in query:
            npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad"
            os.startfile(npath)

        # elif "song on youtube" in query:
        #     kit.playonyt("see you again")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"sir, the time is {strTime}")

        elif 'open code'  in query:
            codePath = "C:\\Users\\Mayur\\AppData\\Local\\Programs\\Microsoft VS Code\\Code"
            os.startfile(codePath)

        # elif 'send whatsapp' in query:
        #     pywhatkit.sendwhatmsg('+91MOBILE NO HERE', 'Hiii',17 ,5)

        elif 'open dev'  in query:
            devPath = "C:\\Program Files (x86)\\Dev-Cpp\\devcpp"
            os.startfile(devPath)   

        elif "open command prompt" in query:
            os.system("start cmd")

             #to close any application
        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")
        
        # To take screenshot 
        elif "take screenshot" in query or "take a screenshot" in query:
            speak("sir, please tell me the name for this screenshot file")
            name = takeCommand()
            speak("please sir hold the screen for few seconds, i am taking sreenshot")
            time.sleep(3)
            # img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir, the screenshot is saved in our main folder. now i am ready for next command")
        
        #To shutdown system
        elif "shutdown the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        #to set an alarm
        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn==22: 
                music_dir = 'D:\\My music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))
        
        #To check battery percentage 
        elif "how much power left" in query or "how much power we have" in query or "battery" in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"Sir our sysytem have {percentage} percent battery")
            if percentage>=75:
                speak("we have enough power to continue our work")
            elif percentage>=40 and percentage<=75:
                speak("we should connect our system to charging point to charge our battery")
            elif percentage<=15 and percentage>=30:
                speak("we dont have enough power to work, please connect to charging")
            elif percentage<=10:
                speak("we have very low power, please connect to charging the system will shutdown very soon")
        
        #To Read PDF file or book
        elif "read pdf" in query or "read book" in query:
                pdf_reader()

        elif 'open spotify'  in query:
            spoPath = "C:\\Users\\Mayur\\Desktop\\Spotify.lnk"
            os.startfile(spoPath)


        elif 'send email' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "GMAIL HERE"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir, i am unable to send this email")

        # elif 'track mobile number' in query:
        #     phoneNumber()

        # elif 'cricket score' in query:
        #     cricketScore()

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif 'play songs' in query:
            songPaath = "C:\\Users\\Mayur\\Downloads\\AabaadBarbaad.mp3"
            os.startfile(songPaath)

        elif 'no thanks' in query:
            speak("thank you for using me sir, Have a good day.")
            sys.exit()