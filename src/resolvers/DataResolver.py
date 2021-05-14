from flask import json
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from pathlib import Path
import datetime


dataSet = Path('src/datasets/')
datafile = dataSet / 'data.json'

def getFromZed():
    """ fetch from zed API """

    # Select your transport with a defined url endpoint
    transport = RequestsHTTPTransport(url="https://zed-ql.zed.run/graphql")

    # Create a GraphQL client using the defined transport
    client = Client(transport=transport, fetch_schema_from_transport=True)
    
    date_from = datetime.datetime(year=2018, month=12, day=1, hour=00, minute=00, second=00)
    date_to = datetime.datetime(year=2021, month=12, day=31, hour=23, minute=59, second=00)
    
    start = date_from.strftime('%Y-%m-%dT%H:%M:%S.%f%SZ')
    end = date_to.strftime('%Y-%m-%dT%H:%M:%S.%f%SZ')

    variables = {
        "first": 2,
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
    
    return result


def readZedDataFromFile():
    """ read json file to browser """
    
    with open(datafile, "r") as read_file:
        data = json.load(read_file)
    
    return data

    