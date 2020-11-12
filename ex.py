#!/usr/bin/python
# encoding: utf-8
import sys
from workflow import Workflow3
log = None

def main(wf):
    # The Workflow instance will be passed to the function
    # you call from `Workflow.run`

    # Your imports here if you want to catch import errors
    #import urllib.request
    import urllib2
    import json

    # Get args from Workflow as normalized Unicode
    args = wf.args

    # Do stuff here ...
    desired_base = "USD"
    symbols = ["EUR", "GBP"]
    fixer_io_key = wf.settings['fixer_io_key']
    log.debug (wf.settings['fixer_io_key'])
    if fixer_io_key == "":
        #wf.notify.notify(title="fixer.io key required",text="type 'exr key' to set API key for fixer.io")
        wf.add_item(uid="exr key",title="type 'exr key' to set API key for fixer.io", valid=False)
    else:
        symbols_parameter = "&symbols="+desired_base
        for symbol in symbols:
            symbols_parameter = symbols_parameter+","+symbol

        url = "http://data.fixer.io/api/latest?access_key="+fixer_io_key+symbols_parameter+"&format=1"

        #log.debug (url)

        req = urllib2.Request(url)

        ##parsing response
        r = urllib2.urlopen(req).read()
        cont = json.loads(r.decode('utf-8'))
        log.debug (cont)
        success = cont['success']
        if (success):
            #log.debug (success)
            base = cont['base']

            #check to make sure that the base returned is what we want, if not, we need to convert the values
            if (base != desired_base):
                #log.debug ("fix it")
                cont["base"]=desired_base
                #log.debug (cont["rates"][desired_base])
                desired_base_rate=(cont["rates"][desired_base])
                cont["rates"][desired_base]="1.00"

                for symbol in symbols:
                    #log.debug (cont["rates"][symbol])
                    converted_rate = str(round(cont["rates"][symbol]/desired_base_rate,4))
                    cont["rates"][symbol]=converted_rate

            #log.debug (cont)
            wf.add_item(uid=desired_base,title=desired_base,subtitle=cont["rates"][desired_base],arg=cont["rates"][desired_base])
            for symbol in symbols:
                wf.add_item(uid=symbol,title=symbol,subtitle=cont["rates"][symbol],arg=cont["rates"][symbol])
        else:
            wf.add_item(uid="exr key",title="fixer.io call failed, save your key via 'exr key'", valid=False)
    # Send output to Alfred
    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow3()
    # Assign Workflow logger to a global variable for convenience
    log = wf.logger
    sys.exit(wf.run(main))
