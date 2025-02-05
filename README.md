## Examples of what CompassLabs needs to integrate a protocol into the Compass API

[Compass API](https://api.compasslabs.ai)

This repository shows what CompassLabs would need to integrate a new protocol.

For each endpoint you must provide:

- User friendly request models
- User friendly response models
- Code for handling the request

## We need

- Endpoints for performing actions on the protocol
  - Our API will return an unsigned transaction
- Endpoints for fetching information from the chain.
  - The user must be able to make informed decisions about what they will do on your protocol by calling these endpoints.
  - There must be no requirement on understanding of encoding formats
    - you _must not_ return values that require decoding using further solidity calls
    - Ray format, x96 format, scaled values etc.

## Nice to have

- Example uses of each endpoint = useful
- Tests = even better

### Using the Repository

```
poetry install
```
