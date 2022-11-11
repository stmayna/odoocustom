# Agenda: Odoo APAC Partner Internal Training

## Odoo Standard upgrade
> New version every year
> Few changes
> Run inside module and have different version for each Odoo version.

## On-premise:
> Python Command line (find it on documentation).

> Make sure openupgradelib python library is installed in the server.

> Odoo SH: Using Upgrade Button.

> Website upload form


## Potential issues:
Because we need to upgrade custom module by ourself.

## How to fix something if you find issue. You may send the ticket here:
https://www.odoo.com/help


## Migration Scripts:
Run it during module upgrade.
Depends on each module.

## Type of migration script:
> pre-**.py
> post-**.py
> end-**.py

## More detail about migration script:
https://oca.github.io/OpenUpgrade/development.html

## Structure:
migrations/version name

migrations/14.0.1.0.0

and put the function name on "__manifest__.py"

## Example of migration script:
https://oca.github.io/OpenUpgrade/API.html

## They show the Demo.

## If there is an issue upgrading:
On-premise, check the terminal error message.
SH, chech the logs.

## Best practice:
Useful SQL query, if it happen many times, write a function to upgrade.

Localhost, don't forget to backup the database.

Localhost testing, backup test database.

## Documentation you may visit:
> https://www.odoo.com/documentation/15.0/administration/upgrade.html

> https://upgrade.odoo.com/

## QnA
> No option to rollback to the old version. (He seems unsure while answering this question)