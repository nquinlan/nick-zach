name=raw_input("What is your Name?")
print "Oh hi there " + ( name)
print "Your name begins with "+ name[0].lower()
if name[0].lower()=="a":
	word="alphabet"
elif name[0].lower()=="b":
	word="barrel"
elif name[0].lower()=="c":
	word="copy"
elif name[0].lower()=="d":
	word="dunk"
elif name[0].lower()=="e":
	word="epitome"
elif name[0].lower()=="f":
	word="fan"
elif name[0].lower()=="g":
	word="grduge"
elif name[0].lower()=="h":
	word="homework"
elif name[0].lower()=="i":
	word="Indent"
elif name[0].lower()=="j":
	word="jackhammer"
elif name[0].lower()=="k":
	word="kick"
elif name[0].lower()=="l":
	word="lick"
elif name[0].lower()=="m":
	word="master"
elif name[0].lower()=="n":
	word="Nope"
elif name[0].lower()=="o":
	word="Opperator"
elif name[0].lower()=="p":
	word="pie"
elif name[0].lower()=="q":
	word="quarky"
elif name[0].lower()=="r":
	word="right"
elif name[0].lower()=="s":
	word="stunt"
elif name[0].lower()=="t":
	word="Tired"
elif name[0].lower()=="u":
	word="unattentive"
elif name[0].lower()=="v":
	word="varriable"
elif name[0].lower()=="w":
	word="work"
elif name[0].lower()=="x":
	word="xylophone"
elif name[0].lower()=="y":
	word="yak"
elif name[0].lower()=="z":
	word="zebra"
else:
	word="dont be stupid like Nick Quinlan. No names should begin with a number"

print  word +" also begins with " +name[0].lower()

if name.lower()=="nick":
	print "Welcome back Nick!"
if name.lower()=="zach":
	print "Welcome back Zach!"
	