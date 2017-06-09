import argparse, requests, random, os

# maximum random values per request
MAX_REQ = int(1e4)

def request(endpoint, **parameters):
    params = '&'.join([
        '%s=%s' % (key, val)
        for key, val in parameters.items()
    ])
    r = requests.get(
        'https://www.random.org/%s/?%s' % (endpoint, params),
        headers={
            'User-Agent': 'ung.m888@gmail.com',
        },
        timeout=100
    )
    if r.status_code != 200:
        raise Exception('Request returned a %d status code' % r.status_code)
    return r.content

class Generator(object):
    def __init__(self, debug=False):
        parser = self._parser()
        self.args = parser.parse_args()
        
    def _parser(self):
        parser = argparse.ArgumentParser()
        return parser
        
    def _random_ints(self, min, max, num=1):
        if num <= MAX_REQ:
            response = request(
                'integers',
                num=num,
                min=min,
                max=max,
                col=1,
                base=10,
                format='plain',
                rnd='new',
            )
            return [int(x) for x in response.splitlines()]
        else:
            vals = []
            while num > MAX_REQ:
                vals.extend(self._random_ints(min, max, MAX_REQ))
                num -= MAX_REQ
            vals.extend(self._random_ints(min, max, num))
            return vals    