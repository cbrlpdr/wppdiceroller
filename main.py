from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from random import randint


import time

#Issue list:
# - Ao enviar uma mensagem imediatamente após o comando, o comando não é executado
# - Acrescentar o nome de quem fez a rolagem
# - Resolver o problema de múltiplas requisições


class WhatsDiceRoller:
    def __init__(self):

        self.groupname="Guilda dos CapaAnoes"
        #options = webdriver.Edge
        #options.add_argument('lang=pt-br')
        self.driver = webdriver.Edge(EdgeChromiumDriverManager().install())

    def run(self):
        self.driver.get('https://web.whatsapp.com/')
        groupname=self.groupname
        cmd=input(">")
        if(cmd!="start"):
            print("Program stopped")
            print("REASON: WRONG USER COMMAND")
            exit(0)
        elif cmd=="exit":
            print("Program stopped")
            print("REASON: STOPPED BY USER TERMINAL COMMAND")

        print("Lauching in 5s")
        time.sleep(5)
        #Clicar no grupo
        grupo = self.driver.find_element_by_xpath(f"//span[@title='{groupname}']")
        grupo.click()
        time.sleep(1)

        #Clicar na caixa de texto
        cxtxt = self.driver.find_element_by_class_name('_3uMse')
        cxtxt.click()
        time.sleep(0.5)

        #Digitar mensagem
        cxtxt.send_keys("Bot iniciado!")
        btn = self.driver.find_element_by_xpath("//span[@data-icon='send']")
        time.sleep(0.5)
        btn.click()

        while(1):
            tEspera=0.3 #tempo de espera para enviar a mensagem após digitá-la
            exp = self.driver.find_element_by_xpath("(//span[@class='_3Whw5 selectable-text invisible-space copyable-text']//span)[last()]")
            #sender = self.driver.find_element_by_xpath("(//div[@class='_274yw']//div[@class='copyable-text'])[last()]")
            
            time.sleep(1)
            cxtxt.click()
            command = exp.text
            if("/d " in command):
                command = command.replace("/d ","")

                if(command=="stop"):
                    cxtxt.send_keys("Bot: Falou mano, até mais")
                    

                    btn = self.driver.find_element_by_xpath("//span[@data-icon='send']")
                    time.sleep(tEspera)
                    btn.click()

                    print("Program stopped")
                    print("REASON: STOPPED BY USER CHAT COMMAND")
                    exit(0)
                elif("changeWait" in command):
                    command=command.replace("changeWait ","")
                    tEspera=int(command)
                    cxtxt.send_keys(f"Bot: Tempo de resposta modificado para *{tEspera}s*")
                    btn = self.driver.find_element_by_xpath("//span[@data-icon='send']")
                    time.sleep(tEspera)
                    btn.click()
                    continue

                #cxtxt.send_keys(exp.text)
                #print(command)

                entrada = command
                mod=0
                posD=entrada.find('d')
                #print(posD)
                q=int(entrada[0:posD])

                #TODO: tratamento de variáveis para evitar erros e adicionar novas operações
                t=entrada[posD+1:(len(entrada))]
                if("+" in t):
                    posSinal=t.find("+")
                    mod=int(t[posSinal+1:len(t)])
                    #print(mod)
                    t=int(t[0:posSinal])
                elif ("-" in t):
                    posSinal=t.find("-")
                    mod=int(t[posSinal+1:len(t)])*(-1)
                    #print(mod)
                    t=int(t[0:posSinal])
                #print(q)
                t=int(t)
                #print(t)

                #TODO: Name finder - Nota: está retornando apenas o nome do usuário-servidor, preciso dar um jeito de retornar o nome dos outros contatos
                #           Provavelmente preciso achar o nome da classe da mensagem do outro usuário em vez de usar o data pre plain text
                #nome=sender.get_attribute("data-pre-plain-text")
                #nome=nome.replace(nome[0:nome.find("]")+2],"")

                mensagem = f"Resultado: ("
                res=0
                for i in range(q):
                    roll=randint(1,t)

                    if(roll==20):
                        mensagem+=" *" + str(roll) + "!* "
                    else:
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
                time.sleep(tEspera)
                btn.click()

            time.sleep(tEspera)
    
    
#---------------------------------------------------
bot = WhatsDiceRoller()
bot.run()