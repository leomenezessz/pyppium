# Fecther

The Pyppium fetcher is a module to search elements by the platform. It contains some behaviours like check the consistency of the queries, waits, timeout to search some element.

## Basic fetcher usage

To find one element to the android and ios platform, inside of your screen.

```python

class MyScreen:

 _button = fetch(iOS("xpath", "//XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]"), Android("id", "my_button"))

```

This sample above its a simple association of `#!python _button` to the fetch class. 
The class `#!python Android` and `#!python iOS` only will check if you using a valid locator, before running the tests.

If you don't want to use string as the locator you can use the `#!python By class` from the selenium, just import it.

```python

class MyScreen:

 _button = fetch(iOS(By.XPATH,"//XCUIElementTypeWindow[1]/XCUIElementTypeButton"), Android(By.ID, "my_button"))

```

To fetch a list of elements you can use `#!python fetches from fetcher module`.

```python



class MyScreen:

 _my_labels_list = fetches(iOS(By.XPATH,"//XCUIElementTypeStaticText"), Android(By.ID, "my_text_view"))


```

!!! warning
    Always try to use ids instead of XPath because ids make your tests more consistent and fast.


The order of parameters matters, the first parameter is `#!python iOS class` and second is `#!python Android class`. 

But if you don't want to send Android parameter, don't have any problem since you don't run tests with an android capability.


```python



class MyScreen:

 _my_labels_list = fetches(iOS(By.XPATH,"//XCUIElementTypeStaticText"))


```

You can run only for android with named parameter.

```python



class MyScreen:

 _my_labels_list = fetches(android=Android(By.ID, "my_text_view"))


```

## Timeouts

Every fetch has a timeout and the default timeout is 15 seconds. You can override the fetch timeout like this sample below.

```python



class MyScreen:

 _button = fetch(iOS("xpath", "//XCUIElementTypeOther[1]"), Android("id", "my_button"), timeout=20)


```

## Waits

The fetcher has a default wait to every fetch. To the `#!python fetch class` the default wait is `wait_visibility_of_element`
and for the `#!python fetches class` the default is `wit_visibility_of_elements`. 

You can override the wait function sending the constant with the value of wait from conditions module.


```python



class MyScreen:

 _button = fetch(iOS("xpath", "//XCUIElementTypeOther[1]"), Android("id", "my_button"), wait_condition=PRESENCE)


```

Have some possibilities of wait in the condition module below have the condition and a little description.

=== "fetch"

    * `#!python condition.VISIBILITY:` Wait for an element to be visible.
    * `#!python condition.PRESENCE:` Wait for the presence of the element.
    * `#!python condition.INVISIBILITY:` Wait for an element to be invisible.
    * `#!python condition.CLICKABLE:` Wait for an element to be clickable.
    

=== "fetches"

    * `#!python condition.VISIBILITIES:` Wait for the visibility of some elements.
    * `#!python condition.VISIBILITY_OF_ANYS:` Wait for visibility of any elements.


<br/>


