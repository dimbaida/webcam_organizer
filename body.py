from pathlib import Path
from PIL import Image

src = Path("/Users/dim/Documents/Resident/Resident/webcam/")
dst = Path("/Users/dim/Documents/Resident/Resident/webcam_processed/")

if not dst.is_dir():
    dst.mkdir(parents=True)

files = sorted(src.rglob("*.jpg"))

counter = 0
for i in range(0, len(files)):
    f = files[i]
    f_new = dst / (str(counter).zfill(6) + '.jpg')

    if i > 0:
        f_prev = files[i - 1]
        if f.stat().st_size == f_prev.stat().st_size:
            print(f.stem, f_new.stem, 'skipped [duplicated]', sep=' ---> ')
            continue
    try:
        img = Image.open(f)
        img.save(f_new)
        print(f.stem, f_new.stem, 'saved', sep=' ---> ')
        counter += 1
    except OSError or IOError:
        print(f.stem, f_new.stem, 'skipped [bad file]', sep=' ---> ')
