#!/usr/bin/env python


""" View Convox resources """

import os
import click
import base64
import logging

from rc.rc import RestAPI
from classes import Racks, Instances

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='./convox.log',
                    filemode='w')

CONTEXT_SETTINGS = dict(
    help_option_names=['-h', '--help'],
    token_normalize_func=lambda x: x.lower()
    )


class ConvoxAPI(RestAPI):
    def __init__(self, url, api_key):
        self.url = url

        self.check_token()
        self.key = api_key

        auth_header = base64.b64encode("{}:{}".format("convox", self.key))
        self.headers = {
            "Authorization": 'Basic {}'.format(auth_header),
            'Accept': 'application/json',
            }
        logging.debug(self.headers)

        RestAPI.__init__(self, url, self.headers)

    def log(self, msg, level=0):
        logging.info(msg)
        click.secho(msg, fg='blue', nl=False)
        if level > 4:
            exit(1)

    def check_token(self):
        if 'CONVOX_API_KEY' not in os.environ:
            dashboard_url = "https://console.convox.com/"
            click.secho("No CONVOX_API_KEY envvar found. ", fg='red')
            msg = ("Retrieve it from the Convox Console:\n")
            msg += click.style(dashboard_url, fg='blue') + "\n"
            msg += ("Once you have it, add it to your bash profile: \n"
                    "export CONVOX_API_KEY='changeme'")
            click.secho(msg)
            logging.fatal(msg)
            exit()

    def set_header(self, key, value):
        self.headers[key] = value

    @property
    def instances_as_json(self):
        return self.get("/instances")

    @property
    def racks_as_json(self):
        return self.get('/racks')


class Convox(ConvoxAPI):
    def __init__(self, apikey, url="https://console.convox.com"):
        ConvoxAPI.__init__(self, url, apikey)

    @property
    def instances(self):
        il = Instances()
        il.init(self.instances_as_json)
        return il

    @property
    def racks(self):
        rl = Racks()
        rl.init(self.racks_as_json)
        return rl


@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    pass


@cli.command()
def racks():
    print(user.racks)


@cli.command()
@click.argument('rack', required=False)
def instances(rack):
    """show the instances of a rack"""
    for rack in user.racks:
        user.set_header('rack', "legit")
        # self.headers['rack'] = rack
        print("-------------")
        print(rack.name)
        print(user.instances)

user = Convox(os.environ.get('CONVOX_API_KEY'))
user.check_token()

if __name__ == '__main__':
    cli(obj={})
