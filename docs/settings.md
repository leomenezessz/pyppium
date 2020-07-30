# Settings

Pyppium has some global default settings and you can override all settings with a simple YAML file.

Just add a file called `pyppium.yaml` to your root directory project like the sample below.

```yaml

driver: # driver main settings.
  timeout: 45 # fetch/fetches timeout.
  appium_url: "http://localhost:3333/wd/hub" # appium base URL.
  browserstack_url: "@hub-cloud.browserstack.com/wd/hub:8080" # brosewrstack base url.

```


Or you can override only a specific key like timeout by example.

```yaml

driver:
  timeout: 45

```

!!! Note
    Even with this settings file, you can override settings at runtime.
