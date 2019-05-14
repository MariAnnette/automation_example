from behave import when, then
from selenium.webdriver.common.by import By


COLOR = [By.CSS_SELECTOR, "div#variation_color_name li[title='Click to select {}']"]
SELECTED_COLOR = (By.CSS_SELECTOR, 'div#variation_color_name span.selection')
COLOR_OPTIONS = (By.CSS_SELECTOR, 'div#variation_color_name li')

def create_locator_color(color) -> list:
    """
    :param color: this is a string to put into COLOR locator
    :return: full locator searching for a certain color
    """
    print(color)
    return [COLOR[0], COLOR[1].format(color)]

@when('Click on color {color}')
def click_color(context, color):
    locator = create_locator_color(color)  # use create_locator_color function (above) to make a locator
    context.driver.find_element(*locator).click()


@then('Color is updated to {expected_color}')
def click_color(context, expected_color):
    assert context.driver.find_element(*SELECTED_COLOR).text == expected_color


@then('Verify user can select through colors')
def verify_colors_selection(context):
    expected_colors = ['Black', 'Emerald', 'Navy', 'Winter White']
    color_webelements = context.driver.find_elements(*COLOR_OPTIONS)
    print('\n\nWebElements:\n', color_webelements)

    for x in range(len(color_webelements)):
        print('\nWebElement:', color_webelements[x])
        color_webelements[x].click()

        actual_color_text = context.driver.find_element(*SELECTED_COLOR).text
        print('Actual color: ', actual_color_text)

        print('Expected color: ', expected_colors[x])
        assert actual_color_text == expected_colors[x], \
            'Expected color {}, but got {}'.format(expected_colors[x], actual_color_text)


# @then('Verify user can select through colors')
# def verify_colors_selection(context):
#     expected_colors = ['Black', 'Emerald', 'Navy', 'Winter White']
#     colors = context.driver.find_elements(*COLOR_OPTIONS)
#     for color in colors:
#         color.click()
#         assert context.driver.find_element(*SELECTED_COLOR).text == expected_colors[colors.index(color)]


@then('Verify user can select jeans colors')
def verify_jeans_colors_selection(context):
    expected_colors = ['Rinse', 'Medium Wash', 'Dark Wash']
    color_webelements = context.driver.find_elements(*COLOR_OPTIONS)
    print('\n\nWebElements:\n', color_webelements)

    for x in range(len(color_webelements)):
        print('\nWebElement:', color_webelements[x])
        color_webelements[x].click()

        actual_color_text = context.driver.find_element(*SELECTED_COLOR).text
        print('Actual color: ', actual_color_text)

        print('Expected color: ', expected_colors[x])
        assert actual_color_text == expected_colors[x], \
            'Expected color {}, but got {}'.format(expected_colors[x], actual_color_text)