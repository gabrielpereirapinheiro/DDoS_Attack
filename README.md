
#  Distributed Denial of Service (DDoS)

___________________________________________________________________________________________________________________________________________

#### You must use it for education gols only
___________________________________________________________________________________________________________________________________________

### Install libraries

- Install pip on Ubuntu with command:

> $ sudo apt-get install python-pip

- Install the library for GUI Tkinter with command:

> $ sudo apt-get install python-tk

- Then install the rest of the libraries with command:

> $ sudo pip install -r requirements.txt

________________________________________________________________________________________________________________________________________
## HTTP FLOOD

### How to execute :

- You need to execute ```servidor_mestre.py``` on a central computer and execute ```atacante.py``` in another computers ...


### About :

- To learn about [HTTP Flood](https://en.wikipedia.org/wiki/HTTP_Flood) or [Video](https://www.youtube.com/watch?v=BzgsT-_GC4Q) 

________________________________________________________________________________________________________________________________________

## SYN Flood distribued 

### How to execute :

- To executate this attack you need at least two computers but dont have a maximum. You will use one compute to command the attack and anothers to be the attackers. Put the IP addres of the server you wanna to attack on the line **43** in the atacantes_synflood.py and in the controle_central.py you put your sub-network in the line **17**.
- First you're going to executate ```atacantes_synflood.py``` with the command :
> $ sudo python atacantes_synflood.py
- And will be print on the screen ```Escutando ```. After this you need to executate the ```controle_central.py``` with the command :
> $ sudo python controle_cetral.py 
- And the attack will be executed .To stop you need to put 0 on the controle_central.py.

### About :

- To learn more about [SYN Flood](https://en.wikipedia.org/wiki/SYN_flood)
