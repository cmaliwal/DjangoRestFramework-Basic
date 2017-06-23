# DjangoRestFramework-Basic
A web API, is exactly that, it's a set of defined requests and responses that allow us to communicate with a server, consume and edit the data it offers.  REST There are several approaches to API design, however, one architectural style that has become very popular, is REST, it stands for Representational State Transfer. The idea behind REST, is to use HTTP verbs to represent CRUD actions.  GET read  POST create  PUT update  DELETE delete  So, for example, if you're going to work with a resource users, you can use these HTTP verbs to request the server a specific CRUD action.  GET /users/1 Get user with id 1  POST /users/ Create a new user  PUT /users/1 Update user with id 1  DELETE /users/1 Delete user with id 1  Django REST Framework Django Rest framework is a toolkit, that allows for rapid API development, it comes with very handy features like Serializers, a browse-able API, Authentication and more.  On the other hand, Django Rest Framework integrates very well with Django and enhances it with several useful Classes and functions.  Overview of the Todo's API We're going to go over some of the aspects of building a simple API. For the following sections, we've put together a GitHub repository with a Todo's JSON API, we recommend you clone it in order to follow along with the article.  This API, has a basic Task model, and a serializer TaskSerializer which will take care of serializing the task so that we can return them as JSON data.
