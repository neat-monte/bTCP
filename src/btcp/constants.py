# Connections
CLIENT_IP = 'localhost'
CLIENT_PORT = 20000
SERVER_IP = 'localhost'
SERVER_PORT = 30000

# Sizes
HEADER_SIZE = 10
PAYLOAD_SIZE = 1008
SEGMENT_SIZE = HEADER_SIZE + PAYLOAD_SIZE

# Communication
HEADER_FORMAT = '!HHbbHH'
DATA_FORMAT= '!s'
MAX_ATTEMPTS = 3
SEGMENT_KEYS = ['seq', 'ack', 'flag', 'win', 'dlen', 'cksum', 'data']
BUFFER_SIZE = 5