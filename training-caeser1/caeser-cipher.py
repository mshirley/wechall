# modified from https://inventwithpython.com/chapter14.html 

def getMessage():
    print('Enter your message:')
    return raw_input()

def getTranslatedMessage(message, key):
#    if mode[0] == 'd':
    key = -key
    translated = ''
    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            translated += chr(num)
        else:
            translated += symbol
    return translated

def createWords():
    words = []
    try:
    	f = open('/usr/share/dict/words', 'r')
    	words = f.read().split()
    except:
        print('unable to open /usr/share/dict/words')
    return words

def createMessages(message):
    messages = []
    for key in range(1, 26):
        msgtmp = getTranslatedMessage(message, key)
        #print 'Your translated text is: {message}'.format(message=msgtmp)
        messages.append(msgtmp)
    return messages

def printMessages(messages):
    for m in messages:
        print m

def detectWords(messages, words):    
    counter = 0
    matchList = {}
    print('Detecting words...')
    for m in messages:
      msgSplit = m.split()
      for s in msgSplit:
         if s.lower() in words or s.upper() in words:
           counter += 1
      matchList[m] = counter
      counter = 0
    
    winner = {}
    leader = 0
    for k, v in matchList.iteritems():
      if v > leader:
        leader = v
        leaderKey = k
    if leader == 0:
      print 'No words detected' 
    else:
      winner[leaderKey] = leader
      print winner

message = getMessage()
messages = createMessages(message)
printMessages(messages)

words = createWords()
if len(words) > 0:
    detectWords(messages, words)

#MAX_KEY_SIZE = 26
#
#def getMode():
#    while True:
#        print('Do you wish to encrypt or decrypt a message?')
#        mode = input().lower()
#        if mode in 'encrypt e decrypt d'.split():
#            return mode
#        else:
#            print('Enter either "encrypt" or "e" or "decrypt" or "d".')
#
#def getKey():
#    key = 0
#    while True:
#        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
#        key = int(input())
#        if (key >= 1 and key <= MAX_KEY_SIZE):
#            return key
#mode = getMode()
#key = getKey()

