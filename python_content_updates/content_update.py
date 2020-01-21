# Copyright (c) 2018, Palo Alto Networks
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

# Author: Scott Shoaf <sshoaf@paloaltonetworks.com>

'''
Palo Alto Networks content_update.py

uses the firewall api to check, download, and install content updates
does both content/threat and antivirus updates

This software is provided without support, warranty, or guarantee.
Use at your own risk.
'''

import argparse
import sys
import time
import pan.xapi


def get_job_id(s):
    '''
    extract job-id from pan-python string xml response
    regex parse due to pan-python output join breaking xml rules
    :param s is the input string
    :return: simple string with job id
    '''

    return s.split('<job>')[1].split('</job>')[0]

def get_job_status(s):
    '''
    extract status and progress % from pan-python string xml response
    regex parse due to pan-python output join breaking xml rules
    :param s is the input string
    :return: status text and progress %
    '''

    status = s.split('<status>')[1].split('</status>')[0]
    progress = s.split('<progress>')[1].split('</progress>')[0]
    return status, progress

def check_job_status(fw, results):
    '''
    periodically check job status in the firewall
    :param fw is fw object being queried
    :param results is the xml-string results returned for job status
    '''

    # initialize to null status
    status = ''

    job_id = get_job_id(results)
    #print('checking status of job id {0}...'.format(job_id))

    # check job id status and progress
    while status != 'FIN':

        fw.op(cmd='<show><jobs><id>{0}</id></jobs></show>'.format(job_id))
        status, progress = get_job_status(fw.xml_result())
        if status != 'FIN':
            print('job {0} in progress [ {1}% complete ]'.format(job_id, progress), end='\r', flush=True)
            time.sleep(5)

    print('\njob {0} is complete'.format(job_id))

def update_content(fw, type):
    '''
    check, download, and install latest content updates
    :param fw is the fw object being updated
    :param type is update type - content or anti-virus
    '''

    print('checking for latest {0} updates...'.format(type))
    fw.op(cmd='<request><{0}><upgrade><check/></upgrade></{0}></request>'.format(type))

    # download latest content
    print('downloading latest {0} updates...'.format(type))
    fw.op(cmd='<request><{0}><upgrade><download><latest/></download></upgrade></{0}></request>'.format(type))
    results = fw.xml_result()

    if '<job>' in results:
        check_job_status(fw, results)

    # install latest content
    print('installing latest {0} updates...'.format(type))
    fw.op(cmd='<request><{0}><upgrade><install><version>latest</version></install></upgrade></{0}></request>'.format(type))
    results = fw.xml_result()

    if '<job>' in results:
        check_job_status(fw, results)


def main():
    '''
    simple set of api calls to update fw to latest content versions
    '''

    # python skillets currently use CLI arguments to get input from the operator / user. Each argparse argument long
    # name must match a variable in the .meta-cnc file directly
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--TARGET_IP", help="IP address of the firewall", type=str)
    parser.add_argument("-u", "--TARGET_USERNAME", help="Firewall Username", type=str)
    parser.add_argument("-p", "--TARGET_PASSWORD", help="Firewall Password", type=str)
    args = parser.parse_args()

    if len(sys.argv) < 2:
        parser.print_help()
        parser.exit()
        exit(1)

    fw_ip = args.TARGET_IP
    username = args.TARGET_USERNAME
    password = args.TARGET_PASSWORD

    # create fw object using pan-python class
    fw = pan.xapi.PanXapi(api_username=username, api_password=password, hostname=fw_ip)

    # get firewall api key
    api_key = fw.keygen()

    # !!! updates require mgmt interface with internet access
    # update to latest content and av versions
    for item in ['content', 'anti-virus']:
        update_content(fw, item)

    print('\ncontent update complete')


if __name__ == '__main__':
    main()