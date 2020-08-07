# homeassistant
Home Assistant

Welcome to my Home Assistant page! Some of my content will be available here so others may use it.

Some integrations will be in norwegian as they are regional packages and not usually needed outside Norway.

PACKAGES

I am using the packages feature in Home Assistant as I find it very usefull and tidy!
https://www.home-assistant.io/docs/configuration/packages/

So in my configuration.yaml I have the following line:
packages: !include_dir_named packages

The packages are saved in a folder named "packages" inside your config-folder. 

When you have made changes to a package or added a new package you need to restart HA to include the package.


MY CONTENT:

packages/posten.yaml - Lager en sensor som forteller deg de neste leveringsdatoene for Posten og en binær sensor som forteller om posten blir levert i dag
