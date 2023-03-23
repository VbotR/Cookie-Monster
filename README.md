# Cookie-Monster
Website cookie access.

This program is useful for accessing websites that require the installation of cookies to authenticate or maintain user sessions.

To use this program, you must specify a valid website URL, the name of the cookie and the value of the cookie. The program will then send a GET request to a website with the specified cookies attached, and if the request is successful, the program will save the contents of the response to a file and open it in a new window using the user's default web browser. If the request fails or throws an exception, the program will display an error message indicating what went wrong.
