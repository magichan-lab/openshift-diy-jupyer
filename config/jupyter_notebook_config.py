# Configuration file for jupyter-notebook.

import os
WS_URL = 'ws://' + os.environ["OPENSHIFT_APP_NAME"] + '-' + \
    os.environ['OPENSHIFT_NAMESPACE'] + '.rhcloud.com:8000'

c.NotebookApp.ip = '*'
c.NotebookApp.allow_origin = '*'
# c.NotebookApp.password = 'sha1:f47378fec76d:a7411cfd32b857e9466e3fcb3cedcc2a2e7fbb57'
c.NotebookApp.websocket_url = WS_URL
c.ConnectionFileMixin.transport = 'ipc'
