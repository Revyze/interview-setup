# interview

This is the initial state of the repository for the live coding session.
Its goal is to mimick the core components of our production codebase.

If you prefer to use your own environment, please set up this repository and ensure "Hello World" is properly displayed.

This app sends "Hello World" through a graphql python server to a react-native frontend.

Note: you don't need to setup a mobile emulator, a web navigator works fine for the interview.


## Running the app

### pre-requisite

* Node & npm
* Python & uv

### front
```
cd front
npm i
npm run web # or npm run ios
```

### back

```
cd back
uv venv
source .venv/bin/activate
uv pip install flask ariadne flask-cors
python app.py
```

You can check http://127.0.0.1:5000/graphql to ensure the server is running
