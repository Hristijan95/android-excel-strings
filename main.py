import xlrd

# The excel file path (e.g. C:\Users\username\Desktop\strings.xls)
file_path = r'android_strings.xlsx'
output_file_name = r'strings.xml'
document = xlrd.open_workbook(file_path)
sheet = document.sheet_by_index(0)  # If the document has more than one sheet, specify the desired sheet here


def convert_excel_to_xml():
    fw = open(output_file_name, 'w')
    count = 0
    while count < sheet.nrows:
        # Change cell_value(row, column) according to your document
        row = '<string name="' + sheet.cell_value(count, 0) + '">' + sheet.cell_value(count, 1) + '</string>\n'
        fw.write(row)
        count += 1
    fw.close()


convert_excel_to_xml()
