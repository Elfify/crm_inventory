Base repo for inventory API

## Development
Due to multiple system dependencies,the recommended method for local development is using docker compose. 

### Docker Compose
This method will install all the required dependencies (ex: Rust, local postgres db) and open a bash terminal inside the application container for running tests.

1. Run `make compose-bash` to build the docker image, spin up the container, and execute a bash terminal from the application container.

2. Run specific tests or whole test suite with `pytest`
