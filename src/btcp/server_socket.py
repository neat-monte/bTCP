from btcp.btcp_socket import BTCPSocket
from btcp.lossy_layer import LossyLayer
from btcp.constants import *
from btcp.enums import State, Flag, Key


class BTCPServerSocket(BTCPSocket):
    """ The bTCP server socket
    A server application makes use of the services provided by bTCP by calling accept, recv, and close
    """

    def __init__(self, window, timeout):
        super().__init__(window, timeout)
        self._lossy_layer = LossyLayer(self, SERVER_IP, SERVER_PORT, CLIENT_IP, CLIENT_PORT)


    def lossy_layer_input(self, segment, address):
        """ Called by the lossy layer from another thread whenever a segment arrives """
        if not self.buffer.full():
            self.buffer.put(segment, block=False)
    
    
    def accept(self):
        """ Wait for the client to initiate a three-way handshake """
        # Only non-connected server can accept a connection
        if self.state is not State.OPEN:
            return
        # Wait for connection attempt
        while self.state is State.OPEN:
            # Make a break and handle incoming segments
            self.handle_flow()
            # Block for receiving SYN request
            if Key.SYN in self.drop:
                message = self.drop.pop(Key.SYN)
                self.seq_nr = self.start_random_sequence()
                self.ack_nr = message['seq_nr'] + 1
                segment = self.pack_segment(flag=Flag.SYNACK)
                self._lossy_layer.send_segment(segment)
                print('Server sent SYNACK')
                # Move state to pending connection
                self.state = State.CONN_PEND
        # Wait for connection until the state changes
        while self.state is State.CONN_PEND:
            # Make a break and handle incoming segments
            self.handle_flow()
            # Block for receiving ACK
            if Key.CONN_ACK in self.drop:
                message = self.drop.pop(Key.CONN_ACK)
                self.state = State.CONN_EST
                print('Server established connection')


    def recv(self):
        """ Send any incoming data to the application layer """
        pass


    def send(self, segment):
        """ Send data originating from the application in a reliable way to the client """
        self._lossy_layer.send_segment(segment)


    def close(self):
        """ Clean up any state """
        self._lossy_layer.destroy()
