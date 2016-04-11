# CF Sample App Python

A Python sample web application that can be deployed to Cloud Foundry

## Run locally

1. Run `pip install -r requirements.txt`
1. Run `python app.py`
1. Visit [http://localhost:3000](http://localhost:3000)

## Run in the cloud

1. Run `cf push my-python-app -m 128M -n my-random-hostname` (replacing my-random-hostname with something creative)
1. Visit the given URL
