from django.conf import settings

def get_request_values(request):

    req = request

    client_header = dict(req.headers)
    client_body = dict(req.data)
    client_files = dict(req.FILES)
    client_method = str(req.method)
    client_path = str(req.path)
    client_query = req.query_params

    query = '&'.join("{!s}={!r}".format(key,val) for (key,val) in client_query.items()).replace("'","")
    if query:
        query = "?" + query

    target_destination = settings.SERVICE_CONTEXT_HOST + client_path + query

    return {"client_header": client_header,
            "client_body": client_body,
            "client_files": client_files,
            "client_method": client_method,
            "client_path": client_path,
            "client_query": client_query,
            "target_destination": target_destination}