#!//usr/local/bin/python
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
        symbols = wf.settings['symbols']
        if not symbols:
            symbols = []
        symbols.append(args[0])
        wf.settings['symbols'] = symbols
        wf.settings.save()
        log.debug("set the symbols to: "+symbols)
    else:
       wf.add_item(uid="ex key",title="set the key")

    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow3()
    # Assign Workflow logger to a global variable for convenience
    log = wf.logger
    sys.exit(wf.run(main))
