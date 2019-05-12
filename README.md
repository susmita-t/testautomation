help available in https://stackoverflow.com/questions/32203610/how-to-integrate-uml-diagrams-into-gitlab-or-github
# Test Automation

## Discussion
* What to Test
* Tools
* Programming Languate
* POM Object Model

## What to Test
![alt text](https://raw.githubusercontent.com/amitsaran/plantuml/master/what_to_test.png)

## Tools
* Selenium for Functionality Testing
* JMeter for Load and Stress Testing

## Programming Language
* Java
  * TestNG
  * Built in functionalities like PageFactory to initialize the locators
  * Maven project
    * ![maven folder structure](http://www.plantuml.com/plantuml/png/1S7H4G8n20N0LhI1y6ypDyYX5mT81XxQlhlt6M9zQgVTBc3NWoZvDzuJLp-xD6K5D31aER5F52S7RUD0kv5pGPC-_ENZjUpKF0hPWauTkzt-)
* Python
  * Allows for compact test suites
  * Very pretty and useful failure information
  * Test parametrization
  * Minimal boilerplate
  * Extensible (plugins are available) 
  * Fixtures are simple and easy to use 
  * We can use pyBuilder to have a setup like Maven. I have not explored it yet though. Any idea if we can incude pom.xml file in Python project?
  * Python Folder Structure
    * ![python folder structure](http://www.plantuml.com/plantuml/png/5SqnZW8n34RXVa-nN23kgUOc8vCO4ibn8lkt4BU7gLxtlYF0ZfpwTnjMDPkawty7Tjo9dD_bDT3paI5Ubq4CfQv9F0U2dOssibq3cXmGf_r1NtO-bpRnC-1PaIvbNyWXrdxz0W00)

## POM Object Model
 ![Class Diagram](http://www.plantuml.com/plantuml/png/1S7H3G9120JGLhG0bt-RCRX7xaYMvS8CiNtVU_gUgm_hMe-BlF4MAVsDqtdrjs4rSzCsnymGDCAfBmeDr6Q6qdDBA6WbSodmELpFqXXtn_e3)
