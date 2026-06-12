# RESTful API

## Introduction

In the evolving world of software development, understanding how to communicate and transfer data efficiently between systems is essential. This project delves into the domain of RESTful APIs, a cornerstone in the realm of web services. The Representational State Transfer (REST) architecture is a set of constraints that ensure a scalable, stateless, and cacheable communication system. This approach allows for the easy integration of web services, making them accessible to a wide range of applications.

## Learning objectives

- HTTP/HTTPS Basics: Grasp the foundational principles of the web's primary protocol, understanding how data transfer occurs, methods involved, and the difference between the secure and non-secure versions.

- API Consumption with Command Line: Hands-on experience in interacting with APIs using basic command-line tools, laying the groundwork for more advanced interactions.

- API Consumption with Python: Elevate your data fetching skills by leveraging Python's capabilities, allowing for more advanced processing and data manipulation.

- API Development with http.server: Understand the basics of crafting an API from scratch using Python's built-in modules, setting a solid foundation.

- API Development with Flask: Dive deeper into API development using the lightweight Flask framework, focusing on routing, data management, and scalability.

- API Security & Authentication: Address the crucial aspect of security, understanding how to protect data transfer and ensure only authorized access to resources.

- API Standards & Documentation with OpenAPI: Conclude with the importance of maintaining standardized documentation, ensuring that APIs are usable, understandable, and maintainable.

## REST API Conceptual Diagram:
```text
+-------+           +-------+           +---------+           +---------+
|       |  Request  |       |  Process  |         |  Fetch/   |         |
|       |   ----->  |       |  -------> |         |  Modify   |         |
|       |           |       |           |         |  -------> |         |
|       | <-----    |       | <-------  |         |           |         |
|       |  Response |       |  Return   |         |           |         |
+-------+           +-------+           +---------+           +---------+
  Client            Web Server           API Server           Database
```
## Requirements

IMPORTANT: Your scripts will be tested with Python 3.9.