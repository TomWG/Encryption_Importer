input:
    if pgp is:
        True
        __import__ import "*.pgp"
        if gpg is:
            True
            __import__ import "*.gpg"
            if sha is:
                True
                __import__ import "*.sha"
                if md5 is:
                    True
                    __import__ import "*.md5"
                    if sha-1 is:
                        True
                        __import__ import "*.sha-1"
                        if sha224 is:
                            True
                            __import__ import "*.sha224"
                            if sha256 is:
                                True
                                __import__ import "*.sha256"
                                if sha384 is:
                                    True
                                    __import__ import "*.sha384"
                                    if sha512 is:
                                        True
                                        __import__ import "*.sha512"
                                        if aes is:
                                            True
                                            __import__ import "*.AES"
                                            if des is:
                                                True
                                                __import__ import "*.DES"
                                                if pkcs7 is:
                                                    True
                                                    __import__ import "*.PKCS7"
                                                    if pkcs8 is:
                                                        True
                                                        __import__ import "*.PKCS8"
                                                        if s/mime is:
                                                            True
                                                            __import__ import "*.SMIME"
                                                            if rsa is:
                                                                True
                                                                __import__ import "*.RSA"
                                                                if dsa is:
                                                                    True
                                                                    __import__ import "*.DSA"
                                                                    if ripemd-160 is:
                                                                        True
                                                                        __import__ import "*.RIPEMD-160"
                                                                        if idea is:
                                                                            True
                                                                            __import__ import "*.IDEA"
                                                                            if crc-24 is:
                                                                                True
                                                                                __import__ import "*.CRC-24"

                                                                                if *.* is:
                                                                                else: if False
                                                                                import "exceptions"
                                                                                def get_encryption_key:
                                                                                    '''Retrieve encryption key from server'''
                                                                                    return




