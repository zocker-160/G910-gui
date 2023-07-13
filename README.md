# ![keyboard-center](images/g910-icon.png) Keyboard Center

[![DEB builder](https://github.com/zocker-160/keyboard-center/actions/workflows/debbuilder.yml/badge.svg)](https://github.com/zocker-160/keyboard-center/actions/workflows/debbuilder.yml)

Keyboard Center is an application attempting to create an easy way for users to map their macro keys of their >100$ keyboard to useful actions, because Logitech does not give a fuck.

**Unlike some other solutions, this application works alongside with RGB software like [OpenRGB](https://openrgb.org/)!**

![showcase](images/animation2.gif)

**NOTE:** This application is written for **Linux only**, on Windows use whatever bloatware the vendor wants you to use.

## Features

- [x] Mapping of keys, combos and macros
- [x] Ability to map commands to keys
- [x] Ablity to add delays to macros
- [x] libhidraw backend ~and libusb as backup if needed~ (libusb only < 0.2.0)
- [x] Support for switching LEDs of profile keys
- [x] Import and export of the configuration (added ability to open configuration folder instead)
- [x] openRGB integration - linking of macro profiles with openRGB profiles
- [ ] Application specific profiles *(on hold until there is a common way to do this on Wayland[^1])*

[^1]: For more information see [this](https://github.com/flatpak/xdg-desktop-portal/issues/304) and [this](https://unix.stackexchange.com/questions/399753/how-to-get-a-list-of-active-windows-when-using-wayland) and [this](https://askubuntu.com/questions/1414320/how-to-get-current-active-window-in-ubuntu-22-04)

## Supported Keyboards

- Logitech G910 Orion Spectrum (046d:c335)
- Logitech G910 Orion Spark (046d:c32b) (thanks to [@microdou](https://github.com/microdou))
- Logitech G710+ (046d:c24d) (big thanks to [@nirenjan](https://github.com/nirenjan))
- Logitech G815 (046d:c33f) (thanks to [@nickbuss](https://github.com/nickbuss))
- Logitech G510 (046d:c22d) (thanks to [@Flying--Dutchman](https://github.com/Flying--Dutchman) for the help)

## Install

### Arch / Manjaro

available in the AUR: [[AUR] keyboard-center](https://aur.archlinux.org/packages/keyboard-center/)

### Debian / Ubuntu

- Download `.deb` from [release page](https://github.com/zocker-160/keyboard-center/releases)
- Install using package manager of your choice or in terminal: `apt install ./<packagename>.deb`

## Setup OpenRGB Integration
### Step 1: Create Profile(s) in OpenRGB
![OpenRGBprofiles](images/OpenRGBprofiles.png)

### Step 2: Specify Profile in Keyboard Center

![OpenRGBkeyboardcenter](images/OpenRGBkeyboardc.png)

**note:** if you install OpenRGB after Keyboard Center, you will need to restart it.

## Manage Background Service

Keyboard Center places itself into the system tray (unless disabled see [CLI options](#cli-options)).

If you try to open a secondary instance, it ~will~ should reactivate the primary one if minimized or hidden.

## Settings

Settings are stored in a `settings.yml` file, which is located at
- `$XDG_CONFIG_HOME/keyboard-center` **or** if not defined
- `$HOME/.config/keyboard-center`

## CLI options

- `-v` `--version`: prints version (duh)
- `--background-mode`: hides tray icon
- `--dev`: meant for development purposes only

#### Current default settings
`settings: {usbTimeout: 1000, retryCount: 5}`

### Dependencies
#### Debian / Ubuntu
- python3 >= 3.9
- python3-pyqt5 >= 5.15
- python3-usb
- python3-uinput
- python3-ruamel.yaml
- libhidapi-hidraw0
- libnotify-bin

#### Arch / Manjaro
- python >= 3.9
- python-pyqt5 >= 5.15
- python-uinput >= 0.11.2
- python-ruamel-yaml >= 0.15
- python-pyusb >= 1.0.2
- hidapi >= 0.10
- libnotify >= 0.7.9

### Contribute New Keyboard

- make sure all required dependencies are installed + `git`
- `git clone https://github.com/zocker-160/keyboard-center`
- `cd keyboard-center`
- make sure that `usbVendor` and `usbProduct` in `src/newDeviceDebugger.py` is set properly\
(you can check with `lsusb`)
- **you might need to run the following commands with `sudo` if you get permission errors**
- `python3 src/newDeviceDebugger.py` and press all memory keys, macro keys and multimedia keys one after each other
- `python3 src/newDeviceDebugger.py --info`
- exit with `CTRL + C` (can take a second or two)
- open a new issue and provide output of the last two commands and the USB ID of your keyboard

**overall it should look something like this:**

![addKeyAnim](images/KeyboardCenter_add.gif)
