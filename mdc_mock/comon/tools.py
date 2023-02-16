import zipfile
import os


class FileHandle():
    @staticmethod
    def file_iterator(f, chunk_size=512):
        with open(f, 'rb') as fp:
            while True:
                c = fp.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    @staticmethod
    def zip_dir(dir_name, zip_file_name):
        file_list = []
        if os.path.isfile(dir_name):
            file_list.append(dir_name)
        else:
            for root, dirs, files in os.walk(dir_name):
                for name in files:
                    file_list.append(os.path.join(root, name).replace("\\", "/"))
        zf = zipfile.ZipFile(os.path.join(dir_name, zip_file_name), "w", zipfile.zlib.DEFLATED)
        for tar in file_list:
            arc_name = tar[len(dir_name):]
            zf.write(tar, arc_name)
        zf.close()
