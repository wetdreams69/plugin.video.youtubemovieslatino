import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
import sys
from urllib.parse import parse_qsl

_URL = sys.argv[0]
_HANDLE = int(sys.argv[1])
_ADDON = xbmcaddon.Addon()

def get_channels():
    channels = _ADDON.getSetting('channel_ids').strip()
    return [c.strip() for c in channels.split(',') if c.strip()]

def list_channels():
    channels = get_channels()
    
    for channel_id in channels:
        youtube_url = f'plugin://plugin.video.youtube/channel/{channel_id}/'
        
        list_item = xbmcgui.ListItem(label=channel_id)
        list_item.setArt({'icon': 'DefaultFolder.png'})
        list_item.setInfo('video', {'title': channel_id})
        
        xbmcplugin.addDirectoryItem(
            handle=_HANDLE,
            url=youtube_url,
            listitem=list_item,
            isFolder=True
        )
    
    xbmcplugin.endOfDirectory(_HANDLE)

def router(paramstring):
    params = dict(parse_qsl(paramstring))
    
    if not params:
        list_channels()
    else:
        list_channels()

if __name__ == '__main__':
    router(sys.argv[2][1:])