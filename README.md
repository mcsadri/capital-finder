# capital-finder

An introduction to Serverless Functions using REST APIs

## Feature Tasks and Requirements

- [X] Use [requests](https://requests.readthedocs.io/en/latest/) library to interact with [REST Countries API](https://restcountries.com/#rest-countries)
- [X] Create a serverless function following Vercel’s get-started directions that handles two kinds of queries:
  - [X] The serverless function should handle a `GET` http request with a given country name that responds with a string with the form `The capital of X is Y`
    - [X] E.g.`/capital-finder?country=Chile` should generate an http response of `The capital of Chile is Santiago.`
    - [X] The serverless function should handle a `GET` http request with a given capital that responds with a string with the form `The capital of X is Y`
      - [X] E.g.`/capital-finder?capital=Santiago` should generate an http response of `Santiago is the capital of Chile.`
- [X] Deploy app via [Vercel](https://vercel.com/docs/get-started)

## User Acceptance Tests

- [X] Project README.md should include working example urls for deployed function.
  - [X] Search with the name of a country to return its capital city:
    - [https://capital-finder-mcsadri.vercel.app/api/capital?name=belgium](https://capital-finder-mcsadri.vercel.app/api/capital?name=belgium)
  - [X] Search with the name of a capital city to return its country name
    - [https://capital-finder-mcsadri.vercel.app/api/capital?name=berlin](https://capital-finder-mcsadri.vercel.app/api/capital?name=berlin)
  - [X] Search with an invalid country or capital city name
    - [https://capital-finder-mcsadri.vercel.app/api/capital?name=qwerty](https://capital-finder-mcsadri.vercel.app/api/capital?name=qwerty)
  - [X] Search with an emptry query string
    - [https://capital-finder-mcsadri.vercel.app/api/capital?name=](https://capital-finder-mcsadri.vercel.app/api/capital?name=)
  - [X] Search with name in all UPPER to show case conversion to Title
    - [https://capital-finder-mcsadri.vercel.app/api/capital?name=TOKYO](https://capital-finder-mcsadri.vercel.app/api/capital?name=TOKYO)
