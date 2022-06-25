from pathlib import Path
from PIL import Image

src = Path("/Users/dim/Documents/Resident/Resident/webcam/")
dst = Path("/Users/dim/Documents/Resident/Resident/webcam_processed/")

if not dst.is_dir():
    dst.mkdir(parents=True)

files = sorted(src.rglob("*.jpg"))

counter = 0
for i in range(0, len(files)):
    f_dst = dst / (str(counter).zfill(6) + '.jpg')

    if i > 0:
        if files[i].stat().st_size == files[i - 1].stat().st_size:
            print(files[i].stem, f_dst.stem, 'skipped [duplicated]', sep=' ---> ')
            continue
    try:
        img = Image.open(files[i])
        img.save(f_dst)
        print(files[i].stem, f_dst.stem, 'success', sep=' ---> ')
        counter += 1
    except OSError or IOError:
        print(files[i].stem, f_dst.stem, 'skipped [bad file]', sep=' ---> ')
