# Browserstack

Pyppium has a pretty easy interface with BrowserStack rest API, you can upload, delete, get an apps list or update a test status.

Below has all ```#!python BrowserStackApi class``` requests explained, it's easy like Sunday morning! :sunglasses: 

## Browserstack Interface Class

Browserstack interface is a simple class with some BrowserStack rest requests.

You can use with your credentials in the ```#!python init()``` like the sample below.

```python   

BrowserStackApi("my-user", "my-keys")

```

Or you can connect with your environment variables.

```

export BROWSERSTACK_USERNAME=my-user
export BROWSERSTACK_ACCESS_KEY=my-keys

```

!!! warning
    Remember to use ```$source``` command to refresh your terminal session. :smile:
    
    
After exporting your environments variables, you don't need to send parameters with your BrowserStack credentials anymore.

The ```#!python BrowserStackApi class``` retrieves the user and keys parameters from your local environment.

Now you can use ```#!python BrowserStackApi class``` without sending any parameters, like the sample below. :heart_eyes:

```python   

BrowserStackApi()

```

## BrowserStackApi Requests

Below has some examples of ```#!python BrowserStackApi class``` requests. 

### Getting Recent Apps

To get all recently uploaded apps:

```python

BrowserStackApi().recent_uploads()

```

### Getting Recent Apps By Custom Id


To get all recently uploaded apps with specific ```custom id```:

```python

BrowserStackApi().get_apps_by_custom_id("my-custom-id")

```

### Deleting an app by app-id

You can delete an app from BrowserStack by ```app_id```:

```python

BrowserStackApi().delete_app("your-app-id")

```

### Uploading an app to BrowserStack

You can upload your ```.ipa``` or ```.apk``` to BrowserStack:

```python

BrowserStackApi().upload_app("path/to/my/app")

```

If you want to set a ```custom id``` to your app upload:

```python

BrowserStackApi().upload_app("path/to/my/app", "custom_id")

```

### Updating test status

To update the test status in the Browserstack dashboard:


```python

 BrowserStackApi().update_test_status(
    session=PyppiumDriver.instance().session_id,
    result="passed",
    reason="No reason, its just a test!",
 )

```

## Manipulating Responses

Its easy to manipulate responses from ```#!python BrowserStackApi class```.

Below has some examples of getting body content and status code.


### Getting Body Response

To get a response content as a ```#!python dict``` its easy, just call ```#!python json()```:


```python

body = BrowserStackApi().recent_uploads().json()

print(json.dumps(resp.json(), indent=4))


# console output:
#  [
#      {
#          "app_name": "my-app.ipa",
#          "app_version": "4.23.0",
#          "app_url": "bs://355e6259172efcdd09c49bae90d7f464e8ca2036",
#          "app_id": "355e6259172efcdd09c49bae90d7f464e8ca2036",
#          "uploaded_at": "2020-09-03 21:42:33 UTC"
#      },
#      {
#          "app_name": "app-debug.apk",
#          "app_version": "4.22.1.DEBUG",
#          "app_url": "bs://0fb5cfaa3250f666365ab4e812de002bd1ef69ee",
#          "app_id": "0fb5cfaa3250f666365ab4e812de002bd1ef69ee",
#          "uploaded_at": "2020-09-03 21:07:29 UTC"
#      }
#   ]
 

```

### Getting Status Code Response

You can get a status code as an ```#!python int``` from response:

```python

status = BrowserStackApi().recent_uploads().status_code

print(f"Request status code : {status}")


# console output: Request status code : 200

 
```


!!! Hint
    To understand more about ```#!python httpx Response object``` you can read the [HTTPX Official Documentation](https://www.python-httpx.org/quickstart/). 


<br/>














