from krita import *

x=0 #creating a global variable to store state of foreground color

def switchCE(): #main function of the extension where everything happens

    doc=Krita.instance()#.activeDocument()

    if doc is None:
        return
    
    global x #calling the global x to be here in the function

    kritaEraserAction = doc.action("erase_action")
    forgrndAction = doc.action("toggle_fg_bg")
    if kritaEraserAction is not None and kritaEraserAction.isChecked() is True:
        kritaEraserAction.trigger()
        forgrndAction.trigger()
    else:
        if kritaEraserAction is None:
            return
        if x ==0:
            forgrndAction.trigger()
            x=1
        elif x==1:
            kritaEraserAction.trigger()
            x=0

#CSPE extension's class. All boilerplate except createActions
class CSPE(Extension):

    def __init__(self, parent):
        # This is initialising the parent, always important when subclassing.
        super(CSPE,self).__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        action = window.createAction("CSPE", "CSP Style mod X", "tools/scripts")
        action.triggered.connect(switchCE)


# And add the extension to Krita's list of extensions:
Krita.instance().addExtension(CSPE(Krita.instance()))

