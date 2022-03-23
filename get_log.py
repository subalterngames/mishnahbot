from pathlib import Path
import re
from mishnabot.ssh import ssh

# Read the log.
if __name__ == "__main__":
    secrets = Path("secrets.txt").read_text()
    resp = ssh(command=["cat", "log.txt"],
               cwd=re.search(r"ssh_cwd=(.*)", secrets).group(1),
               daemon=False).decode("utf-8")
    print(resp)
