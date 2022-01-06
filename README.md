# homeassistant
Home Assistant

Velkommen til min Home Assistant side! Her legger jeg ut noe av det jeg har slik at andre kan bruke det.

Du kan se eksempler av pakker i Images folderet.

Du kan se eksempler av flows i Images folderet i node-red. 

# FOR PAKKER TRENGER DU NOE SPESIELT (PACKAGES):

Du kan lese mer her:
https://ha-norge.no/Packages

Eller rett fra kilden her:
https://www.home-assistant.io/docs/configuration/packages/

# MINE NODE-RED flows:

Informasjon ligger inne i node_red mappen...

# MINE PAKKER:

packages/alarmer.yaml - Her er forskjellige alarmer, blant annet vekking, buss og på tide å legge seg alarm

packages/posten.yaml - Lager en sensor som forteller deg de neste leveringsdatoene for Posten og en binær sensor som forteller om posten blir levert i dag

packages/termostater.yaml - Termostatkontroll med dag / natt spar og mye automasjoner

packages/drivstoff.yaml - Henter priser 95 og diesel fra YX og Driv

packages/ladestasjoner.yaml - Tidsstyring på ladestasjoner med to av/på tidspunkt og ukedagoversikt

packages/renovasjon.yaml - Lager 5 sensorer som forteller deg når neste hentedag for renovasjon er

packages/vacation.yaml - Lager input booleans som heter vacation og home som kan brukes i automasjoner

packages/vaskemaskin.yaml - Creates a sensor that tells you what state the Washing Machine is in, a binary sensor that changes label according to stages and when the machine is sone, you get a message!

packages/oppvaskmaskin.yaml - Creates a sensor that tells you what state the Dishwacher is in, a binary sensor that changes label according to stages and when the machine is sone, you get a message!
