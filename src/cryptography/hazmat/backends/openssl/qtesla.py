from __future__ import absolute_import, division, print_function
from cryptography import utils
from cryptography.hazmat.primitives.asymmetric.qtesla import (
    QTESLA
)


@utils.register_interface(QTESLA)
class _QTESLA(object):
    def __init__(self, backend):
        self._backend = backend

    def keypair(self):
        _pub_len = self._backend._lib.OQS_SIG_qTESLA_I_length_public_key
        _pri_len = self._backend._lib.OQS_SIG_qTESLA_I_length_secret_key
        pub_key = self._backend._ffi.new("uint8_t []", _pub_len)
        pri_key = self._backend._ffi.new("uint8_t []", _pri_len)
        self._backend._lib.OQS_SIG_qTESLA_I_keypair(pub_key, pri_key)
        pub_text = self._backend._ffi.buffer(pub_key, _pub_len)[:]
        pri_text = self._backend._ffi.buffer(pri_key, _pri_len)[:]
        print("Public key is {}".format(pub_text))
        print("Private key is {}".format(pri_text))

    def sign(self, signature, signature_len, message, message_len, private_key):
        pass

    def verify(self, message, message_len, signature, signature_len, public_key):
        pass
