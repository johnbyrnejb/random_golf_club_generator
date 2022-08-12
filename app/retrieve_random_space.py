import requests


def return_nasa_info():
    nasa_url = 'https://api.nasa.gov/planetary/apod?api_key=syR4COTCmjA4myhW6cQCiFwkOCVTWfH3dpDN2azK'

    nasa_results = requests.get(nasa_url)
    response_paragraph_intro = f'This image was taken by {nasa_results.json()["copyright"]} on the ' \
                               f'{nasa_results.json()["date"]}. What is it? Well...'

    response_paragraph = f'{nasa_results.json()["explanation"]}'

    nasa_image_url = nasa_results.json()["hdurl"]
    nasa_image_title = nasa_results.json()["title"]

    return response_paragraph_intro, response_paragraph, nasa_image_url, nasa_image_title

