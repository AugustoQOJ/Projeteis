import matplotlib
matplotlib.use('TkAgg')

import matplotlib.widgets as btns
import matplotlib.animation as anim
import matplotlib.pyplot as plt

import fisica as fis

#Inicialização de coisas importantes [
ani = None #para preservar apesar do coletor de lixo

objFis = fis.projetil(77.5, 44.5, 25.0, 9.8)
objFis.updTrag()

janela, eixDisp = plt.subplots()
plt.subplots_adjust(bottom=0.25, top=0.75)
trajetoria, = eixDisp.plot(objFis.histPos[0], objFis.histPos[1])
#]

#Caixas de texto[
xmaxEixo = plt.axes([0.15, (0.2+0.75), 0.5, 0.05])
ymaxEixo = plt.axes([0.15, (0.1+0.75), 0.5, 0.05])
tmaxEixo = plt.axes([0.15, (0.01+0.75), 0.5, 0.05])

xmaxTexto = btns.TextBox(xmaxEixo,'' ,initial=f"Alcançe máximo: {objFis.xQued:.2f}m", textalignment="center")
ymaxTexto = btns.TextBox(ymaxEixo,'' ,initial=f"Altura máxima: {objFis.ymax:.2f}m", textalignment="center")
tmaxTexto = btns.TextBox(tmaxEixo,'' ,initial=f"Tempo de voo: {objFis.tempVoo:.2f}s", textalignment="center")
#]

#Criação dos sliders[
velAxis = plt.axes([0.35, 0.15, 0.5, 0.03])
angAxis = plt.axes([0.35, 0.1, 0.5, 0.03])
altAxis = plt.axes([0.35, 0.05, 0.5, 0.03])
gravAxis = plt.axes([0.35, 0.01, 0.5, 0.03])

velSlide = btns.Slider(velAxis, "Velocidade inicial", 5.0, 150.0, 77.5)
angSlide = btns.Slider(angAxis, "Angulo de lançamento", 1.0, 89.0, 44.5)
altSlide = btns.Slider(altAxis, "Altura inicial", 0.0, 50., 25.0)
gravSlide = btns.Slider(gravAxis, "Aceleração gravitacional", 5.0, 24.8, 9.8)
#]

#Funções de atualização para cada slider, para atualização em tempo real[
def updTrajetoVel(v):
    objFis.updControle(v, objFis.ang, objFis.altInic, objFis.gravAc)
    objFis.updTrag()
    trajetoria.set_xdata(objFis.histPos[0])
    trajetoria.set_ydata(objFis.histPos[1])

    xmaxTexto.set_val(f"Alcançe máximo: {objFis.xQued:.2f}m")
    ymaxTexto.set_val(f"Altura máxima: {objFis.ymax:.2f}m")
    tmaxTexto.set_val(f"Tempo de voo: {objFis.tempVoo:.2f}s")

def updTrajetoAng(a):
    objFis.updControle(objFis.vInic, a, objFis.altInic, objFis.gravAc)
    objFis.updTrag()
    trajetoria.set_xdata(objFis.histPos[0])
    trajetoria.set_ydata(objFis.histPos[1])

    xmaxTexto.set_val(f"Alcançe máximo: {objFis.xQued:.2f}m")
    ymaxTexto.set_val(f"Altura máxima: {objFis.ymax:.2f}m")
    tmaxTexto.set_val(f"Tempo de voo: {objFis.tempVoo:.2f}s")


def updTrajetoAlt(l):
    objFis.updControle(objFis.vInic, objFis.ang, l, objFis.gravAc)
    objFis.updTrag()
    trajetoria.set_xdata(objFis.histPos[0])
    trajetoria.set_ydata(objFis.histPos[1])

    xmaxTexto.set_val(f"Alcançe máximo: {objFis.xQued:.2f}m")
    ymaxTexto.set_val(f"Altura máxima: {objFis.ymax:.2f}m")
    tmaxTexto.set_val(f"Tempo de voo: {objFis.tempVoo:.2f}s")


def updTrajetoGrav(g):
    objFis.updControle(objFis.vInic, objFis.ang, objFis.altInic, g)
    objFis.updTrag()
    trajetoria.set_xdata(objFis.histPos[0])
    trajetoria.set_ydata(objFis.histPos[1])

    xmaxTexto.set_val(f"Alcançe máximo: {objFis.xQued:.2f}m")
    ymaxTexto.set_val(f"Altura máxima: {objFis.ymax:.2f}m")
    tmaxTexto.set_val(f"Tempo de voo: {objFis.tempVoo:.2f}s")



velSlide.on_changed(updTrajetoVel)
angSlide.on_changed(updTrajetoAng)
altSlide.on_changed(updTrajetoAlt)
gravSlide.on_changed(updTrajetoGrav)
#]

#Criação do botão e da função de animação[
btnEixo = plt.axes([0.80, 0.905, 0.1, 0.05]) #eixo do botão
botao = btns.Button(btnEixo, 'Lançar', color='red', hovercolor='yellow')

def updAnim(i):
    trajetoria.set_data(objFis.histPos[0][0:(i-1)], objFis.histPos[1][0:(i-1)])
    return trajetoria,

def Animar(dump): #Desenha os dados de forma progressiva ao invés de imediatamente, animando o lançamento
    global ani

    if ani is not None:
        ani = None
   
    trajetoria.set_xdata(0)
    trajetoria.set_ydata(objFis.altInic)

    ani = anim.FuncAnimation(janela, updAnim, frames=(len(objFis.histPos[0])-1), blit=True, interval=5, repeat=False)
    janela.canvas.draw_idle()

botao.on_clicked(Animar)
#]


plt.show()
