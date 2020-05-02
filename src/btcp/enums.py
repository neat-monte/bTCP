from enum import Enum, unique


@unique
class Flag(Enum):
    """ Different flags for bTCP header """
    NONE = 0
    ACK = 1
    SYN = 2
    SYNACK = 3
    FIN = 4
    FINACK = 5


@unique
class State(Enum):
    """ Different states for a bTCP socket """
    OPEN = 0
    CONN_PEND = 1
    CONN_EST = 2
    DISC_PEND = 3
    RECV = 4
    TRANS = 5


@unique
class Key(Enum):
    """ Different keys to access drop dictionary for specific messages """
    SYN = 0
    SYNACK = 1
    CONN_ACK = 2
    FIN = 3
    FINACK = 4
    DISC_ACK = 5
    RECV_ACK = 6
    DATA = 7
