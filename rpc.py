import SocketServer
import struct
import pickle


class RPCRequestHandler(SocketServer.BaseRequestHandler):
    """UDP RPC server handler"""
    def handle(self):
        data = self.request[0].strip()
        sock = self.request[1]

        sock.sendto(pickle.dumps(getattr(self, data, None)), self.client_address)