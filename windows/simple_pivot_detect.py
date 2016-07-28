#!/usr/bin/env python

import os
import subprocess

a = subprocess.Popen('netstat -ano ', shell=True, stdout=subprocess.PIPE)
out, err = a.communicate()

pids = []
alerts = []


count = 0

if out is not None:
	for entry in out.split("\n"):
		if "ESTABLISHED" in entry:
			entry = entry.split()[4]
			if entry not in pids:
				pids.append(entry)
			
if len(pids) > 0:
	a = subprocess.Popen('wmic process get processid,parentprocessid', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	outnew, err = a.communicate()
	for pid in pids:
		if len(pid) > 0 and pid != 0:
			ppid = None
			while ppid == None or int(ppid) > 0:
				#print pid, ppid
				for line in outnew.split("\n"):
					#print line
					ll = line.split()
					if len(ll) > 0 and pid == ll[0]:
						ppid = ll[1].strip()
						for entry in out.split("\n"):
							if str(ppid) in entry and "ESTABLISHED" in entry:
								a = subprocess.Popen('tasklist /fi "pid eq '+ppid+'" | find "'+ppid+'"', shell=True, stdout=subprocess.PIPE)
								out, err= a.communicate()
								out = out.split()[0]
								alerts.append( "Alert: %s :: %s" % (str(ppid), out))
								ppid = 0
							else:
								if ppid == None:
									ppid = 0
								pid = ppid
								count += 1
					else:
						ppid = 0
						
						
						
for alert in alerts:
	print alert 
