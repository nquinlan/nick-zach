name=raw_input("What is your Name?")
print "Oh hi there " + ( name)
nl=name[0].lower()
fullnl=name.lower()
print "Your name begins with "+ nl
if nl=="a":
	word="alphabet"
elif nl=="b":
	word="barrel"
elif nl=="c":
	word="copy"
elif nl=="d":
	word="dunk"
elif nl=="e":
	word="epitome"
elif nl=="f":
	word="fan"
elif nl=="g":
	word="grduge"
elif nl=="h":
	word="homework"
elif nl=="i":
	word="Indent"
elif nl=="j":
	word="jackhammer"
elif nl=="k":
	word="kick"
elif nl=="l":
	word="lick"
elif nl=="m":
	word="master"
elif nl=="n":
	word="Nope"
elif nl=="o":
	word="Opperator"
elif nl=="p":
	word="pie"
elif nl=="q":
	word="quarky"
elif nl=="r":
	word="right"
elif nl=="s":
	word="stunt"
elif nl=="t":
	word="Tired"
elif nl=="u":
	word="unattentive"
elif nl=="v":
	word="varriable"
elif nl=="w":
	word="work"
elif nl=="x":
	word="xylophone"
elif nl=="y":
	word="yak"
elif nl=="z":
	word="zebra"
else:
	word="dont be stupid like Nick Quinlan. No names should begin with a number"

print  word +" also begins with " +nl

if fullnl=="nick":
	print "Welcome back Nick!"
if fullnl=="zach":
	print "Welcome back Zach!"
	