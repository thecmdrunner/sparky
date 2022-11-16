# 🤖 Sparky | PROJECT STATUS: EXPERIMENTAL

## Documentation pending!

Sparky is an Open source Voice Assistant, alternatives to Google Assistant and Alexa (oh Siri too btw).

Planning to have integration with Home Assistant which allows the operation of many already existing smart home devices.

## How to use

1. Install system dependencies

### Windows:
- Python 3.10 or newer

### MacOS:

### Linux:
- Python 3.10 or newer (most Linux distros come with python preinstalled)
- Library for `espeak`: `libespeak-dev` or `libespeak-ng-dev` or `libespeak1` or `libespeak-ng1`?
    - [Ubuntu](https://packages.ubuntu.com/search?suite=default&section=all&arch=any&keywords=libespeak&searchon=names): `sudo apt install libespeak-ng-dev`
    - [Fedora](https://packages.fedoraproject.org/search?query=espeak): `sudo dnf install espeak-ng`
    - Arch: `sudo pacman -S espeak-ng`

### FreeBSD:

### On a Virtual Machine
To use sparky on a Virtual machine, you can use [Scream](https://github.com/duncanthrax/scream) to passthrough your mic via a virtual sound card.

## How to run?

```bash
# Install python modules
pip3 install -r requirements.txt

# Run sparky
python3 sparky.py
```

## TODO:
- Documentation, Roadmap
- Rewrite without legacy stuff
- Build and package via:
    - Flatpak
    - Snap
    - AppImage?
- Implement gTTS alternatives like:
    - [Mycroft Mimic 3](https://youtu.be/egrMopDIvPE)
    - [Festival Speech](https://www.cstr.ed.ac.uk/projects/festival/) with [Festvox voices v2.4](http://festvox.org/packed/festival/2.4/) or [v2.1](http://festvox.org/packed/festival/2.1/)
    - Microsoft SAPI5?
- Option to switch between multiple TTS engines, like switch to Mycroft when offline, and gTTS for when internet is available.
