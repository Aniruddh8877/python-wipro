import tarfile

# with tarfile.open("test.tar.gz", "w:gz") as tar:
#      tar.add("test.txt")
#      tar.add("test2.txt")

with tarfile.open("test.tar.gz", "r:gz") as tar:
     tar.extractall()