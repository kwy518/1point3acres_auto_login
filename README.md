# 1point3acres automatic login application on Heroku

## Summary
An automated Python script to get daily rewards from 1point3acres (一畝三分地), 
and deploy the application on Heroku.

## Deployment

1. Fork to your github repository.
<img src="https://imgur.com/k3Y979C.png">

2. Create the Heroku free account.

3. Create new app on Heruko.
  - Click `New` > `Create New App` > `Create your own app name`
 
4. Connect with your Github.
  - Go to `Deploy` tab > `Connect to Gtihub` > `Search your github repository`
<img src="https://imgur.com/5KxqpRZ.png">

5. Set up login credential.
  - Go to `Setting` tab > Click `Reveal Config Vars`
  - Create 4 pair of **Key : Values**
    - CHROMEDRIVER_PATH : /app/.chromedriver/bin/chromedriver
    - GOOGLE_CHROME_BIN : /app/.apt/usr/bin/google_chrome
    - USERNAME : {your own 1point3acres username}
    - PASSWORD : {your own 1point3acres password}
    
<img src="https://imgur.com/Vi1rjnl.png">

6. Set up Buildpacks for Webdriver and Google Chrome.
    - Scroll down to `Buildpacks` > Click `Add Buildpacks`
    - Type 3 urls
      - `https://github.com/heroku/heroku-buildpack-google-chrome`
      - `https://github.com/heroku/heroku-buildpack-chromedriver`
      - `https://github.com/heroku/heroku-buildpack-python`
7. All Done!
   - Click `Open App` to see the results!
   
Optional:
-
Set up Scheduler on Heroku:
* Click `Resources` > `Heroku Scheduler` > `Create Job`
* Choose `Every day at ...` with anytime you like
* Copy and paste `python main.py` in the command input below
* Save job

<img src="https://i.imgur.com/hj6adwI.png">
