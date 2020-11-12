#!/usr/bin/python
# encoding: utf-8
import sys
from workflow import Workflow3
log = None

def main(wf):
    # The Workflow instance will be passed to the function
    # you call from `Workflow.run`

    # Your imports here if you want to catch import errors

    # Get args from Workflow as normalized Unicode
    args = wf.args
    log.debug("args size "+str(len(args)))

    if (len(args) > 0):
        wf.settings['fixer_io_key'] = args[0]
        wf.settings.save()
        log.debug("set the key to: "+args[0])
    else:
       wf.add_item(uid="exr key",title="set the key")

    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow3()
    # Assign Workflow logger to a global variable for convenience
    log = wf.logger
    sys.exit(wf.run(main))
