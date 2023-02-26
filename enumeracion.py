import subprocess

def dns_enum(domain):
    dns_results = []

    # dnsrecon
    dnsrecon_result = subprocess.check_output(['dnsrecon', '-d', domain, '-t', 'brt'])
    dns_results.append(dnsrecon_result.decode())

    # fierce
    fierce_result = subprocess.check_output(['fierce', '-dns', domain])
    dns_results.append(fierce_result.decode())

    # sublist3r
    sublist3r_result = subprocess.check_output(['sublist3r', '-d', domain])
    dns_results.append(sublist3r_result.decode())

    # amass
    amass_result = subprocess.check_output(['amass', 'enum', '-d', domain])
    dns_results.append(amass_result.decode())

    return dns_results
