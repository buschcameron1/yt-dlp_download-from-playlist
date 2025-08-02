import requests, json, yt_dlp

def getVideos(playlistId, apiKey):
    playlistItems = requests.get(f'https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults=10&playlistId={playlistId}&key={apiKey}')
    return playlistItems.json()['items']

def downloadVideos(urls, storageLocation):
    opts = {
        'outtmpl': storageLocation
    }
    yt_dlp.YoutubeDL(opts).download(urls)

# This requires oAuth2 implementation, my brain isn't ready :(
#def cleanPlaylist(playlistId, ):


def main():
    with open('config.json', 'r') as file:
        config = json.load(file)

    # Get the video IDs from the playlist
    videos = getVideos(config['playlistId'], config['apiKey'])

    urls = []
    for video in videos:
        urls.append(f'https://www.youtube.com/watch?v={video['contentDetails']['videoId']}')

    # Download the videos
    downloadVideos(urls, config['storagePath'])

    #confirmExistAndClean()

if __name__ == "__main__":
    main()