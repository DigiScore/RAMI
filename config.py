# [HARDWARE]
xarm_connected = False
eda_live = True

# [PLAY PARAMS]
silence_listener = False
duration_of_piece = 2000000  # in sec
speed = 5  # dynamic tempo of the all processes: 1 = slow, 10 = fast
temperature = 0

# [XARM]
xarm1_port = '192.168.1.222'
xarm_x_extents = [-400, 400]  # cartesian coords in mm
xarm_y_extents = [-400, 400]
xarm_z_extents = [155, 1000]
# xarm_ballet_x_extents = [400, 400]
# xarm_ballet_y_extents = [-250, 250]
# xarm_ballet_z_extents = [150, 400]
xarm_irregular_shape_extents = 50
xarm_fenced = True

# [SOUND IN]
mic_sensitivity = 10000
mic_in_prediction = 0.36


# [BITALINO]
baudrate = 10
channels = [0]
mac_address = "98:D3:B1:FD:3D:1F"  # '/dev/cu.BITalino-3F-AE' (Linux)

# [STREAMING]
stream_list = ['rnd_poetry',
               'flow2core',
               'core2flow',
               'audio2core',
               'audio2flow',
               'flow2audio',
               'eda2flow']

# [DEBUG]
# debug = logging.INFO

# [DATAWRITER]
data_writer = False

"""
Notes:
To check available ports, run the following code:
    from serial.tools import list_ports

    available_ports = list_ports.comports()
    print(f'available ports: {[x.device for x in available_ports]}')

May need `sudo chmod 666 /dev/ttyACM0`
"""
