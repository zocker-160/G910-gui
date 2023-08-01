import uinput
from devices import allkeys as key
from dataclasses import dataclass, field


@dataclass(frozen=True)
class KeyboardInterface:

    devicename: str

    usbVendor: int
    usbProduct: int
    usbConfiguration: int
    usbInterface: tuple # tuple[int, int] | (index of interface, index of alternate setting)
    usbEndpoint: int

    numMacroKeys: int
    numMemoryKeys: int # number of memory / profile keys

    macroKeys: dict # dict[bytes, str]
    memoryKeys: dict # dict[bytes, str]
    mediaKeys: dict # dict[bytes, str] | only in use when in libUSB mode (kernel driver unloaded)
    releaseEvents: str # str[bytes]

    # Following is sent to disable the default G keys mapping
    disableGKeysInterface: int
    disableGKeys = list() # list[bytes]
    disableGKeysUseWrite: bool = field(default=True)

    ## optional
    memoryKeysLEDs = dict() # dict[str, bytes]

@dataclass(frozen=True)
class Logitech_G910_OrionSpectrum(KeyboardInterface):

    devicename = "Logitech G910 Orion Spectrum"

    usbVendor = 0x046d
    usbProduct = 0xc335
    usbConfiguration = 0
    usbInterface = (1, 0)
    usbEndpoint = 0

    numMacroKeys = 9
    numMemoryKeys = 3

    macroKeys = {
        b'\x11\xff\x08\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00': key.MACRO_1,
        b'\x11\xff\x08\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00': key.MACRO_2,
        b'\x11\xff\x08\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00': key.MACRO_3,
        b'\x11\xff\x08\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00': key.MACRO_4,
        b'\x11\xff\x08\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00': key.MACRO_5,
        b'\x11\xff\x08\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00': key.MACRO_6,
        b'\x11\xff\x08\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00': key.MACRO_7,
        b'\x11\xff\x08\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00': key.MACRO_8,
        b'\x11\xff\x08\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00': key.MACRO_9,
        b'\x11\xff\n\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00': key.MEMORY_RECORD,
    }

    memoryKeys = {
        b'\x11\xff\t\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00': key.MEMORY_1,
        b'\x11\xff\t\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00': key.MEMORY_2,
        b'\x11\xff\t\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00': key.MEMORY_3,
    }

    memoryKeysLEDs = {
        key.MEMORY_1: b'\x11\xff\x09\x1b\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
        key.MEMORY_2: b'\x11\xff\x09\x1b\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
        key.MEMORY_3: b'\x11\xff\x09\x1b\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    }

    mediaKeys = {
        b'\x02\x08': uinput.KEY_PLAYPAUSE,
        b'\x02\x04': uinput.KEY_STOP,
        b'\x02\x02': uinput.KEY_PREVIOUS,
        b'\x02\x01': uinput.KEY_NEXT,
        b'\x02@': uinput.KEY_MUTE,
        b'\x02\x10': uinput.KEY_VOLUMEUP,
        b'\x02 ': uinput.KEY_VOLUMEDOWN,
    }

    releaseEvents = {
        b'\x11\xff\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', # G release
        b'\x02\x00', # media key release
        b'\x11\xff\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', # M release
        b'\x11\xff\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', # MR release
    }

    disableGKeys = [
        b'\x11\xff\x10>\x00\x04\x00\x00\x00\x00\x00\x00\xd0\x01d\x07\x00\x00\x00\x00', # keyboard reset
        b'\x11\xff\x08.\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', # disable GMapping
        #b'\x11\xff\x08\x2e\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' # old mapping reset
    ]
    disableGKeysInterface = 1

@dataclass(frozen=True)
class Logitech_G910_OrionSpark(Logitech_G910_OrionSpectrum):
    devicename = "Logitech G910 Orion Spark"
    usbProduct = 0xc32b
    disableGKeysInterface = 0

@dataclass(frozen=True)
class Logitech_G710p(KeyboardInterface):

    devicename = "Logitech G710+"

    usbVendor = 0x046d
    usbProduct = 0xc24d
    usbConfiguration = 0
    usbInterface = (1, 0)
    usbEndpoint = 0

    numMacroKeys = 6
    numMemoryKeys = 3

    macroKeys = {
        b'\x03\x01\x00\x00': key.MACRO_1,
        b'\x03\x02\x00\x00': key.MACRO_2,
        b'\x03\x04\x00\x00': key.MACRO_3,
        b'\x03\x08\x00\x00': key.MACRO_4,
        b'\x03\x10\x00\x00': key.MACRO_5,
        b'\x03\x20\x00\x00': key.MACRO_6,
        b'\x03\x00\x80\x00': key.MEMORY_RECORD,
    }

    memoryKeys = {
        b'\x03\x00\x10\x00': key.MEMORY_1,
        b'\x03\x00\x20\x00': key.MEMORY_2,
        b'\x03\x00\x40\x00': key.MEMORY_3,
    }

    memoryKeysLEDs = {
        key.MEMORY_1: b'\x06\x10', # M1 LED
        key.MEMORY_2: b'\x06\x20', # M2 LED
        key.MEMORY_3: b'\x06\x40', # M3 LED
    }

    mediaKeys = {
        b'\x02\x08': uinput.KEY_PLAYPAUSE,
        b'\x02\x04': uinput.KEY_STOP,
        b'\x02\x02': uinput.KEY_PREVIOUS,
        b'\x02\x01': uinput.KEY_NEXT,
        b'\x02\x40': uinput.KEY_MUTE,
        b'\x02\x10': uinput.KEY_VOLUMEUP,
        b'\x02\x20': uinput.KEY_VOLUMEDOWN,
    }

    releaseEvents = {
        b'\x03\x00\x00\x00', # G release
        b'\x02\x00', # media key release
        b'\x03\x00\x00\x00', # M release
        b'\x03\x00\x00\x00', # MR release
    }

    disableGKeys = [b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00']
    disableGKeysInterface = 1
    disableGKeysUseWrite = False

@dataclass(frozen=True)
class Logitech_G510(KeyboardInterface):
    
    devicename = "Logitech G510"

    usbVendor = 0x046d
    usbProduct = 0xc22d
    usbConfiguration = 0
    usbInterface = (1, 0)
    usbEndpoint = 0

    numMacroKeys = 18
    numMemoryKeys = 3

    macroKeys = {
        b'\x03\x01\x00\x00\x00': key.MACRO_1,
        b'\x03\x02\x00\x00\x00': key.MACRO_2,
        b'\x03\x04\x00\x00\x00': key.MACRO_3,
        b'\x03\x08\x00\x00\x00': key.MACRO_4,
        b'\x03\x10\x00\x00\x00': key.MACRO_5,
        b'\x03\x20\x00\x00\x00': key.MACRO_6,
        b'\x03\x40\x00\x00\x00': key.MACRO_7,
        b'\x03\x80\x00\x00\x00': key.MACRO_8,
        b'\x03\x00\x01\x00\x00': key.MACRO_9,
        b'\x03\x00\x02\x00\x00': key.MACRO_10,
        b'\x03\x00\x04\x00\x00': key.MACRO_11,
        b'\x03\x00\x08\x00\x00': key.MACRO_12,
        b'\x03\x00\x10\x00\x00': key.MACRO_13,
        b'\x03\x00\x20\x00\x00': key.MACRO_14,
        b'\x03\x00\x40\x00\x00': key.MACRO_15,
        b'\x03\x00\x80\x00\x00': key.MACRO_16,
        b'\x03\x00\x00\x01\x00': key.MACRO_17,
        b'\x03\x00\x00\x02\x00': key.MACRO_18,
        b'\x03\x00\x00\x80\x00': key.MEMORY_RECORD
    }

    memoryKeys = {
        b'\x03\x00\x00\x10\x00': key.MEMORY_1,
        b'\x03\x00\x00\x20\x00': key.MEMORY_2,
        b'\x03\x00\x00\x40\x00': key.MEMORY_3,
    }

    mediaKeys = {
        b'\x02\x08': uinput.KEY_PLAYPAUSE,
        b'\x02\x04': uinput.KEY_STOP,
        b'\x02\x02': uinput.KEY_PREVIOUS,
        b'\x02\x01': uinput.KEY_NEXT,
        b'\x02\x10': uinput.KEY_MUTE, # not 100% sure about those last 3
        b'\x02\x20': uinput.KEY_VOLUMEDOWN,
        b'\x02\x40': uinput.KEY_VOLUMEUP
    }

    releaseEvents = [
        b'\x03\x00\x00\x00\x00', # M and G release
        b'\x02\x00' # media key release
    ]

    disableGKeys = [
        bytes([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]),
        bytes([7, 3, 0]),
        bytes([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]),
    ]

    disableGKeysInterface = 1
    disableGKeysUseWrite = False

@dataclass(frozen=True)
class Logitech_G815(KeyboardInterface):

    devicename = "Logitech G815"

    usbVendor = 0x046d
    usbProduct = 0xc33f
    usbConfiguration = 0
    usbInterface = (1, 0)
    usbEndpoint = 0

    numMacroKeys = 5
    numMemoryKeys = 3

    macroKeys = {
        b'\x11\xff\n\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00': key.MACRO_1,
        b'\x11\xff\n\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00': key.MACRO_2,
        b'\x11\xff\n\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00': key.MACRO_3,
        b'\x11\xff\n\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00': key.MACRO_4,
        b'\x11\xff\n\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00': key.MACRO_5,
        b'\x11\xff\x0c\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00': key.MEMORY_RECORD,
    }

    memoryKeys = {
        b'\x11\xff\x0b\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00': key.MEMORY_1,
        b'\x11\xff\x0b\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00': key.MEMORY_2,
        b'\x11\xff\x0b\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00': key.MEMORY_3,
    }

    memoryKeysLEDs = {
        key.MEMORY_1: b'\x11\xff\x0b\x1a\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', # M1 LED
        key.MEMORY_2: b'\x11\xff\x0b\x1a\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', # M2 LED
        key.MEMORY_3: b'\x11\xff\x0b\x1a\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', # M3 LED
    }

    mediaKeys = {
        b'\x03\x08': uinput.KEY_PLAYPAUSE,
        b'\x03\x04': uinput.KEY_STOP,
        b'\x03\x02': uinput.KEY_PREVIOUS,
        b'\x03\x01': uinput.KEY_NEXT,
        b'\x03\x10': uinput.KEY_VOLUMEUP,
        b'\x03\x20': uinput.KEY_VOLUMEDOWN,
        b'\x03\x40': uinput.KEY_MUTE,
    }

    releaseEvents = {
        b'\x11\xff\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', # G release
        b'\x03\x00', # media key release
        b'\x11\xff\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', # M release
        b'\x11\xff\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', # MR release
    }

    disableGKeys = [
        # switch from keyboard memory mode to client mode - disables everything but the "normal" keys
        # so we need to enable it again
        b'\x11\xff\x11\x1a\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', 
        # enable Gkeys
        b'\x11\xff\n*\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
        # enable LED manual control (not 100% sure but without this package the following
        # two packages will not do anything)
        b'\x11\xff\x0fZ\x01\x03\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
        # enable GLogo light
        b'\x11\xff\x0f\x1a\x00\x02\x00\x00\x00\x00\x00\x084d\x00\x00\x01\x00\x00\x00',
        # enable default background light
        b'\x11\xff\x0f\x1a\x01\x04\x00\x00\x00\x00\x00\x004\x01d\x08\x01\x00\x00\x00',
    ]

    disableGKeysInterface = 1

@dataclass(frozen=True)
class Logitech_G915(Logitech_G815):
    devicename = "Logitech G915 (wired)"
    usbProduct = 0xc33e

    macroKeys = {
        b'\x02\x01\x00\x00\x00\x00\x00\x00\x00': key.MACRO_1,
        b'\x02\x02\x00\x00\x00\x00\x00\x00\x00': key.MACRO_2,
        b'\x02\x04\x00\x00\x00\x00\x00\x00\x00': key.MACRO_3,
        b'\x02\x08\x00\x00\x00\x00\x00\x00\x00': key.MACRO_4,
        b'\x02\x10\x00\x00\x00\x00\x00\x00\x00': key.MACRO_5,
        b'\x11\x01\x0c\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00': key.MEMORY_RECORD,
    }

    memoryKeys = {
        b'\x11\x01\x0b\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00': key.MEMORY_1,
        b'\x11\x01\x0b\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00': key.MEMORY_2,
        b'\x11\x01\x0b\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00': key.MEMORY_3,
    }

    memoryKeysLEDs = {
        key.MEMORY_1: b'\x11\x01\x0b\x1a\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', # M1 LED
        key.MEMORY_2: b'\x11\x01\x0b\x1a\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', # M2 LED
        key.MEMORY_3: b'\x11\x01\x0b\x1a\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', # M3 LED
    }

    releaseEvents = {
        b'\x02\x00\x00\x00\x00\x00\x00\x00\x00', # G release
    }

    disableGKeys = [
        b'\x11\x01\x11\x1a\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', 
        b'\x11\x01\n*\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
        b'\x11\x01\x0fZ\x01\x03\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
        b'\x11\x01\x0f\x1a\x00\x02\x00\x00\x00\x00\x00\x084d\x00\x00\x01\x00\x00\x00',
        b'\x11\x01\x0f\x1a\x01\x04\x00\x00\x00\x00\x00\x004\x01d\x08\x01\x00\x00\x00',
    ]

@dataclass(frozen=True)
class Logitech_G935(KeyboardInterface):
    devicename = "Logitech G935"

    usbVendor = 0x046d
    usbProduct = 0x0a87

    usbConfiguration = 0
    usbInterface = (3, 0)
    usbEndpoint = 0

    disableGKeysInterface = 3
    usbUseWrite = True

    numMacroKeys = 3
    numMemoryKeys = 1 # does not have any, so we set it to 1, because we need at least 1 button in the UI

    macroKeys = {
        b'\x11\xff\x05\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00': key.MACRO_1,
        b'\x11\xff\x05\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00': key.MACRO_2,
        b'\x11\xff\x05\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00': key.MACRO_3,
        b'\x08\x01': key.MACRO_4, # kernel driver does not handle mute button, so we make it remappable by setting it as "G4"
        # TODO: this button does not have a release event, so it would be "stuck" all the time ._.
    }

    memoryKeys = {} # headset has no memory keys
    memoryKeysLEDs = {} # headset has no memory keys, so it also does not have any LED

    mediaKeys = {
        # b'\x08\x01': uinput.KEY_MUTE, # moved this to "macroKeys" to make that button remappable
        b'\x08\x10': uinput.KEY_MICMUTE,
        b'\x08 ': uinput.KEY_MICMUTE, # is actually "unmute", so could cause issues later
    }

    releaseEvents = {
        b'\x11\xff\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', # G release
    }

    disableGKeys = [
        b'\x11\xff\x05\x2a\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ]

    #flick up microphone (mute)
    #got data from keyboard: b'\x08\x10'
    
    #flick down microphone (unmute)
    #got data from keyboard: b'\x08 '

    ## other data unused for now:

    # headset connected
    # b'\x11\xff\x08\x00\x0ec\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    # b'\x01\x00\x00\x00\x00'
    # b'\x01\x00\x00\x00\x00'

    # lost connection to headset (turned off)
    # b'\x11\xff\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'




SUPPORTED_DEVICES = [
    Logitech_G910_OrionSpectrum,
    Logitech_G710p,
    Logitech_G910_OrionSpark,
    Logitech_G815,
    Logitech_G915,
    Logitech_G510,

    Logitech_G935
]
