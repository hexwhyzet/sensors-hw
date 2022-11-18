import time

from pySerialTransfer import pySerialTransfer as txfer

if __name__ == '__main__':
    try:
        link = txfer.SerialTransfer('COM6')

        link.open()
        time.sleep(2)

        while True:
            while not link.available():
                if link.status < 0:
                    if link.status == txfer.CRC_ERROR:
                        print('ERROR: CRC_ERROR')
                    elif link.status == txfer.PAYLOAD_ERROR:
                        print('ERROR: PAYLOAD_ERROR')
                    elif link.status == txfer.STOP_BYTE_ERROR:
                        print('ERROR: STOP_BYTE_ERROR')
                    else:
                        print('ERROR: {}'.format(link.status))

            rec_float_ = link.rx_obj(obj_type=float,
                                     obj_byte_size=4)

            print(f'Illuminance: {rec_float_} lux')
            with open("res.txt", "a+") as res_file:
                print(rec_float_, file=res_file)

    except KeyboardInterrupt:
        try:
            link.close()
        except:
            pass

    except:
        import traceback

        traceback.print_exc()

        try:
            link.close()
        except:
            pass
