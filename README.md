# 🤖 Sparky | PROJECT STATUS: EXPERIMENTAL

## Documentation pending!

Sparky is an Open source Voice Assistant, alternatives to Google Assistant and Alexa (oh Siri too btw).

Planning to have integration with Home Assistant which allows the operation of many already existing smart home devices.

## TODO
- Documentation
- Rewrite without legacy stuff
- Build and package via:
    - Flatpak
    - Snap
    - AppImage?
- Implement [gTTS alternatives](https://www.youtube.com/watch?v=Ju_X11JyRSE)?

## How to use

### Install dependencies

```bash
pip3 install -r requirements.txt
```

### Run `sparky.py`

```bash
python3 sparky.py
```

### On Linux:

Install `espeak`


#### Enter variables for personalization (Optional)

```python
yourName = '' # enter your name 
yourMail = '' # enter your email address
```

### Sending Email 

Email is currently setup for GMAIL.

You need to enter credentials if you want to be able to send emails.

```python
botMail = '' # Put your burner email address here, and turn on external access. 

botMailPassword = '' # create a secure password
```

Enter names and email addresses as you wish.

```python
elif recipientName == "PERSON 1":
    to = "THEIR EMAIL"

elif recipientName == "PERSON 2":
    to = "THEIR EMAIL"

elif recipientName == "PERSON 3":
    to = "THEIR EMAIL"     
```




