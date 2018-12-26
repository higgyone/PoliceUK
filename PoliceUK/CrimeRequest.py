import requests

class CrimeRequest(object):
    """description of class"""

    def __init__(self, urlBase, Payload = None, HookCallback = None):
        self.url = urlBase
        self.payload = Payload
        self.callback = HookCallback
        self.response = None

    def SetUrlBase(self, urlBase):
        self.url = urlBase

    def SetPayload(self, payload):
        self.payload = payload

    def SetHookCallback(self, callback = None):
        self.SetHookCallback = callback

    def RunRequest(self, payload = None, hookType = None):
        pld = self.payload

        hook = None

        if hookType is not None:
            hook = {str(hookType) : [self.Hook]}
        
        if payload is not None:
            pld = payload

        self.response = requests.get(self.url, params=pld, hooks = hook)

        return self.response


