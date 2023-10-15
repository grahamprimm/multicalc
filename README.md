# Multi-Function Calculator

A simple desktop calculator application developed with Python and Tkinter. This application provides three calculators for temperature conversion, compound interest calculation, and finding the slope of a line.

## Features

- Temperature Calculator: Convert temperatures between Celsius and Fahrenheit.
- Compound Interest Calculator: Calculate the future value of an investment.
- Slope Calculator: Determine the slope of a line given two points.

## Requirements

- Python 3.12
- Tkinter 0.1.0

Install the required package using pip:

```bash
pip install -r requirements.txt
```

## Usage

Navigate to the `src` directory and run `main.py` to launch the application:

```bash
cd src
python main.py
```

## Directory Structure

```plaintext
project_root/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── calculators/
│   │   ├── temperature.py
│   │   ├── compound_interest_.py
│   │   └── slope.py
    └── test_calculators.py
```

## Testing

### Testing on your local machine

Run `test_calculators.py` to execute the tests:

```bash
cd src
python test_calculators.py
```

### Running Tests with Docker

To ensure the consistency and reliability of the MultiCalc Application, a Docker container has been set up for running the tests. The `test.Dockerfile` located at the root of the project is used to create a Docker image for testing purposes.

Here's how you can build and run the test container:

1. **Building the Docker Image:**
    In the project root directory, execute the following command to build the Docker image for testing:

    ```bash
    docker build -t multicalc-tests -f test.Dockerfile .
    ```

    This command builds a Docker image named `multicalc-test` using the `test.Dockerfile` in the current directory.

2. **Running the Tests:**
    Once the Docker image is built, you can run the tests by executing the following command:

    ```bash
    docker run multicalc-tests
    ```

    This command runs a container from the `multicalc-test` image, and executes the tests specified in `src/test_calculators.py`.

The `test.Dockerfile` is configured to:

- Use the official Python 3.12 slim-buster image as a base image.
- Set the working directory in the container to `/app`.
- Copy the project source code and `requirements.txt` into the container.
- Install the necessary dependencies from `requirements.txt`.
- Run `src/test_calculators.py` to execute the tests when the container is launched.

By utilizing Docker, we ensure that the tests are executed in a clean, controlled environment, minimizing the chances of inconsistencies due to differing local development environments.

## License

This project is open source and available under the [BSD 2-Clause License](LICENSE).
