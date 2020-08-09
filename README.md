# homeassistant
Home Assistant

Welcome to my Home Assistant page! Some of my content will be available here so others may use it.

Some integrations will be in norwegian as they are regional packages and not usually needed outside Norway or I just don't have time to translate.

You can see examples of packages in the Images folder and simple Lovelace codes for some in the Lovelace folder.

# WHAT YOU NEED TO MAKE IT WORK (PACKAGES):

You need to use the package feature in Home Assistant
https://www.home-assistant.io/docs/configuration/packages/

Add a folder in your config-folder named "packages"

Add following line in configuration.yaml:
packages: !include_dir_named packages

Next step is to store the package in the folder "packages"
When it is stored or changed, you need to then reboot HA

# MY CONTENT:

packages/alarmer.yaml - Her er forskjellige alarmer, blant annet vekking, buss og på tide å legge seg alarm

packages/posten.yaml - Lager en sensor som forteller deg de neste leveringsdatoene for Posten og en binær sensor som forteller om posten blir levert i dag

packages/termostater.yaml - Thermostat controll with day / night savings and a lot of automations

packages/drivstoff.yaml - Henter priser 95 og diesel fra YX og Driv

packages/ladestasjoner.yaml - Tidsstyring på ladestasjoner med to av/på tidspunkt og ukedagoversikt

packages/renovasjon.yaml - Lager 5 sensorer som forteller deg når neste hentedag for renovasjon er

packages/vacation.yaml - Creates input booleans called vacation and home to be used in automations

packages/vaskemaskin.yaml - Creates a sensor that tells you what state the Washing Machine is in, a binary sensor that changes label according to stages and when the machine is sone, you get a message!

packages/oppvaskmaskin.yaml - Creates a sensor that tells you what state the Dishwacher is in, a binary sensor that changes label according to stages and when the machine is sone, you get a message!
