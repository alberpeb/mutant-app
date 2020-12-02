# Mutant Detector API REST

1. [ Setup. ](#setup)
2. [ AWS CLI and IAM. ](#aws)
3. [ Usage tips. ](#usage)
4. [ Live Demo. ](#demo)


**If you are a mutant, join Magneto**

With this app you can check if a DNA sample contains a mutant pattern or not by sending a POST request to the API Gateway

<a name="setup"></a>
## Setup

First execute the following commands after downloading and positioning in the project folder:
```
$ npm install
$ virtualenv venv -p python3
$ . venv/bin/activate
$ pip install -r requirements.txt
$ pip install flask
```

<a name="aws"></a>
## AWS CLI and IAM
In Amazon Management Console, search "IAM" and go to Users > Create New User. And associate existing policies

```
"AdministratorAccess"
"AWSLambda_FullAccess"
```
### Config credentials
Create a new key with the access key ID
Using the command `sls cli`, add your new credential
```
sls config credentials --provider aws --key <your_key_here> --secret <your_secret_here>
```


## Usage

**Deploy**

This example is made to work with the Serverless Framework dashboard which includes advanced features like CI/CD, monitoring, metrics, etc.

```
$ serverless login
$ serverless deploy
```

To deploy without the dashboard you will need to remove `org` and `app` fields from the `serverless.yml`, and you won’t have to run `sls login` before deploying.

**Run the application locally.**

```
sls wsgi serve
```
Check for the dependencies and install Werkzeug (and add it to the requirements.txt file) if its needed:
```
pip install Werkzeug
pip freeze > requirements.txt
```

<a name="aws"></a>
## Live demo
[Here is the live version of this project](https://aqnjpxjnzk.execute-api.us-east-1.amazonaws.com/prod/)

Try it out with Postman:
**POST**
Make a Post request with the following url
```
https://aqnjpxjnzk.execute-api.us-east-1.amazonaws.com/prod/mutant
```
Insert the following json for in the body segment and try it out
```
{
  "dna":["ATGCGA","CAGTGC","TTATGT","AGAAGG","CTCCTA","TCACTG"]
}
```

The response must be
```
{
    "body": "Ok",
    "statusCode": 200
}
```

If a DNA with less than two patterns is sended, the response would be
```
{
    "body": "Foribiden",
    "statusCode": 403
}
```