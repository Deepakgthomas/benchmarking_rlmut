import subprocess
with open("stdout.txt", "w") as stdout, open("stderr.txt", "w") as stderr:
    result = subprocess.run(["bash", "test.sh", "2"], stdout=stdout, stderr=stderr,text=True, check=True)