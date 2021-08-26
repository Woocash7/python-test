from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen

from celery import shared_task

from websites.models import Website

@shared_task
def retrieve_websites():
    temp = []
    url = 'http://s3.amazonaws.com/alexa-static/top-1m.csv.zip'
    resp = urlopen(url)
    zipfile = ZipFile(BytesIO(resp.read()))
    for contained_file in zipfile.namelist():
        for line in zipfile.open(contained_file).readlines():
            temp.append(line)

    for site in temp:
        rank, url = site.decode().strip().split(',')
        Website.objects.create(
            url=url,
            alexa_rank=rank
        )

    return True