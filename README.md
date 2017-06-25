# Pyzapp

Schedule your WhatsApp messages via Python!


## Requirements:

+ Python 3.x
+ python-pip
+ virtualenv
+ selenium
+ Mozilla Firefox
+ atd (On most linux systems, this is installed by default)

## How to install:

#### Setting up Firefox

1. Install Mozilla Firefox, if you don't already have it.
2. Open up a terminal emulator and run `firefox -p`.
3. Click on **Create Profile** in the window that opens up.
4. Click on **Next**.
5. Type in "whatsapp" as the new profile name. (You are at liberty to use any name, but whatsapp is more apt)
6. Note down the path that is shown for the profile (you'll need it later!).
7. Click on **Finish**.
8. Then choose your newly created profile and click on **Start Firefox**.
9. Open up "<https://web.whatsapp.com>" and scan the QR code with your mobile after clicking on "WhatsApp Web".
10. Make sure the "Keep me signed in" checkbox is scheduled.

#### The script

1. Install Python3 if you haven't already installed it, and check if you have atd service enabled.
2. Install pip if it's not installed by default, and install virtualenv by running `pip install virtualenv` if it's not already installed.
2. Clone the contents of this repository onto your machine.
3. cd into the folder and run `virtualenv . --python=python3`.
4. Run `source bin/activate`.
5. Install selenium by running `pip install selenium`.
6. Download geckodriver, unzip it and place the 'geckodriver' file in the folder called geckodriver inside webdriver, which is inside a folder called selenium (You can keep it anywhere, but then you'll have to change the path in the code)
7. Open up "whatsapp.py" and change the path_to_profile variable with the path of profile you noted earlier, and check if the path_to_driver variable matches your path.
8. You are all set to rock!

## Usage:

Run the following command to schedule your whatsapp message

```bash
python pyzapp.py name_of_friend -m "Message" -t "HH:MM DD.MM.YYYY"
```

You can also run `python pyzapp.py --help` for more details

## Contact

For any error or suggestion, feel free to contact me on my mail at [friendyankan@gmail.com]().

## License

This content is licensed under MIT License. See the [license](https://raw.githubusercontent.com/ankan17/pyzapp/master/LICENSE).
