from tabulate import tabulate
class Instance(object):
    """
    [{u'agent': True,
      u'cpu': 0.011960000000000002,
      u'id': u'i-0037f3ac0439a1a45',
      u'memory': 0.2556165751372941,
      u'private-ip': u'10.0.1.138',
      u'processes': 2,
      u'public-ip': u'54.205.209.79',
      u'started': u'2016-12-21T17:27:11Z',
      u'status': u'active'},
    """

    def __init__(self, as_json):
        if as_json == 'error':
            return
        for k in as_json:
            try:
                setattr(self, k.replace('-', '_'), as_json[k])
            except TypeError:
                from IPython import embed; embed()
        
        """
        self.agent = agent
        self.cpu = cpu
        self.id = id
        self.memory = memory
        self.private_ip = private_ip
        self.processes = processes
        self.public_ip = public_ip
        self.started = started
        self.status = status
        """


class Racks(object):
    def init(self, as_json):
        self.racks = []
        self.as_json = as_json
        for r in as_json:
            self.racks.append(Rack(r))

        self.headers = [
            "name",
            "status",
            "host",
            "id",
            "organization_id",
            "version",
        ]
        self.low = 0
        self.current = self.racks[0]
        self.i = 0

    def __iter__(self):
        return self

    def next(self):
        self.i += 1
        if self.i > len(self.racks):
            raise StopIteration
        else:
            self.current = self.racks[self.i - 1]
            return self.current

    def __repr__(self):
        """Print a list of Racks."""
        return tabulate([r.as_list() for r in self.racks], self.headers)

    def tabulate(self):
        """Print a list of Racks as a table."""
        return tabulate([r.as_list() for r in self.racks], self.headers)


class Organization(object):
    def __init__(self, as_json):
        for k in as_json:
            setattr(self, k.replace('-', '_'), as_json[k])
        self.headers = [
            "DeveloperIds",
            "id",
            "name",
        ]


class Rack(object):
    """
     {u'host': u'staging-1328120697.us-east-1.elb.amazonaws.com',
      u'id': u'8f90d422-f310-464f-a132-9721a3d050f2',
      u'name': u'staging',
      u'organization': {u'DeveloperIds': [u'175e78e9-5d09-4313-bcc7-b991469af4a8',
        u'8940c637-0aeb-4b11-9252-c6685fb96c65',
        u'c0c1322c-ec7f-4034-8579-2946b29c0f0b',
        u'89b5c1e3-94f5-4ef1-8fe7-a0f99f6ff7dd',
        u'8d67ef0d-9bbb-44cf-85d5-a3acc310bb77',
        u'c873c4b9-26db-440a-8fdc-35159ccfdf8f'],
       u'id': u'1baa4966-94ab-450a-acfd-3e897a0d25fa',
       u'name': u'vhx'},
      u'organization-id': u'1baa4966-94ab-450a-acfd-3e897a0d25fa',
      u'status': u'running',
      u'version': u''}]
    """
    def __init__(self, as_json):
        for k in as_json:
            setattr(self, k.replace('-', '_'), as_json[k])
        self.headers = [
            "name",
            "status",
            "host",
            "id",
            "organization_id",
            "version",
        ]
        
    def __repr__(self):
        return ", ".join([x for x in self.as_list()]) + "\n"

    def as_list(self, keys=[]):
        keys = keys or self.headers

        return [getattr(self, key) for key in keys]
