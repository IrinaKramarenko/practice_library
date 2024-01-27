import pytesseract as pt
pt.pytesseract.tesseract_cmd = r'D:\Tesseract\tesseract.exe'


def get_values(image, type_note):
    string = pt.image_to_string(image, lang='rus')
    if string == "":
        string = get_handwr_values(image)
    return string

def get_handwr_values(image):
    return 'handwriting'