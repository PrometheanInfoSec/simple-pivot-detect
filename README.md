#Simple Pivot Detect
Simple pivot detect functions in an incredibly straightforward way.  It takes a look at all the processes that are currently running on your system with an established conection.  It then runs up the chain, looking for that process'es first parent.  It then checks to see if the first parent is a process with an established connection.  If it is, then an alert is triggered.

In short, this SPD will check if anyone connected to your box remotely, and with that connection spawned another connection.  Pretty simple.
