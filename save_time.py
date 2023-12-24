from datetime import datetime
nw = datetime.now()
nw = datetime.strftime(nw, "%Y-%m-%d %H:%M:%S")
with open("saved_time.txt", "w") as f:
    f.write(nw)
    f.close()
print(f"Saved time is {nw}")
