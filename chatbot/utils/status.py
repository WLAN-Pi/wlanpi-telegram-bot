import os


def get_status():

    stream = os.popen("/opt/wlanpi-chat-bot/etc/scripts/probe_status_msg.sh")
    startup_msg = stream.read()

    return startup_msg