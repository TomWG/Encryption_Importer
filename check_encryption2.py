input:
        if pgp is
                True
import "*.pgp"
        if gpg is:
                True
import "*.gpg"
         if sha is:
                True
import "*.sha"
         if md5 is:
                True
import "*.md5"
         if sha-1 is:
                True
import "*.sha-1"
         if sha224 is:
                True
import "*.sha224"
         if sha256 is:
                True
import "*.sha256"
         if sha384 is:
                True
import "*.sha384"
         if sha512 is:
                True
import "*.sha512"
         if aes is:
                True
import "*.AES"
         if des is:
                True
import "*.DES"
         if pkcs7 is:
                True
import "*.PKCS7"
         if pkcs8 is:
                True
import "*.PKCS8"
         if s/mime is:
                True
import "*.SMIME"
         if rsa is:
                True
import "*.RSA"
         if dsa is:
                True
import "*.DSA"
         if ripemd-160 is:
                True
import "*.RIPEMD-160"
         if idea is:
                True
import "*.IDEA"
         if crc-24 is:
                True
import "*.CRC-24"

if *.* is:
else: if False
import "exceptions"
def get_encryption_key:
                '''Retrieve encryption key from server'''
                return

