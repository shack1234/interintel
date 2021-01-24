<br />
<p align="center">
  <a href="">
  </a>
  <h3 align="center">Interintel Login System</h3>
  <p align="center">
    Awesome login system built with  django!
    <br />
    <br />
    <a href="https://interintel.herokuapp.com/">View Demo</a>
  </p>
</p>
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li>
    <a href="#interview-questions">Interview Questions</a>
     <ul>
        <li>
        <a href="#section-a">Section A</a>
          <ul>
          <li><a href="#question-one">Question One</a></li>
          <li><a href="#question-two">Question Two</a></li>
          <li><a href="#question-three">Question Three</a></li>
        </ul>
        </li>
        <li><a href="#section-b">Section B</a></li>
      </ul>
    </li>
  </ol>
</details>
<!-- ABOUT THE PROJECT -->
## About The Project
Interintel Login system as the name itself its an application that allows users to login in to the sytem. A user first registers
in the system by filling the fields that are required . once completed filling a user submits the credential if the credentials are
true a user is able to login.

Upon login , a user is sent an email that notifies the user that he or she has successufully registered with the site. also a user is able to edit their profile e.g upload a picture of themselves, request for password reset or even  change their password.

### Built With

This system was built with the following technologies.
* [Bootstrap](https://getbootstrap.com)
* [Django](https://djangoproject.com)

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

You need to have the following softwares and install them using the commands below.
* python
  ```sh
  $ sudo apt-get update
  $ sudo apt-get install python3.6

  ```
### Installation

### How To Setup On Linux
1. Clone this project 'git clone https://github.com/shack1234/interintel.git'
2. Go to Project Directory `cd interintel`
3. Create a Virtual Environment `python3.6 -m venv virtual`
4. Activate Virtual Environment `source virtual/bin/activate`
5. Install Requirements Package `pip install -r requirements.txt`
6. Migrate Database `python manage.py migrate`
7. Create Super User `python manage.py createsuperuser`
8. Finally Run The Project `python manage.py runserver`

<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.
[product-screenshot]: images/sign.jpeg

_For more examples, please refer to the [Documentation](https://example.com)_


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.


<!-- CONTACT -->
## Contact

Name - [@shack1234](https://github.com/shack1234)  Email - shadrack.anayo@strathmore.edu

Project Link: [https://github.com/shack1234/interintel](https://github.com/shack1234/interintel)

## Interview Questions

### Section A
#### Question One
##### Types of Integration protocols
1. API 
(Application Programming Interface) is the most common tool for connecting different applications.It enables interaction between applications. An API uses a common code language to specify functionality and set protocols. This gives  applications the ability to transfer data.


* To use an API, you make a request to a remote web server, and retrieve the data you need. 
* APIs are useful in the following cases:
   ```
  You want a small piece of a much larger set of data. - it won't make any sense for one to download entire data while  you are going to use a piece of it.

  The data is changing quickly -An example of this is stock price data. It doesn’t really make sense to regenerate a dataset and download it every minute — this will take a lot of bandwidth, and be pretty slow.
   ```

* in general an API, is a server that you can use to retrieve and send data to using code

* Example in python how you can you APIS

  ```sh
  $ pip install requests
  ```
* Once you’ve installed the library, you’ll need to import it

  ```sh
  import requests
  ```
* There are many different types of requests. The most commonly used one, a GET request, is used to retrieve data.
* When we make a request, the response from the API comes with a response code which tells us whether our request was successful
* Response codes are important because they immediately tell us if something went wrong.
* To make a ‘GET’ request, we’ll use the requests.get() function, which requires one argument — the URL we want to make the  request to. 

  ```sh
  response = requests.get("http://api.open-notify.org/astros.json")
  print(response.status_code)
  ```
* if the  link is okay you will receive a status code of 200 , which means its okay. from there we use response.json() to get the date in the api 
  ```sh
  print(response.json())
  ```
* which will show this data that is available in the api
  ```sh
  {'message': 'success', 'people': [{'name': 'Alexey Ovchinin', 'craft': 'ISS'}, {'name': 'Nick Hague', 'craft': 'ISS'}, {'name': 'Christina Koch', 'craft': 'ISS'}, {'name': 'Alexander Skvortsov', 'craft': 'ISS'}, {'name': 'Luca Parmitano', 'craft': 'ISS'}, {'name': 'Andrew Morgan', 'craft': 'ISS'}], 'number': 6}
  ```

2. WEBHOOKS or HTTP Callbacks -
They are quite similar in that they are tools that link to a web application. But, they have two key differences. For webhooks, implementation is often not code-based. They often have modules that are programmable within a web application. Instead of being request-based, webhooks are event-based. They only trigger when specific events occur within a third-party service

 * In most web frameworks, there is the concept of a route. A route allows the application to respond with specific content or     data when the user visits a specific URL. 
 * The same idea applies to APIs. When you send a request to GitHub for details about a specific organization, such as https://api.github.com/repo/:..., the route is /repo/:... where :.. is the name of the organization.

* The same concept is applied when receiving webhooks. We establish a route, tell the service where to send the data, and our application sits and waits until a request comes in to that route.



#### Question Two
##### Data streaming application Question
* Push notification service architecture
In order to achieve all the requests -  we will use notification system as three components:
1. Notification server -exposes the API to send notifications, and pushes it as a job on our job queue
   * This is an HTTP server that exposes an API internally to send notifications.
   * In order to make things simple, the API accepts the user ID, and an optional application ID as HTTP headers, and notification information in the request body:
   * The server fetches all of the users devices from the token store, and schedules a job for each of the users devices.
   * The notification server abstracts the external interface to the system.

2. Token store — stores the devices and devices tokens of all the currently logged-in users
   * Once a user is logged into our application, the application makes a call to the token store API with their device token and application ID.
   * This entry is then removed when the user logs out.
     The token store abstracts the process of deciding which devices to send a notification to for each user
3. Notification worker — consumes jobs on the job queue and sends notifications via the notification providers
   * The worker processes consume messages from the job queues, and send out messages to the respective notification providers.
   * In order to make the code simpler, and to accommodate different service providers if needed, we will make use of interfaces to  abstract the functionality implemented by each provider:
   * The Push method takes a request object and returns a response object.
   * The response contains information on whether the notification was sent to the provider’s server successfully:
   * We will then implement the interface for specific providers.
   * The notification worker abstracts the process of selecting the correct provider to send the notification. It selects the correct provider, with the correct API key based on the application ID of the message received from the queue.

#### conclusion 
* IF  users will be allowed to stay signed in to multiple devices at a time, Multiple devices for a user will be  put behind the token service
* If the system isn’t comprised of just a single app, Multiple applications will be given a common interface on notification server
* If the system supports more than one operating systems/ providers ,Multiple providers will be  handled by individual job queues and notification workers
#### Question Three
##### Different encryption/hashing methods
 * built-in .hash() function in python provider.
  ```sh
  >>> hash("test")
  2314058222102390712
  ```
 * Secure Hashing
  ```sh
  >>> import hashlib
  >>> hashlib.md5(b"test1").hexdigest()
  '5a105e8b9d40e1329780d62ea2265d8a'
  >>> hashlib.md5(b"test2").hexdigest()
  'ad0234829205b9033196ba818f7a872b'
  ```
### Section B
#### Login and a Success Page
Having all the Prerequisites above, i started by creating a project  and named it intel
  ```sh
  $ django-admin startproject intel .
  ```
After succcessfully creating the project i created an application of it and named it login
  ```sh
  $ django-admin startapp login
  ```
I created a virtual environment and activated it
I went forword and installed all the requirements i needed for this project.The requirements  are available in requirements.txt
I created a database for the storage. named it intel 
  ```sh
  $ create database intel;
  ```
I also created a model for Profile that has the user , the user photo and bio.I migrated the database and saved the changes in the models and created a superuser
  ```sh
  $ python manage.py makemigrations login;
  $ python manage.py migrate login;

  ```
After i was done with the models i went forword and created forms that handles the signup and login ,also for the profile and edit profile. i saved them in a file called forms

After creating the forms i did style the template, using bootstrap and css, after finishing styling all the files that i needed . i went to the final stage, creating the functions that were to enable me to register a user and be able to login. I created different functions as they can be seen in the folder login  a file called views

I was able to add additional features like sending an email after registration, requesiting a password reset.
