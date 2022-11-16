__author__ = 'Joshua Zosky'

if __name__ == "__main__":
    import __init__

import FaceReaderBindCPython as FaceReaderBinding

# Instantiate the controller with IP address(string) and Port number(integer)
# a = FaceReaderBinding.Controller('127.0.0.1', 9090)
a = FaceReaderBinding.Controller('192.168.1.1', 9090)

# Connect to FaceReader
a.connect()
a.start_recording()
# Turn on State Logging(This is a toggle, True = Turn it on, False = Turn it off)
a.state_logging(True)

# Check for state logging events periodically, you'll want this somewhere in a trial loop
while True:
    if a.state_log != "":
        print(a.state_log)
        break

# Disconnect from FaceReader
a.stop_recording()
a.disconnect()
print('done')
