#!/usr/bin/env python
def binertoip(ip_add):
	if ip_add[0:1] == "1":
		a = 128
	else:
		a = 0
	if ip_add[1:2] == "1":
		b = 64
	else:
		b = 0
	if ip_add[2:3] == "1":
		c = 32
	else:
		c = 0
	if ip_add[3:4] == "1":
		d = 16
	else:
		d = 0
	if ip_add[4:5] == "1":
		e = 8
	else:
		e = 0
	if ip_add[5:6] == "1":
		f = 4
	else:
		f = 0
	if ip_add[6:7] == "1":
		g = 2
	else:
		g = 0
	if ip_add[7:8] == "1":
		h = 1
	else:
		h = 0

	return a + b + c + d + e + f + g + h

ip_address = raw_input("Input your binary (8 bit): ")
ip_address = ip_address.split(".")
for biner in ip_address:
	print binertoip(biner)
