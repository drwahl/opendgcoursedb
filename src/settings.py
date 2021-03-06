# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
MONGO_HOST = 'localhost'
MONGO_DBNAME = 'odgcdb'

schema = {
    'name': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 100,
        'unique': True,
        'required': True
    },
    'country': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 50,
    },
    'state': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 50,
    },
    'city': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 50
    },
    'street': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 200,
    },
    'longlat': {
        'type': 'list',
    },
    'contributor': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 100,
    },
    'holes': {
        'type': 'integer'
    },
    'par': {
        'type': 'integer'
    },
    'created': {
        'type': 'datetime'
    },
    'modified': {
        'type': 'datetime'
    },
    'discs_lost': {
        'type': 'integer'
    },
    'hole_type': {
        'type': 'string'
    },
    'notes': {
        'type': 'string'
    },
    'established': {
        'type': 'datetime'
    }
}

courses = {
    'item_title': 'name',
    'resource_methods': ['GET', 'POST'],
    'schema': schema
}
RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET', 'PATCH', 'PUT']
X_DOMAINS = '*'
X_HEADERS = ['Content-Type', 'If-Match']
DOMAIN = {'courses': courses}
