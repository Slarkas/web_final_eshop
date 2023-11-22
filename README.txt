                                    Martynas Bendoraitis

                                    Projektas Web-E-Shop

Sis puslapis yra e-parduotuve, leidzianti sukurti pardavejo accounta , turinti admin funkcionaluma
prekiu kataloga ir paieska, leidzia uploadint paveiksliuka idedant produkta,
issiuncia email pardavejui ir pirkejui.

fake koretele naudot stripe: Mastercard: 5105 1051 0510 5100 | 02/24 | 123


######## PANAUDOTI pip install:
                                asgiref
                                certifi
                                chardet
                                Django
                                idna
                                Pillow
                                pytz
                                requests
                                sqlparse
                                stripe
                                urllib3

Web paleidimas per terminala - python manage.py runserver

## Ka galima siame puslapi:

### A. Adminas gali:
1. Valdyti kategorijas (Add, Update, Filter and Delete)
2. Valdyti visus produktus (Add, Update, Filter and Delete)
3. Valdyt userius (Update, Filter and Delete)
4. Valdyti uzsakymus (View and Process)

### B. Pardavejas(Vendor) gali:
1. Add Products
2. Update Profile
4. Gaut uzsakymus ir valdyt juos


### C. Vartotojas(no-login) gali:
1. Prideti i krepseli
2. Atsiskaityti banko kortele
3. Ivesti pristatymo adresa
4. Matyti visus produktus bei pardavejus
