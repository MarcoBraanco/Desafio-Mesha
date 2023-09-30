from selenium import webdriver
import os

class SeleniumActions:
    def startBrowser(self):
        currentPath = os.getcwd()
        self.driver = webdriver.Chrome(executable_path="")
        self.driver.get("https://www.google.com/")
        print("TESTE")

    

teste = SeleniumActions()
teste.startBrowser()