****************************
Mopidy-Ssd1306
****************************

Display state of mopidy playback using an SSD1306 compatible OLED screen

Features
========

- Bootsplash
- Show Wi-Fi and playback status
- Display currently playing song

Installation
============

Install by running::

    pip install Mopidy-Ssd1306

To access the OLED screen on the Raspberry Pi you have to run mopidy with sudo::

	sudo mopidy


Configuration
=============

Before starting Mopidy, you must add configuration for
Mopidy-Ssd1306 to your Mopidy configuration file::

    [ssd1306]
    enabled = true

Project resources
=================

- `Source code <https://github.com/hadess/mopidy-ssd1306>`_
- `Issue tracker <https://github.com/hadess/mopidy-ssd1306/issues>`_
- `Development branch tarball <https://github.com/hadess/mopidy-ssd1306/archive/master.tar.gz#egg=Mopidy-Ssd1306-dev>`_


Changelog
=========

v1.0.0
----------------------------------------

- First working version

