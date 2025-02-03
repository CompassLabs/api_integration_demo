## Examples of what CompassLabs needs to integrate a protocol into the Compass API

[Compass API](https://api.compasslabs.ai)

This repository shows what CompassLabs would need to integrate a new protocol.

For each endpoint you must provide:
- User friendly request models.
- User friendly response models.
- Code for handling the request.
Example uses of each endpoint would be useful. Tests would be even better.

To make an integration proceed quickly, we would need:
- Endpoints for performing actions on the protcol. For our API this means returning an unsigned transaction.
- Endpoints for fetching information from the chain. The user must be able to make informed decisions about what they will do on your protocol by calling these endpoints. There must not be a requirement to understand encoding formats (e.g. you _must not_ return values in Ray format, x96 format, scaled values which require decoding using further solidity calls, et cetera). 
