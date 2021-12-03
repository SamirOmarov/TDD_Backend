
<h1 align="center">
  <br>
  <a href="https://vast-ridge-58692.herokuapp.com/docs"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI" width="500"></a>
  <br>
  <p> Access the App by clicking the image above</p>
  <br>
  TDD FastAPI Todo RESTAPI
  <br>
</h1>

<h4 align="center">A minimal Todo App built on top of <a href="https://fastapi.tiangolo.com/" target="_blank">FastAPI</a>.

</h4>


  

![Continuous Integration and Delivery](https://github.com/SamirOmarov/TDD_Backend/workflows/Continuous%20Integration%20and%20Delivery/badge.svg?branch=main)


<p align="center">
  <a href="#architectural-decisions">Architectural Decisions</a> •
  <a href="#how-to-use">How To Use</a> •
</p>

![screenshot](https://miro.medium.com/max/3840/1*LdQEEDzAhDhjpgsJbK4s2w.jpeg)

## Architectural Decisions

* Simple ReastAPI created with FastAPI, No database were used, only simple python list to store the todos
* Test Driven Development
  - When writing tests, the the [Given-When-Then](https://martinfowler.com/bliki/GivenWhenThen.html) framework was used to help make the process of writing tests easier and faster.
* Pydantic was used for Base Models
* Deployment configuration were written for Docker 
  - a production-grade WSGI server -Gunicorn
  - I also created and switched to a non-root user, which is [recommended by Heroku](https://devcenter.heroku.com/articles/container-registry-and-runtime#run-the-image-as-a-non-root-user)
* Deployed on Heroku with  Docker images
* Github Packages were used to store the docker containers.
* GitHub Actions were used to automate, customize, and execute software development workflows right in  GitHub repository for CI/CD. 
  - In the `build` job:
		1.  Check out the repository so the job has access to it
		2.  Log in to GitHub Packages
		3.  Pull the image if it exists
		4.  Build the image
		5.  Push the image up to GitHub Packages
		
  - In In the `deploy` stage:
	1.  Check out the repository so the job has access to it
	2.  Log in to GitHub Packages
	3.  Pull the image if it exists
	4.  Build and tag the new image
	5.  Log in to the [Heroku Container Registry](https://devcenter.heroku.com/articles/container-registry-and-runtime)
	6.  Push the image up to the registry
	7.  [Set](https://help.github.com/en/actions/reference/workflow-commands-for-github-actions#setting-an-environment-variable) the `HEROKU_REGISTRY_IMAGE` and `HEROKU_AUTH_TOKEN` environment variables with `set-env` so they can be accessed within the release file
	8.  Create a new release via the [Heroku API](https://devcenter.heroku.com/articles/container-registry-and-runtime#api) using the image ID within the _[release.sh](http://release.sh)_ script 

	

## How To Use

From your command line:

```bash
# Clone this repository
$ git clone https://github.com/SamirOmarov/TDD_Backend

# Go into the repository
$ cd TDD_Backend

Build the image:

`$ docker-compose build`

Once the build is done, fire up the container in [detached mode](https://docs.docker.com/engine/reference/run/#detached--d):

`$ docker-compose up -d` or `$ docker-compose up -d --build`

With the containers up and running, run the tests:

`$ docker-compose exec web python -m pytest`
```

For Deployment:
Build and tag the image:
```
`$ docker build -f project/Dockerfile.prod -t 
 $ docker.pkg.github.com/SamirOmarov/TDD_Backend/todo:latest ./project`
```
