import socket #modulo comunicazione di rete
import random #modulo per generare dati casuali

print("Inserisci i dati richiesti per avviare il programma")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #creo oggetto s ipv4 e protocollo UDP
dimensione_pacchetto = 1024
ip = input("Indirizzo IP: ")
porta = int(input("Porta: "))
numero_pacchetti = int(input("Pacchetti da inviare: "))
inviati = 0 #variabile che serve a tracciare il numero dei pacchetti inviati

for i in range(numero_pacchetti): #ciclo for che dura quanto il numero dei pacchetti
	bytes = random._urandom(dimensione_pacchetto)
	s.sendto(bytes,(ip,porta)) #invia il pacchetto all'ip e la porta indicate
	print("Invia pacchetto %s a %s sulla porta %s." % (i+1,ip,porta))
	inviati += 1

s.close()

