from digitalio import DigitalInOut, Direction, Pull
import board
import storage
import usb_cdc


def main():
    firstRow = DigitalInOut(board.GP0)
    firstRow.direction = Direction.INPUT
    firstRow.pull = Pull.DOWN

    firstColumn = DigitalInOut(board.GP1)
    firstColumn.direction = Direction.OUTPUT
    firstColumn.value = True

    # disable mass storage and serial connection if first button is not pressed on boot
    if not firstRow.value:
        storage.disable_usb_drive()
        usb_cdc.disable()

    firstRow.deinit()
    firstColumn.deinit()


if __name__ == "__main__":
    main()