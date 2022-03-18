#! /usr/bin/env python

import fire

from plexapi.server import PlexServer
from plexapi.library import LibrarySection

def run():
    fire.Fire(plexrefresh)

def plexrefresh(base_url:str, token:str):
    """
    Tell a Plex Media Server instance to refresh library metadata.

    Args:
        base_url (str): The URL used to access plex media server
        token (str): The Plex Token. This can be obtained from viewing the XML
            Metadata of an arbitrary file and copying the `token` URL 
            parameter from the browsers URL bar.

    """
    server = PlexServer(
        baseurl=base_url,
        token=token
    )
    server.library.update()
    server.library.refresh()