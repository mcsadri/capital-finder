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

        # localhost testing URLs
        # http://localhost:8000/api/capital?name=spain

        # do the stuff
        print("capital-finder")
        country_api_url = f"https://restcountries.com/v3.1/name/{dictionary.get('name')}"
        print("the country name search api url is:", country_api_url)
        country_response = requests.get(country_api_url)
        country_data = country_response.json()
        # print("the country response is:", country_data)
        # country_capital = country_data[0]["capital"][0]
        # print("the capital is:", country_capital)


        # capital_api_url = f"https://restcountries.com/v3.1/capital/{dictionary.get('name')}"




        # form the response
        # set the message content
        message = "doodah"
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
