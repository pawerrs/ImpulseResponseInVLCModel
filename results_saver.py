from openpyxl import load_workbook, Workbook
import utils

def save(file_name, values):

    workbook = Workbook()
    dest_filename = file_name
    worksheet = workbook.active
    worksheet.title = 'Input parameters'

    for i, header in enumerate(utils.get_headers()):
        worksheet.cell(row=1, column=i+1).value = header

    for row_index, row in enumerate(values):
        for column_index, column in enumerate(row):
            worksheet.cell(row=2 + row_index, column=1 + column_index).value = column

    workbook.save(filename = dest_filename)

    print(workbook.sheetnames)