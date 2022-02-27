# Strato_Pi

Kasutage *Visual Studio Code*, see on Desktopil

Siia kausta lükkame koodi, backend, frontend ja riistvara

Templates kaustas html, muidu asi ei taha jooksma hakata

Proovige teha võimalikult funktsioonides koodi või klassidena,
siis kõigil kergem importida kui vaja

Kaamera jaoks cv2 ehk OpenCV on olemas

Veebi jaoks Flaski testitud

M6lemal kaunis kena dokumentatsioon olemas

## Kuidas scripte käima panna:
1. Avage terminal ````Ctrl + Alt + T````
2. ````pi@raspberrypi:~ $ cd /Strato_Pi```` 

````cd```` - Change Directory ````cd ..```` - tagasi eelmisesse kausta

````cd```` - tagasi home kausta

ning kaust kus Teie materjalid nt 
````
pi@raspberrypi:~ $ cd /Strato_Pi/Frontend
````
3. python skriptinimi.py n2iteks 
````
pi@raspberrypi:~/Strato_Pi $ python3 temps.py
````
Kui vaja kasutatada brauseris localhosti, ss saab ````127.0.0.1:5000````
või ````localhost:5000````

## How to use github:
ehk kuidas laadida yles ja/v6i alla oma senist romantikat

Desktopil on fail nimega ````manage_git.sh````

double-click ja Execute in terminal

***Github ei tunnista tyhjasid kaustasid!! Neid ei laeta yles!!***

>Selleks puhuks v6ib panna kausta tyhja faili v tekstidokumendi

## Modbus demo
Ma tegin lühikese demo mootori juhtimisest. Demos pöörleb mootor 3 sekundit päripäeva ning 3 sekundit vastupäeva. 

Demo käivitamiseks ava terminal, mine Backend kausta ning käivita Pythoni skript:

````
cd /Strato_Pi/Backend
python3 rtumaster_example.py
````

## Nginx server
Kus see asub:
````
cd /
````
Ehk tulemuseks on:
````
pi@raspberrypi:/ $
````
Mis on root kaust ning edasi:
````
cd /var/www/html/
````
Kui vaja muuta:
````
sudo code index.html
````
