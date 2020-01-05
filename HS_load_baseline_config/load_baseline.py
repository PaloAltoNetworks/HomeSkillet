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
Palo Alto Networks load_baseline.py

use the firewall api to import, load, and commit a baseline config

This software is provided without support, warranty, or guarantee.
Use at your own risk.
'''

import argparse
import sys
import time
import requests
from jinja2 import Environment, FileSystemLoader
from passlib.hash import md5_crypt
import pan.xapi

# define functions for custom jinja filters
def md5_hash(txt):
    '''
    Returns the MD5 Hashed secret for use as a password hash in the PanOS configuration
    :param txt: text to be hashed
    :return: password hash of the string with salt and configuration information. Suitable to place in the phash field
    in the configurations
    '''
    return md5_crypt.hash(txt)

def template_render(filename, context):
    '''
    render the jinja template using the context value from config_variables.yaml
    :param filename: name of the template file
    :param template_path: path for the template file
    :param render_type: type if full or set commands; aligns with folder name
    :param context: dict of variables to render
    :return: return the rendered xml file and set conf file
    '''

    print('creating template for {0}'.format(filename))

    env = Environment(loader=FileSystemLoader('./'))

    # load our custom jinja filters here, see the function defs below for reference
    env.filters['md5_hash'] = md5_hash

    template = env.get_template(filename)
    rendered_template = template.render(context)

    return rendered_template

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

def import_conf(ip_addr, api_key, import_file):
    '''
    import local config file to device
    :param ip_addr: ip address of configured device
    :param api_key: api key for the device
    :param filename: filename to import
    :return:
    '''

    print('importing configuration to device')

    url = "https://{0}/api".format(ip_addr)
    params = {
        "type": "import",
        "category": "configuration",
        "key": api_key
    }

    files = {'file': ('baseline_config.xml', import_file)}
    r = requests.post(url,
                      params=params,
                      verify=False,
                      files=files)

    print(r.text)

    return r

def load_conf(device, filename):
    '''
    load file in device as candidate config
    :param device: configuration device object (fw or panorama)
    :param filename: name of configuration file imported to the device
    :return:
    '''

    print('loading {0} as candidate config'.format(filename))
    device.op(cmd='<load><config><from>{0}</from></config></load>'.format(filename))
    results = device.xml_result()
    print(results)

    return(results)

def commit(device):
    '''
    commit to device after config is complete
    :param device: device object being configured
    :return:
    '''

    # commit changes to the device to look for errors
    cmd = '<commit></commit>'
    print('commit config')
    device.commit(cmd=cmd)
    results = device.xml_result()

    if '<job>' in results:
        check_job_status(device, results)


def main():
    '''
    simple set of api calls to load a baseline clean config to LiaB
    '''

    # python skillets currently use CLI arguments to get input from the operator / user. Each argparse argument long
    # name must match a variable in the .meta-cnc file directly
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--TARGET_IP", help="IP address of the firewall", type=str)
    parser.add_argument("-u", "--TARGET_USERNAME", help="Firewall Username", type=str)
    parser.add_argument("-p", "--TARGET_PASSWORD", help="Firewall Password", type=str)
    parser.add_argument("-n", "--FW_NAME", help="Firewall hostname", type=str)
    parser.add_argument("-d1", "--DNS_1", help="primary dns server", type=str)
    parser.add_argument("-d2", "--DNS_2", help="secondary dns server", type=str)


    args = parser.parse_args()

    if len(sys.argv) < 2:
        parser.print_help()
        parser.exit()
        exit(1)

    fw_ip = args.TARGET_IP
    username = args.TARGET_USERNAME
    password = args.TARGET_PASSWORD
    hostname = args.FW_NAME
    #DNS_1 = args.DNS_1
    #DNS_2 = args.DNS_1
    filename = 'baseline_config.xml'

    # create fw object using pan-python class
    fw = pan.xapi.PanXapi(api_username=username, api_password=password, hostname=fw_ip)

    # get firewall api key
    api_key = fw.keygen()

    # render file with variables
    clean_config = template_render(filename, vars(args))

    # import config
    good_import = import_conf(fw_ip, api_key, clean_config)

    if 'success' not in good_import.text:
        print('error importing configuration')
        exit(1)

    # load config
    good_load = load_conf(fw, filename)

    if 'loaded' not in good_load:
        print('error loading configuration')
        exit(1)

    # commit config
    commit(fw)

    print('baseline load complete')


if __name__ == '__main__':
    main()