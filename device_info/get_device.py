from StreamDeck.DeviceManager import DeviceManager

def FindDevice():
    
    deck_info = []
    streamdecks = DeviceManager()
    devices = streamdecks.enumerate()
    
    for device in devices:
    # Get and print the type of the device
        device.open()
        info  = (device.deck_type(), device.id(), device.get_serial_number(), device.key_layout())
        device.close()
        print(info)
        deck_info.append(info)
        
    return deck_info
