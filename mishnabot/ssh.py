from typing import List
import re
from pathlib import Path
from os import getcwd
import spur


def ssh(command: List[str], daemon: bool, cwd: str) -> bytes:
    """
    Do something with SSH.

    :param command: The command.
    :param daemon: If True, launch as a daemon.
    :param cwd: The current working directory.

    :return: The output result.
    """

    secrets = Path(getcwd()).joinpath("secrets.txt").read_text()
    # Get SSH credentials.
    ssh_username = re.search(r"ssh_username=(.*)", secrets).group(1)
    ssh_password = re.search(r"ssh_password=(.*)", secrets).group(1)
    hostname = re.search(r"hostname=(.*)", secrets).group(1)
    # Spawn a daemon process and run the bot.
    shell = spur.SshShell(hostname=hostname, username=ssh_username, password=ssh_password)
    if daemon:
        shell.spawn(command, cwd=cwd)
        return b''
    else:
        return shell.run(command, cwd=cwd).output
