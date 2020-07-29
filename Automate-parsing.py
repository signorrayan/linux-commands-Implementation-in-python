import os

os.chdir('/home/pytm/Desktop/filefolder')

# print('\n'.join(os.listdir()))
for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    f_detail, f_title, f_num = file_name.split('-')
    f_detail = f_detail.strip()
    f_title = f_title.strip()
    f_num = f_num.strip()[1:].zfill(2)
    new_name = f"{f_num}-{f_title}-{f_detail}{file_ext}"

    os.rename(f, new_name)
