#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/27 10:11
# @Author  : SmallStrong
# @Des     : 
# @File    : pdf_img_core.py
# @Software: PyCharm
import os
import PyPDF2 as pdf
from pdf2image import convert_from_bytes

FILE_PATH = "/Users/smallstrong/Desktop/bc"


def go():
    file_names = []
    for filename in os.listdir(FILE_PATH):
        if '.pdf' in filename:
            file_names.append(filename)

    try:
        for f in file_names:
            name = f.split(".pdf")[0]
            reader = pdf.PdfFileReader('{}/{}'.format(FILE_PATH, f))
            page = reader.getPage(0)
            pdf_writer = pdf.PdfFileWriter()
            pdf_writer.addPage(page)
            with open(os.getcwd() + "/temp.pdf", 'wb') as fh:
                pdf_writer.write(fh)
            images = convert_from_bytes(open("./temp.pdf", 'rb').read())
            images[0].save(os.getcwd() + "/img/{}.jpg".format(name))
    except Exception as e:
        print("error file name is :" + f)
        print(e)
    os.remove(os.getcwd() + "/temp.pdf")


if __name__ == '__main__':
    go()
