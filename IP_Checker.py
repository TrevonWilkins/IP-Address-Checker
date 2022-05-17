#!/usr/bin/env python
# coding: utf-8

import re
def checkIPAddress(ip):
    """
    IP Address structure and content checker.
    
    :param ip: IPv4/IPv6 address.
    :type number: str

    :return: 'Valid IP(type) Address', 'IP:x.x.x.x'
    :rtype: tuple if valid IP Address input. String if Invalid IP is provided.
    
    Example Command: 'checkIPAddress("2301:0db8:85a3:0000:0000:8a2e:0370:7334")'
    Example Output: ('Valid IPv6 Address', '2301:0db8:85a3:0000:0000:8a2e:0370:7334')
    """
    def ipv4_check(ip=ip):
        ipv4 = ip
        try:
            ipv4 = [ i.lstrip('0') if i != '0' else '0' for i in re.findall(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', ipv4)[0].split('.')]
            x=1
            for i in ipv4:
                if int(i) > 255:
                    del ipv4[x]
                    x+=1
            if ipv4 == []:
                return "Neither"
            elif '{}.{}.{}.{}'.format(ipv4[0], ipv4[1], ipv4[2], ipv4[3]) != ip:
                return "Neither"
            else:
                return '{}.{}.{}.{}'.format(ipv4[0], ipv4[1], ipv4[2], ipv4[3])
        except:
            return "Neither"
        
    def ipv6_check(ip=ip):
        try:
            ipv6 = ip
            ipv6 = re.findall(r'[a-fA-F0-9]{1,4}:[a-fA-F0-9]{1,4}:[a-fA-F0-9]{1,4}:[a-fA-F0-9]{1,4}:[a-fA-F0-9]{1,4}:[a-fA-F0-9]{1,4}:[a-fA-F0-9]{1,4}:[a-fA-F0-9]{1,4}', ipv6)
            if ipv6 == []:
                return "Neither"
            elif ipv6[0] != ip:
                return "Neither"
            else:
                return ipv6[0]
        except:
            return "Neither"
        
    ipv4, ipv6 = ipv4_check(), ipv6_check()
    
    if ipv4 != "Neither":
        return "Valid IPv4 Address", ipv4
    elif ipv6 != "Neither":
        return "Valid IPv6 Address", ipv6
    else:
        return "Invalid IP Address"
