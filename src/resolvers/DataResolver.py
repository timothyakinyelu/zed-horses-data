from flask import json, request, jsonify
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from pathlib import Path
from datetime import date, datetime


def getFromZed():
    """ fetch from zed API """

    date_from = request.args.get('start')
    date_to = request.args.get('end')
    numOfPages = int(request.args.get('pages'))

    dataSet = Path('src/datasets/')
    datafile = dataSet / 'dataFor{}To{}.json'.format(date_from, date_to)
    
    start_date = date.fromisoformat(date_from)     
    end_date = date.fromisoformat(date_to)

    start = start_date.strftime('%Y-%m-%dT%H:%M:%S.%f%SZ')
    end = end_date.strftime('%Y-%m-%dT%H:%M:%S.%f%SZ')


    # Select your transport with a defined url endpoint
    transport = RequestsHTTPTransport(url="https://zed-ql.zed.run/graphql")

    # Create a GraphQL client using the defined transport
    client = Client(transport=transport, fetch_schema_from_transport=True)

    variables = {
        "first": numOfPages,
        "input": {
            "dates": {
               "from": "{}".format(start),
			    "to": "{}".format(end)
            }
        }
    }

    # Provide a GraphQL query
    query = gql(
        """
        query ($input: GetRaceResultsInput, $before: String, $after: String, $first: Int, $last: Int) {
            get_race_results(before: $before, after: $after, first: $first, last: $last, input: $input) {
                edges {
                    cursor
                    node {
                        country
                        city
                        name
                        length
                        start_time
                        fee
                        race_id
                        weather
                        status
                        class
                        prize_pool {
                            first
                            second
                            third
                        }
                        horses {
                            horse_id
                            finish_time
                            final_position
                            name
                            gate
                            owner_address
                            bloodline
                            gender
                            breed_type
                            gen
                            coat
                            hex_color
                            img_url
                            class
                            stable_name
                        }
                    }
                }
                page_info {
                    start_cursor
                    end_cursor
                    has_next_page
                    has_previous_page
                }
            }
        }
    """
    )

    # Execute the query on the transport
    result = client.execute(query, variable_values=variables)
    
    with open(datafile, 'w') as outfile:
        json.dump(result, outfile)
    
    res = {'message': "A new file {} has been created".format(datafile)}
    return jsonify(res)


def readZedDataFromFile():
    """ read json file to browser """

    date_from = request.args.get('start')
    date_to = request.args.get('end')

    dataSet = Path('src/datasets/')
    datafile = dataSet / 'dataFor{}To{}.json'.format(date_from, date_to)
    
    try:
        with open(datafile, "r") as read_file:
            data = json.load(read_file)

        res = {'message': data['get_race_results']}
        return jsonify(res)
    except Exception:
        res = {'message': 'No such file exists'}
        return jsonify(res)

    