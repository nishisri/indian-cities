# indiancities

## Technologies Used:

* Language - Python
* Test framework - Pytest
* Build tool - Pyenv

## How to start the application:
To run the test simply run the command -   **python indian-cities-test.py**
This application assumes that Python3 already installed in the system also it assumes that Pytest and requests are also installed.


##Summary: 
I have selected API service "Indian cities" and created automation test as mentioned below:
Created test cases around Partial Search,Specific search and multiple search functionality as mentioned below using python+pytest:-
* test_for_endpoint_specific_city_inParams
* test_For_Endpoint_Specific_District
* test_For_Endpoint_Specific_State
* test_For_Endpoint_search_State_like
* test_For_Endpoint_multiple_parameters_with_status_code

##Additional Point:
Dockerize test : Assumes that Docker is already installed in the system.
Docker File is provided to configure the docker image 
Run the commands :
docker build -t indiancities:test -f ./DockerFile ./

To run the test use below command:
docker run indiancities:test

# Areas of Improvement
* Test names can be created more meaningful.
*  As I am a beginner in Python created simple Pytest.
* Automated few scenarios only not covered all scenarios mentioned in the excel sheet test cases.
* Can cover more scenarios in API testing as well like negative paths,few more combinations etc.