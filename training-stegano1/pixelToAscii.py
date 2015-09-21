import binascii
import sys

word = ""

with open(sys.argv[1]) as f:
    for line in f:
        print "#{line}".format(line=line.strip())
        pixBin = bin(int(line))
#        print "pixBin is {pixBin}".format(pixBin=pixBin)
        print pixBin
	n = int(pixBin,2)
	#print "n is {n}".format(n=n)
        letter = binascii.unhexlify('%x' % n)
        print letter
	word += letter

print word
