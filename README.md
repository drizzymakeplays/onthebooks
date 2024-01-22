<div align="center">

# On the books
_My take on a barber booking application_

# On the books
_My take on a barber booking application_
</div>

[![Gitlab Release](https://img.shields.io/badge/version-1.0-green)](https://gitlab.com/Eksistenze/project-beta)


# Features
- Barber management including appointment, services, and client management with RESTful API.
- Client self service including searching, booking and canceling appointments with RESTful API.

# Requirements
[<img src="https://www.svgrepo.com/show/331370/docker.svg" alt="docker" width="100" height="100">](https://docs.docker.com/get-docker/) Docker
[<img src="https://www.svgrepo.com/show/452210/git.svg" alt="Git" width="100" height="100">](https://git-scm.com/) Git


# Project Installation
1. Fork repository and clone using git.
```bash
git clone https://gitlab.com/***YourNameHere***/onthebooks.git
```
2. Change to the directory that was just created
```bash
cd onthebooks
```
3. Create a .env file in the root directory(onthebooks)
```bash
mkdir .env
```
4. Add these environment variables to the .env file
```bash
SIGNING_KEY=enter a random string of charaters without spaces
PGADMIN_EMAIL=your.email@domain.com
PGADMIN_PASSWORD=yourpassword
```
5. Change to the ghi directory
```bash
cd ghi
```
6. Create a .env file in the ghi directory
```bash
mkdir .env
```
7. Add this environment variable to the ghi/.env file you just created to connect the backend to the frontend
```bash
VITE_API_HOST = ('http://localhost:5173')
```
8. Change back to the root directory
```bash
cd ..
```
9. Create both Docker volumes, build and run your docker container
```bash
docker volume create onthebooks-data
docker volume create pg-admin-data
docker-compose build
docker-compose up
```
### App paths
Use http://localhost:2222/ to connect to the app.
Use http://localhost:2224/docs to connect to Fastapi Swagger for testing the endpoints and documentation.
Use http://localhost:8082/ to connect to pg-admin database for running queries and viewing tables.

### Installing python dependencies locally

In order for VSCode's built in code completion and intelligence to
work correctly, it needs the dependencies from the requirements.txt file
installed. this is done inside docker during the build, but not in your local the workspace.

So you will need to create a virtual environment and pip install the requirements.

1. From inside the `api` folder:

```bash
python -m venv .venv
```

2. Then activate the virtual environment

```bash
source .venv/bin/activate
```

3. And finally install the dependencies

```bash
pip install -r requirements.txt
```
4. Close VSCode and reopen

# Design
### Database Diagram
** Only to show relations, some syntax such as "()'s" removed for diagram creation.
![Database Diagram](https://github.com/drizzymakeplays/onthebooks/assets/118935604/c5f10e5f-1fd4-48aa-ae19-37ed5ce8bbc8)

# API URL:
http://localhost:2222/

# Client Endpoints

### Client Registration and Authentication:
| Behavior | Method | URL |
| --- | --- | --- |
| Register a new client account | POST | `/api/register` |
| Log in to a client account | POST | `/api/login` |
| Log out from the client account | POST | `/api/logout` |

### Client Profile Management:
| Behavior | Method | URL |
| --- | --- | --- |
| Retrieve client profile information | GET | `/api/client/profile` |
| Update client profile information | PUT | `/api/client/profile` |
| Delete the client's own account | DELETE | `/api/client/profile` |

### Barber Listing:
| Behavior | Method | URL |
| --- | --- | --- |
| Get a list of all registered barbers | GET | `/api/barbers` |
| View details of a specific barber | GET | `/api/barbers/{barber_id}` |

### Appointment Booking:
| Behavior | Method | URL |
| --- | --- | --- |
| Get available time slots for a specific barber | GET | `/api/barbers/{barber_id}/availability` |
| Book an appointment with a specific barber | POST | `/api/barbers/{barber_id}/appointments` |
| Cancel a booked appointment | DELETE | `/api/barbers/{barber_id}/appointments/{appointment_id}` |

### View Client's Appointments:
| Behavior | Method | URL |
| --- | --- | --- |
| Get a list of upcoming and past appointments for the client | GET | `/api/client/appointments` |
| View details of a specific appointment | GET | `/api/client/appointments/{appointment_id}` |

# Barber Endpoints

### Barber Registration and Authentication:
| Behavior | Method | URL |
| --- | --- | --- |
| Register a new barber account | POST | `/api/register` |
| Log in to a barber account | POST | `/api/login` |
| Log out from the barber account | POST | `/api/logout` |

### Barber Profile Management:
| Behavior | Method | URL |
| --- | --- | --- |
| Retrieve barber profile information | GET | `/api/barber/profile` |
| Update barber profile information | PUT | `/api/barber/profile` |
| Delete the barber's own account | DELETE | `/api/barber/profile` |

### Working Hours Management:
| Behavior | Method | URL |
| --- | --- | --- |
| Retrieve the barber's working hours | GET | `/api/barber/working-hours` |
| Update the barber's working hours, including regular hours, breaks, and exceptions | PUT | `/api/barber/working-hours` |

### View Barber's Appointments:
| Behavior | Method | URL |
| --- | --- | --- |
| Get a list of upcoming and past appointments for the barber | GET | `/api/barber/appointments` |
| View details of a specific appointment | GET | `/api/barber/appointments/{appointment_id}` |

### Create, Update, and Delete Appointments:
| Behavior | Method | URL |
| --- | --- | --- |
| Create a new appointment for a client | POST | `/api/barber/appointments` |
| Update appointment details | PUT | `/api/barber/appointments/{appointment_id}` |
| Cancel a booked appointment | DELETE | `/api/barber/appointments/{appointment_id}` |

## Client Listing

### Get a list of all clients associated with the barber:
| Behavior | Method | URL |
| --- | --- | --- |
| Get a list of all clients associated with the barber | GET | `/api/clients` |
| View details of a specific client | GET | `/api/clients/{client_id}` |

### Built With
| [<img src="https://www.svgrepo.com/show/331370/docker.svg" alt="docker" width="200" height=150px>](https://docs.docker.com/get-docker/) Docker | [<img src="https://github.com/drizzymakeplays/onthebooks/assets/118935604/4461ab69-77ce-4f01-8f97-d2c7278ef30a" width=200px height=150px>](https://fastapi.tiangolo.com/) FastApi | [<img src="https://www.svgrepo.com/show/374167/vite.svg" alt="Vite.js" width="200" height=150px>](https://vitejs.dev/) Vite.js | [<img src="https://www.svgrepo.com/show/452091/python.svg" alt="Vite.js" width="200" height=150px>](https://www.python.org/) Python | [<img src="https://github.com/drizzymakeplays/onthebooks/assets/118935604/b4a75de8-4afc-4520-b742-eb9a564ae1f6" width=200px height=150px>](https://getbootstrap.com/) BootStrap |
| ----- | --- | ----- | --- | ----- |
