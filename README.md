pyIPCheck
https://github.com/korylprince/pyIPCheck

This is a similar interface as https://github.com/korylprince/IPCheck but written for web2py (in python.) While not having every single feature, it works much faster.

#Installing#

Just copy the folder to your web2py applications folder, then copy db.py.def to db.py in the models folder and edit with your options.

We use ldap for logins, but you can use whatever web2py method for authentication you want. 

To use Active Directory with allowed groups, currently web2py must be patched.
Please see http://www.web2pyslices.com/slice/show/1493/active-directory-ldap-with-allowed-groups on how to set that up.
This issue has been fixed in a new development version of web2py.

If you have any issues or questions, email the email address below, or open an issue at:
https://github.com/korylprince/IPCheck/issues

#Usage#

This distribution is a simple web interface for checking ports on IP addresses. We use it to check if certain devices are up.

You can add services using the appadmin interface of web2py.

Port 445 is common for a Windows machine.

Port 22 for a Linux machine (with an ssh-server.)

Ports 80 or 23 are commonly used for switches.

#Copyright Information#

Some javascript code may have their own license.

All other code is Copyright 2012 Kory Prince (korylprince at gmail dot com.) This code is licensed under the GPL v3 which is included in this distribution. If you'd like it licensed under another license then send me an email.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
