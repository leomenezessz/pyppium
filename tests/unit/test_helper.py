import pytest
from assertpy import assert_that
from pyppium.exception import NotFoundElementToClickException
from pyppium.utils import helper


@pytest.mark.unity
def test_should_create_a_string_list_from_web_elements(
    mocker, mock_list_of_web_elements, items_isinstance_extension, mock_web_element_text
):
    list_of_web_elements = mock_list_of_web_elements(mocker)
    mock_web_element_text(mocker, "MyText")
    string_list = helper.elements_list_to_string_list(list_of_web_elements)
    assert_that(string_list).is_instance_of(list)
    assert_that(string_list).is_all_items_instance_of(str)


@pytest.mark.unity
def test_should_click_in_element_by_text(
    mocker, mock_list_of_web_elements, mock_selenium_click, mock_web_element_text
):
    list_of_web_elements = mock_list_of_web_elements(mocker)
    mock_web_element_text(mocker, "myText")
    spy = mocker.spy(helper, "click_in_element_list_by_text")
    result = helper.click_in_element_list_by_text(list_of_web_elements, "myText")
    spy.assert_called_once_with(list_of_web_elements, "myText")
    assert_that(result).is_none()


@pytest.mark.unity
def test_should_click_in_element_if_contais_text(
    mocker, mock_list_of_web_elements, mock_selenium_click, mock_web_element_text
):
    list_of_web_elements = mock_list_of_web_elements(mocker)
    mock_web_element_text(mocker, "myText")
    spy = mocker.spy(helper, "click_in_element_list_if_contains_text")
    result = helper.click_in_element_list_if_contains_text(list_of_web_elements, "Text")
    spy.assert_called_once_with(list_of_web_elements, "Text")
    assert_that(result).is_none()


@pytest.mark.unity
def test_should_raise_exception_to_element_no_found_in_click_by_exact_text(
    mock_list_of_web_elements, mocker, mock_web_element_text
):
    list_of_web_elements = mock_list_of_web_elements(mocker)
    mock_web_element_text(mocker, "myText")
    text_to_found = "Wrong Way"

    with pytest.raises(NotFoundElementToClickException) as e:
        assert_that(
            helper.click_in_element_list_by_text(list_of_web_elements, text_to_found)
        )
    assert_that(str(e.value)).is_equal_to(
        f"Element with the text {text_to_found} could not be found in the list."
    )


@pytest.mark.unity
def test_should_raise_exception_to_element_no_found_in_click_by_text_contains(
    mock_list_of_web_elements, mocker, mock_web_element_text
):
    list_of_web_elements = mock_list_of_web_elements(mocker)
    mock_web_element_text(mocker, "myText")
    text_to_found = "Wrong Way"

    with pytest.raises(NotFoundElementToClickException) as e:
        assert_that(
            helper.click_in_element_list_if_contains_text(
                list_of_web_elements, text_to_found
            )
        )
    assert_that(str(e.value)).is_equal_to(
        f"No one element with the text {text_to_found} can be found in the list."
    )
