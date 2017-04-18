#!/usr/bin/env python
import sys
import whois
import socket

def print_seperator(char="=",length=79):
    print char * length

def lookup_domain(domain):
    try:
        ip_addr = socket.gethostbyname(domain)
    except e:
        ip_addr = e

    return ip_addr

domains = sys.argv[1:]

for domain in domains:
    try:
        name_servers = whois.query(domain).name_servers
        ip_addr = lookup_domain(domain)
    except:
        name_servers = []
        ip_addr = None

    print_seperator()
    print "%s (%s)" % (domain,ip_addr)

    for nameserver in name_servers:
        print "{0:>40} ({1})".format(nameserver,lookup_domain(nameserver))
