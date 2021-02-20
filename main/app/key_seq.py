class keys:
      
    __consumer_key = 'jiQSijiPfwiBNeeQn9WjzY51k'
    __consumer_secret = 'XAboYUQIS2UsqBMXzBFj5sUHEb0xokK1IT5oMf9D5kZsNd75NS'
    __access_token = '264723466-aEptlEg2eG1ahmg4BJYDDWgUFNVM8WM8z8tgPRGX'
    __access_token_secret = 'iPzBj4PwsyniINYgF3an8QfBFBMdykAGhlGnHVur4fm20'

    '''
        トークンを返すセッター
        以下の順で返します
        consumer_key, consumer_secret, access_token, access_token_secret
    '''
    def get_tokens(self):
        return self.__consumer_key, self.__consumer_secret, self.__access_token, self.__access_token_secret