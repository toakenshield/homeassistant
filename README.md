# homeassistant
Home Assistant

Welcome to my Home Assistant page! Some of my content will be available here so others may use it.

Some integrations will be in norwegian as they are regional packages and not usually needed outside Norway.

You can see examples of packages in the folder Images.

# WHAT YOU NEED TO MAKE IT WORK (PACKAGES):

You need to use the package feature in Home Assistant
https://www.home-assistant.io/docs/configuration/packages/

Add a folder in your config-folder named "packages"

Add following line in configuration.yaml:
packages: !include_dir_named packages

Next step is to store the package in the folder "packages"
When it is stored or changed, you need to then reboot HA

# MY CONTENT:

packages/posten.yaml - Lager en sensor som forteller deg de neste leveringsdatoene for Posten og en binær sensor som forteller om posten blir levert i dag

packages/renovasjon.yaml - Lager 5 sensorer som forteller deg når neste hentedag for renovasjon er

packages/vaskemaskin.yaml - Creates a sensor that tells you what state the Washing Machine is in, a binary sensor that changes label according to stages and when the machine is sone, you get a message!

packages/oppvaskmaskin.yaml - Creates a sensor that tells you what state the Dishwacher is in, a binary sensor that changes label according to stages and when the machine is sone, you get a message!
