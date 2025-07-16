try:
    import sys
    import os

    def OpenSites():
        try:
            import webbrowser
            from Program.Config.Config import telegram, gunslol
            webbrowser.open(f'https://t.me/Nexus0Project')
        except: pass

    if sys.platform.startswith("win"):
        os.system("cls")
        print("Installing the python modules required for the RedTiger Tool:\n")
        os.system("python -m pip install --upgrade pip")
        os.system("python -m pip install -r requirements.txt")
        OpenSites()
        os.system("python RedTiger.py")

    elif sys.platform.startswith("linux"):
        os.system("clear")
        print("Installing the python modules required for the RedTiger Tool:\n")
        os.system("pip3 install --upgrade pip")
        os.system("pip3 install -r requirements.txt")
        OpenSites()
        os.system("python3 RedTiger.py")

except Exception as e:
    input(e)