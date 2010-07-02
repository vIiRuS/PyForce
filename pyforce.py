#!/usr/bin/python
# -*- coding: utf-8 -*-

#       pyforce.py
#       
#       Copyright 2010 vIiRuS <viirus@pherth.net>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import hashlib
import sys
import time
import thread

def passwordforce(length):
	print "length", length
	suggestlist = ["a"]
	for b in range(1, length):
		suggestlist.append("a")
	
	i = len(suggestlist)-1
	n = 1
	m = 1
	while True:
		for c in characterlist:
			suggestlist[i] = c
			#print "".join(suggestlist)
			hash = hashlib.md5("".join(suggestlist)).hexdigest()
			if hashlib.md5("".join(suggestlist)).hexdigest() == forcehash:
				print "The password is", "".join(suggestlist)
				end = time.clock()
				print "The search took", end - start, "seconds"
				quit()
		#print "".join(suggestlist)
		#print -n, suggestlist[-n]
		while suggestlist[-n] == characterlist[-1]:
			#print n, suggestlist, suggestlist[-n]
			suggestlist[-n] = characterlist[0]
			m = m+1
			#print len(suggestlist), n
			if len(suggestlist) != n:
				n = n+1
		#print len(suggestlist), n, m	
		if m > len(suggestlist):
			reached = time.clock()
			print "reached", len(suggestlist), "characters in", reached-start, "seconds"
			suggestlist.append("a")
			i = i+1
		else:
			#print suggestlist[-n], characterlist[characterlist.index(suggestlist[-n])+1]
			suggestlist[-n] = characterlist[characterlist.index(suggestlist[-n])+1]
		n = 1
		m = 1

try:
	forcehash = sys.argv[1]
except IndexError:
    print "Specify the hash that you wan't to bruteforce as first argument"
else:
	start = time.clock()
	characterlist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
	passwordforce(0)
	#for b in range(0, threadcount):
		#thread.start_new_thread(passwordforce, (b, ))
	#while True: 
		#pass
		