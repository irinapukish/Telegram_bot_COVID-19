def get_from_txt(txtpath):
    with open(txtpath, 'r', encoding='utf8') as f:
        txt_string = f.read()
        return txt_string
