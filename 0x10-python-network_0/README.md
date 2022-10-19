
Resources

Read or watch:

    HTTP HyperText Transfer [Protocol](https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/HTTP_Basics.html)
    (except: “TRACE” Request Method, “CONNECT” Request Method, Language Negotiation and “Options MultiView” and Character Set Negotiation)
    [HTTP Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)

Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
General

    What a URL is
    What HTTP is
    How to read a URL
    The scheme for a HTTP URL
    What a domain name is
    What a sub-domain is
    How to define a port number in a URL
    What a query string is
    What an HTTP request is
    What an HTTP response is
    What HTTP headers are
    What the HTTP message body is
    What an HTTP request method is
    What an HTTP response status code is
    What an HTTP Cookie is
    How to make a request with cURL
    What happens when you type google.com in your browser (Application level)

Copyright - Plagiarism

    You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
    You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
    You are not allowed to publish any content of this project.
    Any form of plagiarism is strictly forbidden and will result in removal from the program.

Requirements
General

    Allowed editors: vi, vim, emacs
    - A README.md file, at the root of the folder of the project, is mandatory
    All your scripts will be tested on Ubuntu 20.04 LTS
    All your Bash scripts should be exactly 3 lines long (wc -l file should print 3)
    All your files should end with a new line
    All your files must be executable
    The first line of all your bash files should be exactly #!/bin/bash
    The second line of all your Bash scripts should be a comment explaining what is the script doing
    All curl commands must have the option -s (silent mode)
    All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
    The first line of all your Python files should be exactly #!/usr/bin/python3
    Your code should use the pycodestyle (version 2.8.*)
    All your modules should be documented: python3 -c 'print(__import__("my_module").__doc__)'
    All your classes should be documented: python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    All your functions (inside and outside a class) should be documented: python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Tasks :page_with_curl:

NOTE: The `curl` behavior in all Bash scripts were written to interact with a
server set up on a container provided by Holberton School.

* **0. cURL body size**
  [0-body_size.sh](./0-body_size.sh): Bash script that sends a `GET` request to
  a given URL and displays the size of the response body in bytes.

* **1. cURL to the end**
  * [1-body.sh](./1-body.sh): Bash script that sends a `GET` request to a given
  URL and displays the response body for a `200` status code response.

* **2. cURL Method**
  * [2-delete.sh](./2-delete.sh): Bash script that sends a `DELETE` request to
  a given URL and displays the response body.

* **3. cURL only methods**
  * [3-methods.sh](./3-methods.sh): Bash script that displays all HTTP methods
  the server of a given URL will accept.

* **4. cURL headers**
  * [4-header.sh](./4-header.sh): Bash script that sends a `GET` request to a
  given URL with a header variable `X-HolbertonSchool-User-Id=98` and displays
  the response body.

* **5. cURL POST parameters**
  * [5-post_params.sh](./5-post_params.sh): Bash script that sends a `POST`
  request to a given URL with the variables `email=hr@holbertonschool.com` and
  `subject=I will always be here for PLD` and displays the response body.

* **6. Find a peak**
  * [6-peak.py](./6-peak.py): [Technical interview preparation] - Python
  program that finds a peak in a list of unsorted integers.
  * [6-peak.txt](./6-peak.txt): Text file containing the complexity of the
  algorithm.

* **7. Only status code**
  * [100-status_code.sh](./100-status_code.sh): Bash script that sends a `GET`
  request to a given URL without using pipes, redirections, `;`, or `&&` and
  displays the status code of the response.

* **8. cURL a JSON file**
  * [101-post_json.sh](./101-post_json.sh): Bash script that sends a JSON `POST`
  request with the contents of a provided file to a given URL, and displays the
  response body.

* **9. Catch me if you can!**
  * [102-catch_me.sh](./102-catch_me.sh): Bash script that sends a request to
  `0.0.0.0:5000/catch_me` that causes the server to respond with a message
  containing `You got me!` in the repsonse body.
