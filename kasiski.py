from math import sqrt

def encrypt(plain, key):
	k = pad(plain, key)
	p = formatText(plain)
	c = ""
	for i in range(0, len(p)):
		c += chr(65 + (ord(p[i]) + ord(k[i])) % 26)
	return c
		
def decrypt(cipher, key):
	k = pad(cipher, key)
	c = formatText(cipher)
	p = ""
	for i in range(0, len(c)):
		p += chr(65 + (ord(c[i]) - ord(k[i])) % 26)
	return p
		
def pad(text, key):
	orig_len = len(key)
	while len(key) < len(text):
		key += key[ len(key) % orig_len ]
	return key
def formatText(text):
	clean = "".join(text.split(" "))
	clean = "".join(clean.split("\n"))
	clean = "".join(clean.split("\t"))
	clean = "".join(clean.split("."))
	return clean
	
def readFile(path):
	f = open(path, "rb")
	filebytes  =  []
	b = f.read(1)
	while b:
		filebytes.append(b)
		b = f.read(1)
	f.close()
	return filebytes

#http://www.robindavid.fr/blog/2012/06/15/kasiski-babbage-cryptanalysis-in-python/

def getDivisors(n):
	div = []
	for i in range(2, int(sqrt(n)) + 1): ## DON"T NEED TO GO FURHTER THAN sqrt(n), NUMBER THEORY...
		if n % i == 0:
			div.append(i)
	return div
	

def getTuples(l):
    res = {}
    freq =[]
    count = 0
    i = 0
    while i < len(l): # Loop through all the list
        elt= l[i:i+3] # Take at least 3-character length for tuples
        long = len(elt)
        if long == 3: #should be 3 if not means we are at the end of the list
            for j in range(i+1,len(l)): #Find further in the list for the same pattern
                if l[i:i+long] == l[j:j+long]: #If match the 3-char check for more
                    while l[i:i+long] == l[j:j+long]:
                        long = long + 1
                    long = long -1
                    elt = l[i:i+long] # Now we have a tuple 
                    diff = j - i # Compute the distance
                    freq.extend(getDivisors(diff)) #Add the divisors to the list 
                    print ("%s\ti:%s\tj:%s\tdiff:%s\t\tDivisors:%s" % (elt,i,j, diff,getDivisors(diff))) #Print information about the tuple (can be deleted)
                    count = count +1
                    j = j + long + 1
            i = i + long -3 +1
        else:
            i = i + 1
    return count, freq
	

	
if __name__ == "__main__":
	formattedPlain = formatText("""Eci ouch ptdvwjvv Dm ymftmkblpu oplu azavcuz grw vvdh echxoghzl vvsk wqg ca bkkg
vavkuiuhph Ow fqakthvs oph pssb vvsk wi vvz ivuwbvpgbo grw apaw uiwulv hcm
fqrz wi vvz brqzn grw inmg vc ymftmkb wjwn uhugvoh kb v Olvvpj ugdjalvcmg
Bqi pahf o Fivkgfq hzohqqchdwq cby bkgb v juwhz nrtqz wq czg shag jn
wjs yqvecqmugr gmqihc a Vwphqw vvz krfs twx wgzl iqf wwwj ca bkggz awgdn br c
dmqychz Olvvpj ugdjalvcmg qcazl fu1653 jdohpsmm ddq123 rphts vjf123 kg twxt
Ddbw wgzzqcaz ahromiwg hcm zqfya zkhc lduvza Vjomm wjwn zhrcnqwqft elvv oph VO qqfvcmhkb Wa grw gjtygr nbhr
cim xuwio hphdzhnm kmq cby xdrsm afcb twxt vvvgyfdbwgb ywfwazvw cby axdadb lv
Wi mlvvzz fcgz axdadb d tsvlpg tdth fsnkukpdvj acpz drdmwdev Dn bqi ciyg zdbwns
ywfwazvwchdwq cpjcw acpz vqzpblqb twx oot kkqcnm wq whxogazvw c pvale Yvaluyd
macadvdvwjv wq siaxts opdv mjc jgh acon djqqvg jv wjwn awgd jn wjs vavkuiuhph""")
	f = open("vigenere.txt", 'w')
	f.write(formattedPlain)
	f.close()
	print("Getting possible divisors ")
	
	l = readFile("text.txt")
	divs = getTuples(l)[1]
	print(divs)
	divs_dict = {}
	for i in divs:
		if i in divs_dict:
			divs_dict[i] += 1
		else:
			divs_dict[i] = 1
	print(sorted(divs_dict.items(),key=lambda x: x[1], reverse=True))
	