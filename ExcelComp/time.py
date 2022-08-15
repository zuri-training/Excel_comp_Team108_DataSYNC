
@ login_required(login_url='login')
def singlefile(request):
    context = {}
    if request.method == 'POST':
        if 'deletedup' in request.POST:
            uploaded_file = request.FILES['singlefile']
            fs = FileSystemStorage()
            fs.save(uploaded_file.name, uploaded_file)
            # print(fs.url(uploaded_file.name, uploaded_file))
            # fs.url(name)
            excel_file = uploaded_file
            # print(excel_file)

            file_df = pd.read_excel(excel_file)
            # source_df = pd.DataFrame(file_df)
            # print('Source DataFrame:\n', source_df)
            result_df = file_df.drop_duplicates()
            # print('Result DataFrame:\n', result_df)
            result_df.to_excel(
                f"ExcelComp/singlefiles/cleaned{dt_string + uploaded_file.name}.xlsx")
            dropname = (
                f"cleaned{dt_string + uploaded_file.name}.xlsx")
            context['url'] = fs.url(dropname)
        elif 'compare' in request.POST:
            uploaded_file = request.FILES['singlefile']
            fs = FileSystemStorage()
            fs.save(uploaded_file.name, uploaded_file)
            # fs.url(name)
            excel_file = uploaded_file
            file_df = pd.read_excel(excel_file)
            df2 = pd.DataFrame(file_df)

            # df2.loc[df2.duplicated(keep=False), :]

            hello = df2.loc[df2.duplicated(keep=False), :]

            keyword1 = df2.columns[0]
            keyword2 = hello.columns[0]

            duplicated = df2[keyword1].isin(hello[keyword2])

            def row_styler(row):
                return ['background-color: yellow' if duplicated[row.name] else ''] * len(row)

            df2.style.apply(row_styler, axis=1)
            result_df2 = df2.style.apply(row_styler, axis=1)
            result_df2.to_excel(
                f"ExcelComp/singlefiles/compare{dt_string + uploaded_file.name}.xlsx")
            dropname = (
                f"compare{dt_string + uploaded_file.name}.xlsx")
            context['url'] = fs.url(dropname)
        elif 'deletedup1' in request.POST:
            uploaded_file = request.FILES['singlefile']
            fs = FileSystemStorage()
            fs.save(uploaded_file.name, uploaded_file)
            # print(fs.url(uploaded_file.name, uploaded_file))
            # fs.url(name)
            excel_file = uploaded_file
            # print(excel_file)

            file_df = pd.read_excel(excel_file)
            # source_df = pd.DataFrame(file_df)
            # print('Source DataFrame:\n', source_df)

    return render(request, 'singlefile.html', context)
