from typing import List
import pytest
from appium.webdriver import WebElement
from assertpy import assert_that
from selenium.webdriver.common.by import By
from pyppium import condition


@pytest.mark.unity
def test_wait_visibility(mocker, mock_selenium_wait, mock_pyppium_instance):
    spy = mocker.spy(condition, "wait_visibility_of_element")
    element = condition.wait_visibility_of_element(By.ID, "button", 10)
    spy.assert_called_once_with(By.ID, "button", 10)
    assert_that(element).is_type_of(WebElement.__class__)


@pytest.mark.unity
def test_waits_visibilities(mocker, mock_selenium_waits, mock_pyppium_instance):
    spy = mocker.spy(condition, "wait_visibility_of_elements")
    elements = condition.wait_visibility_of_elements(By.ID, "button", 10)
    spy.assert_called_once_with(By.ID, "button", 10)
    assert_that(elements).is_type_of(List[WebElement].__class__)


@pytest.mark.unity
def test_waits_visibilities_of_any(mocker, mock_selenium_waits, mock_pyppium_instance):
    spy = mocker.spy(condition, "wait_visibility_of_any_elements")
    elements = condition.wait_visibility_of_any_elements(By.ID, "button", 10)
    spy.assert_called_once_with(By.ID, "button", 10)
    assert_that(elements).is_type_of(List[WebElement].__class__)


@pytest.mark.unity
def test_wait_presence_of_element(mocker, mock_selenium_wait, mock_pyppium_instance):
    spy = mocker.spy(condition, "wait_presence_of_element")
    elements = condition.wait_presence_of_element(By.ID, "button", 10)
    spy.assert_called_once_with(By.ID, "button", 10)
    assert_that(elements).is_type_of(WebElement.__class__)


@pytest.mark.unity
def test_wait_invisibility_of_element(mocker, mock_selenium_wait, mock_pyppium_instance):
    spy = mocker.spy(condition, "wait_invisibility_of_element")
    elements = condition.wait_invisibility_of_element(By.ID, "button", 10)
    spy.assert_called_once_with(By.ID, "button", 10)
    assert_that(elements).is_type_of(WebElement.__class__)


@pytest.mark.unity
def test_wait_element_to_be_clickable(mocker, mock_selenium_wait, mock_pyppium_instance):
    spy = mocker.spy(condition, "wait_element_to_be_clickable")
    elements = condition.wait_element_to_be_clickable(By.ID, "button", 10)
    spy.assert_called_once_with(By.ID, "button", 10)
    assert_that(elements).is_type_of(WebElement.__class__)
