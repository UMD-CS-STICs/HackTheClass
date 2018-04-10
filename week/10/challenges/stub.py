# do `curl http://starship.python.net/~gherman/programs/md5py/md5py.py > md5.py`
# if you do not have it from the git repo
import md5py

#####################################
### STEP 1: Calculate forged hash ###
#####################################

message = ''    # original message here
legit = ''      # a legit hash of secret + message goes here, obtained from signing a message

# initialize hash object with state of a vulnerable hash
fake_hash = md5py.new('A' * 64)
fake_hash.A, fake_hash.B, fake_hash.C, fake_hash.D = md5py._bytelist2long(legit.decode('hex'))

malicious = ''  # put your malicious message here

# update legit hash with malicious message
fake_hash.update(malicious)

# test is the correct hash for md5(secret + message + padding + malicious)
test = fake_hash.hexdigest()
print(test)


#############################
### STEP 2: Craft payload ###
#############################

# TODO: calculate proper padding based on secret + message
# secret is 6 bytes long (48 bits)
# each block in MD5 is 512 bits long
# secret + message is followed by bit 1 then bit 0's (i.e. \x80\x00\x00...)
# after the 0's is a bye with message length in bits, little endian style
# (i.e. 20 char msg = 160 bits = 0xa0 = '\xa0\x00\x00\x00\x00\x00\x00\x00\x00')
# craft padding to align the block as MD5 would do it
# (i.e. len(secret + message + padding) = 64 bytes = 512 bits
padding = 

# payload is the message that corresponds to the hash in `test`
# server will calculate md5(secret + payload)
#                     = md5(secret + message + padding + malicious)
#                     = test
payload = message + padding + malicious

# send `test` and `payload` to server (manually or with sockets)
# REMEMBER: every time you sign new data, you will regenerate a new secret!
