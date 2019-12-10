import pytest

from pydodo import bluebird_config
from pydodo.bluebird_connect import get_bluebird_url, construct_endpoint_url

def test_bluebird_config():

    host = 'test_host'
    port = 2001
    version = 'v25'

    resp = bluebird_config(host=host, port=port, version=version)
    assert resp == True

    url = get_bluebird_url()
    assert url == "http://{}:{}".format(host,port)

    endpoint="POS"
    endpoint_url = construct_endpoint_url(endpoint)
    assert endpoint_url == "{0}/api/{1}/{2}".format(url,version,endpoint)
