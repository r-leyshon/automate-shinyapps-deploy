# automate-shinyapps-deploy
Setup required for automated deploy to shinyapps.io

A [minimal python shiny application](https://richleysh84.shinyapps.io/scheduled-deployment/)
displays the time it was deployed to shinyapps.io servers. This is deployed on
a weekly basis by GitHub Actions. 

## Workflow Guide

The [GitHub Actions workflow file](/./.github/workflows/update.yml) expects the
repository to have configured:

- environment variables
    - `RSCONNECT_USERNAME`
- secrets
    - `RSCONNECT_TOKEN`
    - `RSCONNECT_SECRET`
    - `APP_ID`

Note the workflow deploys to an application called `scheduled-deployment`.
Update this title for your use case.

For help on finding values for shinyapps tokens & secrets, consult
[Posit's documentation](https://docs.posit.co/shinyapps.io/getting-started.html?_gl=1*5o5r6u*_ga*MTIyMzQ1MTAwLjE2OTc5NTQ0NzQ.*_ga_8QJS108GF1*MTcwMzU3MzgwMy4xMi4xLjE3MDM1NzM4MTAuMC4wLjA.#configure-rsconnect-python).
To find the correct `APP_ID` you will need to successfully deploy the
application from the command line. Once deployed, find the ID of the deployed
app in your shinyapps dashboard. 



