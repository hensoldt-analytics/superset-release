import logging
import subprocess
import time
from threading import Thread

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)

def renew_kerberos_ticket(kinit_path, keytab, principal, reinit_time_in_sec):

    login_command = [kinit_path,
                    "-r", "{0}s".format(reinit_time_in_sec),
                    "-kt", keytab,
                    principal]

    LOG.info("Trying to perform kerberos login via command: " + " ".join(login_command))

    subp = subprocess.Popen(login_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True, bufsize=-1)
    subp.wait()

    if subp.returncode != 0:
        LOG.error("Kerberos Login failed! `kinit` exited with %s.\n%s\n%s" % (
            subp.returncode,
            "\n".join(subp.stdout.readlines()),
            "\n".join(subp.stderr.readlines())))

class KerberosLoginThread(Thread):
    def __init__(self, kinit_path, keytab, principal, reinit_time_in_sec):
        super(KerberosLoginThread, self).__init__()
        self.kinit_path = kinit_path
        self.keytab = keytab
        self.principal = principal
        self.reinit_time_in_millis = reinit_time_in_sec

    def run(self):
        while True :
            renew_kerberos_ticket(self.kinit_path, self.keytab, self.principal, self.reinit_time_in_millis)
            time.sleep(int(self.reinit_time_in_millis))