# automate-shinyapps-deploy
Setup required for automated deploy to shinyapps.io

A [minimal python shiny application](https://richleysh84.shinyapps.io/scheduled-deployment/)
displays the time it was deployed to shinyapps.io servers. This is deployed on
a weekly basis by GitHub Actions. 

## Workflow Guide

```mermaid
flowchart LR
    A[update.yml] ==>|Saturday 00:00| B(Job: Install dependencies)
    B ==> C(Job: Run save_time.py)
    C -->|write datetime.now| D[saved_time.txt]
    C ==> E(Job: Configure rsconnect)
    H([SHINYAPPS_USERNAME\nSHINYAPPS_TOKEN\nSHINYAPPS_SECRET]) -.-> E
    E ==> F(Job: Deploy to rsconnect)
    K([APP_ID]) -.-> F
    F ==> G{{shinyapps.io: serve app.py}}
    D -.->|python -m shiny run app.py| G    
```

The [GitHub Actions workflow file](/./.github/workflows/update.yml) expects the
repository to have configured:

- environment variables
    - `SHINYAPPS_USERNAME`
- secrets
    - `SHINYAPPS_TOKEN`
    - `SHINYAPPS_SECRET`
    - `APP_ID`

Note the workflow deploys to an application called `scheduled-deployment`.
Update this title for your use case.

For help on finding values for shinyapps tokens & secrets, consult
[Posit's documentation](https://docs.posit.co/shinyapps.io/getting-started.html?_gl=1*5o5r6u*_ga*MTIyMzQ1MTAwLjE2OTc5NTQ0NzQ.*_ga_8QJS108GF1*MTcwMzU3MzgwMy4xMi4xLjE3MDM1NzM4MTAuMC4wLjA.#configure-rsconnect-python).
To find the correct `APP_ID` you will need to successfully deploy the
application from the command line. Once deployed, find the ID of the deployed
app in your shinyapps dashboard. 



