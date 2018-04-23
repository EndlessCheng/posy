import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES_DIR = os.path.join(BASE_DIR, 'res')


def get_res_file_path(res_filename):
    res_path = os.path.join(RES_DIR, res_filename)
    return res_path
