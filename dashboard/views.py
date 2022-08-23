from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    content = {
        "items" : {
            "Host Discovery" : "A simple scan to discover live hosts and open ports.",
            "OS Detection" : "A system scan to discover host Operating System.",
            "Version Detection" : "A system scan to discover service Versions.",
            "Basic Network Scan" : "A full system scan suitable for any host.",
            "Host Discovery1" : "A simple scan to discover live hosts and open ports.",
            "OS Detection1" : "A system scan to discover host Operating System.",
            "Version Detection1" : "A system scan to discover service Versions.",
            "Basic Network Scan1" : "A full system scan suitable for any host.",
            "Host Discovery2" : "A simple scan to discover live hosts and open ports.",
            "OS Detection2" : "A system scan to discover host Operating System.",
            "Version Detection2" : "A system scan to discover service Versions.",
            "Basic Network Scan2" : "A full system scan suitable for any host.",
            "Host Discovery3" : "A simple scan to discover live hosts and open ports.",
            "OS Detection3" : "A system scan to discover host Operating System.",
            "Version Detection3" : "A system scan to discover service Versions.",
            "Basic Network Scan3" : "A full system scan suitable for any host.",
            }
    }

    return render(request,'dashboard/index.html',content)