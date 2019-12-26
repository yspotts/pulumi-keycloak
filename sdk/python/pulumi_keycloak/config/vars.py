# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

__config__ = pulumi.Config('keycloak')

client_id = __config__.get('clientId')

client_secret = __config__.get('clientSecret')

client_timeout = __config__.get('clientTimeout')
"""
Timeout (in seconds) of the Keycloak client
"""

initial_login = __config__.get('initialLogin')
"""
Whether or not to login to Keycloak instance on provider initialization
"""

password = __config__.get('password')

realm = __config__.get('realm')

url = __config__.get('url')
"""
The base URL of the Keycloak instance, before `/auth`
"""

username = __config__.get('username')
