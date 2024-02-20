# -*- coding: utf-8 -*-
num_2 =[]
num = range(10)
for a1 in num:
    for a2 in num:
        num_2.append(str(a1)+str(a2))

netiv =input('Enter a file path ').replace('\\' ,"\\\\").replace('"','')

from PyPDF3 import PdfFileWriter, PdfFileReader
from PyPDF3.pdf import PageObject

num_acpalot = input('Enter the number of times you want to multiply each page for example 3*3'[::-1])

pdf_filenames = netiv
output = PdfFileWriter()
input1 = PdfFileReader(open(pdf_filenames, "rb"), strict=False)
sac_dapim = input1.numPages
for i in range (sac_dapim):

    input1 = PdfFileReader(open(pdf_filenames, "rb"), strict=False)

    page1 = input1.getPage(i)

    total_width = page1.mediaBox.upperRight[0] * int(num_acpalot.split('*')[0])
    total_height = page1.mediaBox.upperRight[1] * int(num_acpalot.split('*')[1])
    print(total_width)
    print(total_height)
    new_page = PageObject.createBlankPage(None, total_width, total_height)
    print(i)
    # Add second page with moving along the axis x
    for aa in range (int(num_acpalot.split('*')[0])):
        for bb in range (int(num_acpalot.split('*')[1])):
            new_page.mergeTranslatedPage(page1, page1.mediaBox.upperRight[0]*aa, page1.mediaBox.upperRight[1]*bb)


    output.addPage(new_page)
ik=open(netiv[:-4:] +' doubled.pdf' , "wb")
output.write(ik)
ik.close()
