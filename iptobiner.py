#!/usr/bin/env python
def iptobiner(ip_add):
	ip_add = int(ip_add)
	if ip_add >= 128:
		a1 = "1" # True
		a2 = ip_add - 128
	else:
		a1 = "0" # False
		a2 = ip_add

	if a2 >= 64:
		b1 = "1" # True
		b2 = a2 - 64
	else:
		b1 = "0"
		b2 = a2	# False
	
	if b2 >= 32:
		c1 = "1" # True
		c2 = b2 - 32
	else:
		c1 = "0" # False
		c2 = b2

	if c2 >= 16:
		d1 = "1" # True
		d2 = c2 - 16
	else:
		d1 = "0" # False
		d2 = c2

	if d2 >= 8:
		e1 = "1" # True
		e2 = d2 - 8
	else:
		e1 = "0" # False
		e2 = d2

	if e2 >= 4:
		f1 = "1" # True
		f2 = e2 - 4
	else:
		f1 = "0" # False
		f2 = e2

	if f2 >= 2:
		g1 = "1" # True
		g2 = f2 - 2
	else:
		g1 = "0" # False
		g2 = f2

	if g2 >= 1:
		h1 = "1" # True
		h2 = g2 - 1
	else:
		h1 = "0" # False
		h2 = g2

	return a1 + b1 + c1 + d1 + e1 + f1 + g1 + h1

ip_address = raw_input("Input your IP Address: ")
ip_address = ip_address.split(".")
for ip in ip_address:
    print iptobiner(ip)
