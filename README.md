##### Mode d'emploi du simulateur d'anesthésie locorégionale 
###### Echoguidage

#Configuration


- Branchez la carte ARDUINO et la caméra sur des ports USB de l'ordinateur

- Vérifiez sur quel port USB se trouve la carte ARDUINO

Sous windows, vous trouverez le numéro du port en allant dans Gestionnaire des peripheriques > Port COM 

Sous linux, le numéro du port COM est donné par la commande "dmesg -s 1024".

- Entrez ce numéro dans le fichier main.py, ligne 25, dans la variable n_port_COM.


'''python
global n_port_COM
n_port_COM = 5
'''



#Lancement du simulateur


- Lancez l'application IDLE.exe dans le dossier WinPython
- Ouvrez le fichier main.py à partir de cette application
- Executez ce fichier en appuyant sur F5 
- Sur l'Interface Homme Machine qui apparait, choisissez parmis un des scénario proposés (dans cette version, seul le nerf femoral est disponible)
- Cliquez sur "Charger le scénario" puis sur "Lancer la simulation"

(une erreur de compatibilité avec la carte Arduino peut survenir de temps en temps, ré-executez le fichier main.py)




#Utilisation


- Placez la caméra sur son support en face du pain de gel de telle sorte à ce que la caméra se trouve dans le prolongement de la longueur du pain de gel

- L'accéléromètre de la sonde doit être orienté toujours face à la caméra

- L'aiguille doit se tenir au niveau des bouts de scotch rouge en haut et le capteur de distance doit toujours se situer du côté intérieur à l'angle que fait l'aiguille avec la surface sur pain de gel


