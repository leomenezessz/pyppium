# Fecther

The Pyppium fetcher is an module to search elements by platform. It contains 
some behaviours like check the consistance of the queries, waits options, timeout
to serch some element.

## Basic fetcher usage

To find one element to the android and ios platform, inside of your screen.

```python

class MyScreen:

 _button = fetch(Android("id", "my_button"), iOS("xpath", "//XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]"))

```

This sample above its a simple association of `#!python _button` to the fetch class. 
The class `#!python Android` and `#!python iOS` only will checking if you using a valid locator, before running the tests.

If you don't want to use string as the locator you can use a the `#!python By class` from the selenium, just import it.

```python

class MyScreen:

 _button = fetch(Android(By.ID, "my_button"), iOS(By.XPATH,"//XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]"))

```

To fetch a list of elements you can use `#!python fetches from fetcher module`.

```python



class MyScreen:

 _my_labels_list = fetches(Android(By.ID, "my_text_view"), iOS(By.XPATH,"//XCUIElementTypeStaticText"))


```

!!! warning
    Always try to use ids instead xpath because ids make your tests more strong and more fast.


