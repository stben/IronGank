from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
# 用例导入


from server import settings

import xlrd


def upload_file(request):
    if request.method == "POST":    # 请求方法为POST时，进行处理

        myFile = request.FILES.get(
            "my_file", None)    # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            request.session['message'] = 'Upload error!'
            return HttpResponseRedirect('/admin/auth/user/add/')
        else:
            filename = '%s/%s' % (settings.MEDIA_ROOT, myFile.name)

            destination = open(filename, 'wb+')    # 打开特定的文件进行二进制的写操作
            for chunk in myFile.chunks():      # 分块写入文件
                destination.write(chunk)
            destination.close()

            main(filename)
            request.session['message'] = 'Upload success!'
            return HttpResponseRedirect('/admin/auth/user/add/')


def open_excel(file='file.xlsx'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(str(e))
# 根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以
# ，by_index：表的索引


def excel_table_by_index(file='', colnameindex=0, by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows  # 行数
    ncols = table.ncols  # 列数
    colnames = table.row_values(colnameindex)  # 某一行数据
    list = []
    for rownum in range(1, nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
            list.append(app)
    return list

# 根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以
# ，by_name：Sheet1名称


def excel_table_by_name(file='', colnameindex=0, by_name=u'Sheet1'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows  # 行数
    colnames = table.row_values(colnameindex)  # 某一行数据
    list = []
    for rownum in range(1, nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
            list.append(app)
    return list


def main(file):
    tables = excel_table_by_index(file)
    for one in tables:
        for k in one.values():
            if isinstance(k, float):
                password = str(int(k))
            else:
                username = str(k)
        user = User(username=username, password=password)
        user.save()
