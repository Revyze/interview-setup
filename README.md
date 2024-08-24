# Interview set-up

This is the initial state of the repository for the live coding session.
Its goal is to mimick some of the core components of our production codebase.

If you prefer to use your own environment, please set up this repository and ensure "Hello World" is properly displayed.

This app sends "Hello World" through a graphql python server to a react-native frontend.

Note: you don't need to setup a mobile emulator, a web navigator works fine for the interview.

## Running the app

### Frontend

#### Prerequisites

- Node (installation can be a bit long)
- npm

#### Running instructions

```
cd front
npm i
npm run web # or npm run ios
```

### Backend

#### Prerequisites

- python >= 3.9
- [uv](https://github.com/astral-sh/uv) >= 0.3.0 (if you don't have python installed, you might want to install python through uv, following the steps here).

#### Running instructions

```
cd back
uv sync
source .venv/bin/activate
python app.py
```

You can check http://127.0.0.1:5000/graphql to ensure the server is running
