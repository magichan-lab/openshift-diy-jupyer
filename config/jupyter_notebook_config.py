# Configuration file for jupyter-notebook.

import os
from pgcontents import PostgresContentsManager, PostgresCheckpoints

WS_URL = 'ws://' + os.environ["OPENSHIFT_APP_NAME"] + '-' + \
    os.environ['OPENSHIFT_NAMESPACE'] + '.rhcloud.com:8000'

c.NotebookApp.ip = '*'
c.NotebookApp.allow_origin = '*'
# c.NotebookApp.password = 'sha1:f47378fec76d:a7411cfd32b857e9466e3fcb3cedcc2a2e7fbb57'
c.NotebookApp.websocket_url = WS_URL
c.ConnectionFileMixin.transport = 'ipc'

pg_url = os.getenv('OPENSHIFT_POSTGRESQL_DB_URL', None)
pg_usr = os.getenv('OPENSHIFT_POSTGRESQL_DB_USERNAME', None)
if pg_url and pg_usr:
    c.PostgresContentsManager.user_id = 'openshift'
    c.NotebookApp.contents_manager_class = PostgresContentsManager
    c.NotebookApp.checkpoints_class = PostgresCheckpoints
    c.PostgresContentsManager.db_url = pg_url + '/' + \
                                       os.environ["OPENSHIFT_APP_NAME"]
    c.PostgresContentsManager.max_file_size_bytes = 1000000
