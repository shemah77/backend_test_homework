import hashlib


class MarsURLEncoder:


    def __init__(self):
        self.dict = {}
        self.hash_md5 = hashlib.new('md5')


    def encode(self, long_url):
        """Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol."""
        long_url = long_url.encode('utf-8')
        # print (long_url)
        self.hash_md5.update(long_url)
        hash_long_url = self.hash_md5.hexdigest()
        # print (self.hash_md5.hexdigest())
        if hash_long_url not in self.dict:
            self.dict.update({self.hash_md5.hexdigest():long_url})
            short_url = self.hash_md5.hexdigest()

        return  f'https://ma.rs/{short_url}'
    def decode(self, short_url):
        """Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную."""
        short_url_key = short_url[14:]
        long_link  = self.dict.get(short_url_key).decode('utf-8')

        # print (long_link)
        return f'{str(long_link)}'



a = MarsURLEncoder()
a.encode("https://tsup.ru/mars/marsohod-1/01-09-2023/daily_job.html")
a.encode("https://tsup.ru/mars/marsohod-2/01-09-2024")
print (a.encode("https://tsup.ru/mars/marsohod-1/01-09"))


a.decode('https://ma.rs/59cd412b29e9edc0ee9631a2b337cac0')


b = '59cd412b29e9edc0ee9631a2b337cac0'
if b in a.dict:
    print(f'извелекаем по ключу {a.dict[b].decode("utf8")}')

for i in a.dict.items():
     print (i)




