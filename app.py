from services import SocialNetworkScraper

if __name__ == '__main__':
    service = SocialNetworkScraper()

    service.social_network_register()
    title = 'My homework post'
    content = 'My homework post content'
    service.social_network_add_post(title, content)
    service.logout()
    print('done')

