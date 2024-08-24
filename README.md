# Interview set-up

This is the initial state of the repository for the live coding session.
Its goal is to mimick some of the core components of our production codebase.

If you prefer to use your own environment, please set up this repository and ensure "Hello World" is properly displayed.

This app sends "Hello World" through a graphql python server to a react-native frontend.

**Note:** you don't need to setup a mobile emulator, a web navigator should work fine for the interview.

## Running the app

### Frontend

#### Prerequisites

- Node (v16+)
- npm

#### Running instructions

```sh
cd front
npm i
npm run web # or npm run ios
```

### Backend

#### Prerequisites

- python >= 3.9
- [uv](https://github.com/astral-sh/uv) >= 0.3.0 (if you don't have python installed, you might want to install python through uv, following the steps here).

#### Running instructions

```sh
cd back
uv sync
source .venv/bin/activate
python app.py
```

You can check http://127.0.0.1:5000/graphql to ensure the server is running and http://localhost:8081/ should display "Hello World".

## The technical test

When the technical test starts you will be given access to the test repository.

```sh
git remote add test TEST_REPO_URL # replace with provided url
git fetch --all
git merge test/main
```
