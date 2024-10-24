import pandas as pd
from django.shortcuts import render
from .forms import CsvFileForm


def home(request):
    if request.method == "POST":
        form = CsvFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            file_name = uploaded_file.name
            file_extension = file_name.split('.')[-1].lower()

            try:
                if file_extension == 'csv':
                    df = pd.read_csv(uploaded_file)
                elif file_extension in ['xlsx', 'xls']:
                    df = pd.read_excel(uploaded_file)
                else:
                    return render(request, 'index.html', {'form': form, 'error': 'Unsupported file type'})
                headings = df.columns.tolist()
                data = df.values.tolist()

                return render(request, 'displaycsv.html', {'headings': headings, 'data': data})

            except Exception as e:
                return render(request, 'index.html', {'form': form, 'error': str(e)})
    
    else:
        form = CsvFileForm()
    
    return render(request, 'index.html', {'form': form})
