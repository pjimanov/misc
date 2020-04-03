from google.cloud import bigquery

def sms_data(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    breath = None
    cough = None
    weakness = None
    appetite = None
    vomiting = None
    temp = None
    oxygen = None
    phone = None
    datetime = None
    channel = None
    dataset_table_id = '<[project_id.dataset_id.table_id]>'

    request_json = request.get_json(silent=True)
    if request_json and 'breath' in request_json:
        breath = request_json['breath']
    if request_json and 'cough' in request_json:
        cough = request_json['cough']
    if request_json and 'weakness' in request_json:
        weakness = request_json['weakness']
    if request_json and 'appetite' in request_json:
        appetite = request_json['appetite']
    if request_json and 'vomiting' in request_json:
        vomiting = request_json['vomiting']
    if request_json and 'temp' in request_json:
        temp = request_json['temp']
    if request_json and 'oxygen' in request_json:
        oxygen = request_json['oxygen']
    if request_json and 'phone' in request_json:
        phone = request_json['phone']
    if request_json and 'datetime' in request_json:
        datetime = request_json['datetime']
    if request_json and 'channel' in request_json:
        channel = request_json['channel']

    client = bigquery.Client()
    table = client.get_table(dataset_table_id)
    rows_to_insert = [(breath, cough, weakness, appetite, vomiting, temp, oxygen, phone, datetime, channel)]
    errors = client.insert_rows(table, rows_to_insert)

    #-----------------------------------debug-info----------------------------------------------------------
    #if errors == []:
    #  print("New rows have been added.")
    #print("Got table '{}.{}.{}'.".format(table.project, table.dataset_id, table.table_id))
    #print("Table schema: {}".format(table.schema))
    #print("Table description: {}".format(table.description))
    #print("Table has {} rows".format(table.num_rows))
    #errors = client.insert_rows(table, rows_to_insert)
    #return '{}'.format(errors)
    #schema: can be programmatically created
    #
    #breath:STRING,
    #cough:STRING,
    #weakness:STRING,
    #appetite:STRING,
    #vomiting:STRING,
    #temp:STRING,
    #oxygen:STRING,
    #phone:STRING,
    #datetime:STRING,
    #channel:STRING
    #
    #