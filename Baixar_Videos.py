from pytube import YouTube
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import uic, QtWidgets
import os

def baixar_videos():
    def Caixa_de_mensagem():
        msg = QMessageBox()
        msg.setWindowTitle('DOWNLOAD')
        msg.setText('Download concluído')
        msg.setIcon(QMessageBox.Information)        
        msg.exec_()

    #COLANDO O LINK DO VÍDEO E DIRETORIO

    url = file.lineEdit.text()
    diretorio = file.lineEdit_2.text()
    tube = YouTube(url)
    
    botaoAudio = file.radioButton.isChecked()
    botaoVideo = file.radioButton_2.isChecked()
    
    if botaoVideo:
        video = tube.streams.get_highest_resolution()
        video.download(diretorio)
        Caixa_de_mensagem()
        
    elif botaoAudio:
        audio = tube.streams.filter(only_audio=True).first()
        RemoverFormatoMp4 = audio.download(output_path=diretorio)
        
        base = os.path.splitext(RemoverFormatoMp4)
        NovoFormatoDeArquivo = base + '.mp3'
        os.rename(RemoverFormatoMp4, NovoFormatoDeArquivo)
        
        Caixa_de_mensagem()
        
app = QtWidgets.QApplication([])
file = uic.loadUi('baixar.ui')    
file.pushButton.clicked.connect(baixar_videos)
file.show()
app.exec()
