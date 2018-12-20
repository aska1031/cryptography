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
        message = b"Hello World"
        msg_len = len(message)
        print("message is")
        print(message)
        print("---------------------------------------------------------")
        print("---------------------------------------------------------")
        _pub_len = self._backend._lib.OQS_SIG_qTESLA_I_length_public_key
        _pri_len = self._backend._lib.OQS_SIG_qTESLA_I_length_secret_key
        _sig_len = self._backend._lib.OQS_SIG_qTESLA_I_length_signature
        pub_key = self._backend._ffi.new("unsigned char []", _pub_len)
        pri_key = self._backend._ffi.new("unsigned char []", _pri_len)
        sig = self._backend._ffi.new("unsigned char []", _sig_len)
        sig_len = self._backend._ffi.new("size_t *", _sig_len)
        self._backend._lib.OQS_SIG_qTESLA_I_keypair(pub_key, pri_key)
        pub_text = self._backend._ffi.buffer(pub_key, _pub_len)[:]
        pri_text = self._backend._ffi.buffer(pri_key, _pri_len)[:]
        print("Public key is")
        print(pub_text)
        print("---------------------------------------------------------")
        print("---------------------------------------------------------")
        print("Private key is")
        print(pri_text)
        print("---------------------------------------------------------")
        print("---------------------------------------------------------")

        self.sign(sig,
                  sig_len,
                  message,
                  msg_len,
                  pri_key)

        verified_message = b"Hello World"
        verified_msg_len = len(verified_message)
        verified_result = self.verify(verified_message,
                                      verified_msg_len,
                                      sig,
                                      sig_len[0],
                                      pub_key)
        print("sig len is {}".format(sig_len[0]))
        if verified_result is 0:
            print("Valid message")
        else:
            print("Invalid message")

    def sign(self, signature, signature_len, message, message_len, private_key):
        self._backend._lib.OQS_SIG_qTESLA_I_sign(signature,
                                                 signature_len,
                                                 message,
                                                 message_len,
                                                 private_key)
        sig_text = self._backend._ffi.buffer(signature)[:signature_len[0]]
        print("Signature is")
        print(sig_text)

    def verify(self, message, message_len, signature, signature_len, public_key):
        return self._backend._lib.OQS_SIG_qTESLA_I_verify(message,
                                                          message_len,
                                                          signature,
                                                          signature_len,
                                                          public_key)
