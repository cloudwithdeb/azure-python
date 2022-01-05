#### How to deploy FastAPI app to Azure App Service using cli.

This config demonstrate how to deploy fastapi application to azure app service using your cli.

### Note:
After you have successfully deployed your app service plan and app service, configure the following:
* In app service -> configuration -> Application settings, add the following:

KEY = SCM_DO_BUILD_DURING_DEPLOYMENT
VALUE = 1

* In app service -> configuration -> General settings, change the following:

Startup Command = gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app

* In `script.sh`, change the following:

--sku to your application sku and
--name to the name of your app service
--plan to the name of your app service plan
--runtime to the application runtime

### Deploying the application
To finally deploy your application, change the permission of your `script.sh` file using the command chmod +x script.sh then run the script using `./script.sh` to deploy your FastAPI app to app service.