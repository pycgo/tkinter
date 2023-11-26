import fitz

'''
pip install fitz
python -m pip install --upgrade pymupdf
'''

def split_pdf(input_file, first_num, last_num):

    # input_file = r'C:\Users\zxx\Downloads/111.pdf'
    doc = fitz.open(input_file)

    list1 = []
    # first_num = 209
    # last_num = 216

    for i in range(first_num - 1, last_num):
        list1.append(i)

    # select 选择的是一个页数列表
    doc.select(list1)

    doc2 = fitz.open()
    doc2.insert_pdf(doc)
    doc2.save(str(first_num) + '-' + str(last_num) + '.pdf')

    doc.close()
    doc2.close()
