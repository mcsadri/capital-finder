# capital-finder

An introduction to Serverless Functions using REST APIs

## Feature Tasks and Requirements

- [ ] Use [requests](https://requests.readthedocs.io/en/latest/) library to interact with [REST Countries API](https://restcountries.com/#rest-countries)
- [ ] Create a serverless function following Vercel’s get-started directions that handles two kinds of queries:
  - [ ] The serverless function should handle a `GET` http request with a given country name that responds with a string with the form `The capital of X is Y`
    - [ ] E.g.`/capital-finder?country=Chile` should generate an http response of `The capital of Chile is Santiago.`
    - [ ] The serverless function should handle a `GET` http request with a given capital that responds with a string with the form `The capital of X is Y`
      - [ ] E.g.`/capital-finder?capital=Santiago` should generate an http response of `Santiago is the capital of Chile.`
- [ ] Deploy app via [Vercel](https://vercel.com/docs/get-started)

## User Acceptance Tests

- [ ] Project README.md should include working example urls for deployed function.
  - [ ] doodah test 1
  - [ ] doodah test 2
  - [ ] doodah test 3
  - [ ] doodah test 4
  - [ ] doodah test 5
