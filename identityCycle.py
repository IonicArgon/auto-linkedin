import subprocess
import os

# get current working directory
cwd = os.getcwd()

# folder of identities
identityFolder = os.path.join(cwd, "identities")

# get the url string from target file
def getURL(target):
    url = ""
    with open(target, "r") as f:
        url = f.readline()
    return url
url = getURL("talent_links/sampleIBio2027.txt")

# arguments for the scripts
args = [
    "-m", "src.recruiter", "find",
    "--url", f"{url}",
    "--start", "0",
    "--count", "25",
    "--end", "143"
]

# loop through all the identities and execute the script
with open("stdout.txt", "w") as f_obj:
    for folder in os.listdir(identityFolder):
        if folder.startswith("."):
            continue

        identity = os.path.join(identityFolder, folder)
        print(f"Identity: {identity}\n")
        subprocess.run(["py", *args, "--identity", f"{identity}", "--output", f"output/identityTest/{folder}.json"], stdout=f_obj)