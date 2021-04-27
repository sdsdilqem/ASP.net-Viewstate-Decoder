#!/usr/bin/python3

# Small tool to decode ASP.NET __VIEWSTATE variable
#
#
# 

import viewstate
import exceptions
import sys
import colors as c

#
# 08.01.2020
#
## Valid format: "/wEPDwU[a-zA-Z0-9=]+"

c.print_red("** ASP.NET __VIEWSTATE decoder **\n")
c.print_red("** ASP.NET __VIEWSTATE decode edici.  **\n")

if len(sys.argv) != 2:
    print("Usage / istifadesi:  decoder.py \"<__VIEWSTATE ASP.NET string>\"")
    print("Example / numune: decoder.py \"/wEwRDwEweWRkoCvssdUOH7PD446REdvEOF6GBCq0=\"")
    sys.exit()

vst= sys.argv[1]

c.print_blue("[*] Decoding __VIEWSTATE:")
print(vst)
try:
    vs= viewstate.ViewState(vst)
    c.print_green(str(vs.decode()))
except exceptions.ViewStateException as e:
    print (e)
except IndexError as e:
    print (e)
