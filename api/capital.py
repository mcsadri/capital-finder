from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # create a dictionary of parameters from the url string
        url = self.path
        url_components = parse.urlsplit(url)
        query_string_list = parse.parse_qsl(url_components.query)
        dictionary = dict(query_string_list)
        # print("dictionary: ", dictionary)

        # localhost testing URLs
        # http://localhost:8000/api/capital?name=spain

        # do the stuff
        country_capital = str()
        capital_country = str()
        if dictionary.get("name"):
            print("capital-finder")

            # given the name of a country get the name of the capital city
            country_api_url = f"https://restcountries.com/v3.1/name/{dictionary.get('name')}"
            # print("the country name search api url is:", country_api_url)
            country_response = requests.get(country_api_url)

            # if the name doesn't match a country
            if country_response.status_code == 404:
                country_capital = None
                # print("that country name was not found")

                # search if the name matches a country's capital city
                capital_api_url = f"https://restcountries.com/v3.1/capital/{dictionary.get('name')}"
                capital_response = requests.get(capital_api_url)

                # is the name doesn't match a capital
                if capital_response.status_code == 404:
                    capital_country = None
                    # print("that capital name was not found")
                else:
                    capital_data = capital_response.json()
                    # print("capital_data is:", capital_data)
                    capital_country = capital_data[0]["name"]["common"]
                    # print("the country is:", capital_country)
                    # print(f"{dictionary.get('name')} is the capital of {capital_country}")

            # if the query name matched a country name
            else:
                country_data = country_response.json()
                country_capital = country_data[0]["capital"][0]
                print("the capital is:", country_capital)

        # form the response
        # set the message content
        if country_capital is None and capital_country is None:
            message = f"The provided location, {dictionary.get('name')}, was not found."
        elif country_capital:
            message = f"The capital of {dictionary.get('name')} is {country_capital}."
        else:
            message = f"{dictionary.get('name')} is the capital of {capital_country}"

        # message = "doodah"

        # HTTP code
        self.send_response(200)
        # define the content type
        self.send_header('Content-type', 'text/plain')
        # add a blank line
        self.end_headers()
        # write the message
        self.wfile.write(message.encode())


if __name__ == '__main__':
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, handler)
    print(f'Starting httpd server on port: {server_address[0]}:{server_address[1]}')
    httpd.serve_forever()
