import math 

class projetil:
    histPos = [] #Historico de posições para plotagem e animação
    vInic = 0 #velocidade inicial
    ang = 0 #angulo de lançamento
    altInic = 0 #altura inicial
    gravAc = 0 #aceleração da gravidade

    ymax = 0
    xQued = 0 #alcançe horizontal
    tempVoo = 0 #tempo de voo

    def __init__(self, vel, angulo, alt, grav):
        self.histPos = [[0], [alt]]

        self.vInic = vel
        self.ang = angulo
        self.altInic = alt
        self.gravAc = grav
        
        #Calculo display de informações[
        self.ymax = self.vInic * math.sin(math.radians(self.ang)) #dividindo a conta em 2 para melhor legibilidade
        self.ymax = self.altInic + ((self.ymax * self.ymax)/(2 * self.gravAc))

        self.tempVoo = self.vInic * math.sin(math.radians(self.ang))#dividindo a conta para melhor legibilidade
        self.tempVoo = self.tempVoo * self.tempVoo
        self.tempVoo = self.tempVoo + (2 * self.gravAc * self.altInic)
        self.tempVoo = ((self.vInic * math.sin(math.radians(self.ang))) + math.sqrt(self.tempVoo))/self.gravAc

        self.xQued = 0 + (self.altInic * math.cos(math.radians(self.ang)) * self.tempVoo)
        #]


    def updControle(self, vel, angulo, alt, grav):
        self.histPos = [[0], [alt]]

        self.vInic = vel
        self.ang = angulo
        self.altInic = alt
        self.gravAc = grav
        
        #Calculo display de informações[
        self.ymax = self.vInic * math.sin(math.radians(self.ang)) #dividindo a conta em 2 para melhor legibilidade
        self.ymax = self.altInic + ((self.ymax * self.ymax)/(2 * self.gravAc))

        self.tempVoo = self.vInic * math.sin(math.radians(self.ang))#dividindo a conta para melhor legibilidade
        self.tempVoo = self.tempVoo * self.tempVoo
        self.tempVoo = self.tempVoo + (2 * self.gravAc * self.altInic)
        self.tempVoo = ((self.vInic * math.sin(math.radians(self.ang))) + math.sqrt(self.tempVoo))/self.gravAc

        self.xQued = 0 + (self.altInic * math.cos(math.radians(self.ang)) * self.tempVoo)
        #]


    def updTrag(self):
        #atualiza os pontos na tragetória para plotagem e animação
        pos = [0, self.altInic]
        self.histPos[0][0] = pos[0]
        self.histPos[1][0] = pos[1]
        #[lista de componentes x, lista de componentes y]
        
        t = 0
        maior = [0, 0] #valores maximos para eu ajustar o alcançe dos eixos

        while pos[1] >= 0:
            pos[0] = 0 + (self.vInic * math.cos(math.radians(self.ang)) * t)
            pos[1] = self.altInic + (self.vInic * math.sin(math.radians(self.ang)) * t) - (0.5 * self.gravAc * t * t)
           
            maior = [max(maior[0], pos[0]), max(maior[1], pos[1])]
            self.histPos[0].append(pos[0])
            self.histPos[1].append(pos[1])

            t += 0.05
        
        maior[0] = maior[0] + 15
        maior[1] = maior[1] + 15
        self.histPos.append(maior) #O maior esta no ultimo index



