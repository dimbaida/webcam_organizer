import os
from PIL import Image


def process_images(source_folder, destination_folder):

    if not os.path.exists(destination_folder):
        os.mkdir(destination_folder)

    counter = 0
    prev_filesize = 0
    corrupted_files = []
    doubled_files = []

    for root, dirs, files in os.walk(source_folder):
        for f in files:
            old = os.path.join(root, f)
            print('Now processing: ' + os.path.basename(f), sep="")
            ext = os.path.splitext(f)[1]
            new = os.path.join(destination_folder, 'webcam_' + str(counter).zfill(6) + ext)

            curr_filesize = os.path.getsize(old)

            if curr_filesize != prev_filesize:
                if os.path.exists(new):
                    os.remove(new)
                try:
                    im = Image.open(old)
                    im.save(new)
                except IOError:
                    corrupted_files.append(old)
                    print('>>>>>>> Corrupted')
                    continue
                counter += 1
                prev_filesize = curr_filesize
                print(' >> Ok')
            else:
                doubled_files.append(old)
                print('>>>>>>> Doubled')

    print('Corrupted:')
    for f in corrupted_files:
        print(os.path.basename(f))

    print('Doubled:')
    for f in doubled_files:
        print(os.path.basename(f))
