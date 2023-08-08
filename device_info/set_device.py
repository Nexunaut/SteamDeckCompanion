from StreamDeck.DeviceManager import DeviceManager

def SetBrightness(bLevel):
    streamdecks = DeviceManager().enumerate()
    print("Found {} Stream Deck(s).\n".format(len(streamdecks)))

    for index, deck in enumerate(streamdecks):
        # This example only works with devices that have screens.
        if not deck.is_visual():
            continue
        
        print(f"Opening {deck}")
        deck.open()
        print(f"Set Brightness to: {bLevel}")
        deck.set_brightness(bLevel)
        #deck.reset()
        deck.close()
    
#SetBrightness(5)
        
        
