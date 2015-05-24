from hashlib import sha224
from requests import request

class SiteComparator:
    def get_hash(self, url):
        html = request('GET', url, timeout=30)
        return str(sha224(html.text.encode('UTF-8')).hexdigest())

    def url_and_hash(self, url, hash):
        return hash == self.get_hash(url)

    def urls(self, url1, url2):
        return self.get_hash(url1) == self.get_hash(url2)

    def is_hashable(self, url):
        try:
            hash_at_instant_one = self.get_hash(url)
            hash_at_instant_two = self.get_hash(url)

            return hash_at_instant_one == hash_at_instant_two
        except:
            return False

