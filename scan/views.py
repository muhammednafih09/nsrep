from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
import json
import nmap3

@login_required(login_url='login')
def load_json_table_format(request):
    
    host = '127.0.0.1'

    nmap = nmap3.Nmap()
    results = nmap.scan_top_ports(host)

    print(results[host])
    data = results[host]

    return render(request, 'scan/scan.html', data)


@login_required(login_url='login')
def scan_form(request):
    page = "scan-form"
    context = {'page': page}
    return render(request, 'scan/scan_form.html', context)