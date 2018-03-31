import math

def make_readable(seconds):
    HH = math.floor(seconds/3600)
    seconds -= HH*3600

    MM = math.floor(seconds/60)
    seconds -= MM*60

    return (
        str(HH).zfill(2) + ":" + str(MM).zfill(2) + ":" + str(seconds).zfill(2)
    )

make_readable(86399)
