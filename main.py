from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from random import randint


import time

class Whatsappbot:
    def __init__(self):
        self.mensagem = "Teste"
        self.grupos = ["Teste"]
        #options = webdriver.Edge
        #options.add_argument('lang=pt-br')
        self.driver = webdriver.Edge(EdgeChromiumDriverManager().install())

    def enviarMensagem(self):
        self.driver.get('https://web.whatsapp.com/')
        
        order=input(">")
        if(order!="start"):
            print("Program stopped")
            exit(0)

        print("Lauching in 5s")
        time.sleep(5)
        #Clicar no grupo
        grupo = self.driver.find_element_by_xpath("//span[@title='Teste']")
        grupo.click()
        time.sleep(1)

        #Clicar na caixa de texto
        cxtxt = self.driver.find_element_by_class_name('_3uMse')
        cxtxt.click()
        time.sleep(1)

        #Digitar mensagem
        cxtxt.send_keys("Pedro's bot launched. Now listening...")
        btn = self.driver.find_element_by_xpath("//span[@data-icon='send']")
        time.sleep(1)
        btn.click()

        while(1):
            exp = self.driver.find_element_by_xpath("(//span[@class='_3Whw5 selectable-text invisible-space copyable-text']//span)[last()]")
            time.sleep(1)
            cxtxt.click()
            command = exp.text
            if("/d" in command):
                command = command.replace("/d ","")

                if(command=="stop"):
                    cxtxt.send_keys("Bot: Goodbye, sir.")
                    print("STOPPED BY USER")
                    btn = self.driver.find_element_by_xpath("//span[@data-icon='send']")
                    time.sleep(1)
                    btn.click()
                    exit(0)

                #cxtxt.send_keys(exp.text)
                print(command)

                entrada = command
                mod=0
                posD=entrada.find('d')
                #print(posD)
                q=int(entrada[0:posD])
                t=entrada[posD+1:(len(entrada))]
                if("+" in t):
                    posSinal=t.find("+")
                    mod=int(t[posSinal+1:len(t)])
                    print(mod)
                    t=int(t[0:posSinal])
                elif ("-" in t):
                    posSinal=t.find("-")
                    mod=int(t[posSinal+1:len(t)])*(-1)
                    print(mod)
                    t=int(t[0:posSinal])
                print(q)
                t=int(t)
                print(t)

                mensagem = "Resultado: ("
                res=0
                for i in range(q):
                    roll=randint(1,t)
                    mensagem+=str(roll) + " "
                    res+=roll
                mensagem+=")"
                mensagem=mensagem.replace(" )",")")
                if(mod!=0):
                    if(mod>0):
                        mensagem+=" + " + str(mod)
                    else:
                        mensagem+=" - " + str(abs(mod))
                    
                    res+=mod

                mensagem+=" = *" + str(res)+"*"

                cxtxt.send_keys(mensagem)
                btn = self.driver.find_element_by_xpath("//span[@data-icon='send']")
                time.sleep(1)
                btn.click()

            time.sleep(1)
    
    
            




bot = Whatsappbot()
bot.enviarMensagem()