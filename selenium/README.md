# selenium 

## install 

```
    pip install selenium    
```

## Example

``` python
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.python.org")

search_text = driver.find_element_by_id('id-search-field')
#search_text = driver.find_element_by_name('q')
search_text.send_keys(" and some", Keys.ARROW_DOWN)
```


## create instance

``` python
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.python.org")

```
<href a = "https://selenium-python.readthedocs.io/locating-elements.html#locating-elements">詳細可以參考</a>
## Locating Elements
<ul>   
    <li>find_element_by_id</li>
    <li>find_element_by_name</li>
    <li>find_element_by_xpath</li>
    <li>find_element_by_link_text</li>
    <li>find_element_by_partial_link_text</li>
    <li>find_element_by_tag_name</li>
    <li>find_element_by_class_name</li>
    <li>find_element_by_css_selector</li>
</ul>
To find multiple elements
<ul>   
    <li>find_elements_by_id</li>
    <li>find_elements_by_name</li>
    <li>find_elements_by_xpath</li>
    <li>find_elements_by_link_text</li>
    <li>find_elements_by_partial_link_text</li>
    <li>find_elements_by_tag_name</li>
    <li>find_elements_by_class_name</li>
    <li>find_elements_by_css_selector</li>
</ul>

Other method using By

```python
from selenium.webdriver.common.by import By
driver.find_element(By.XPATH, '//button[text()="Some text"]')
```
These are the attributes available for By class:
```
ID = "id"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
NAME = "name"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"
```

## Navigating

### Manipulate Elements 
<ul>   
    <li>send_keys</li>
    <li>clear()</li>
    <li>click</li>
</ul>

<a href = "https://selenium-python.readthedocs.io/navigating.html">Navigating</a>

send_keys
```python
from selenium.webdriver.common.keys import Keys
search_text.send_keys("python ", "3")
search_text.send_keys("python", Keys.ENTER)
```
### handle Selection Element

```python
element = driver.find_element_by_xpath("//select[@name='project']")
all_options = element.find_elements_by_tag_name("option")
for option in all_options:
    print("Value is: %s" % option.get_attribute("value"))
    print("Text is: %s" % option.text)
    print('--------------------')
```
use Select
```python
from selenium.webdriver.support.ui import Select
select = Select(driver.find_element_by_name('project'))
select.select_by_index(index)
select.select_by_visible_text("text")
select.select_by_value(value)
select.deselect_all()

```

### Switch Window
有些情況會跳出新視窗,這時候需要用driver.switch_to.window

```python
driver.switch_to_window("windowName")
```
也可以透過driver.window_handles[1]取得第一個視窗的名字

```python
driver.switch_to.window(driver.window_handles[1])   
```

### Switch Frame
```html
<html>
 <iframe id="frame1">
  <iframe id="frame2"/>
 </iframe>
</html>
```



#### driver.switch_to.frame("name or id")

```python
driver.switch_to.frame("frame1")
```
#### nested frame
必須一層一層切進去

```python
driver.switch_to.frame("frame1")
driver.switch_to.frame("frame2")
```
也可以使用(待測試)
```python
driver.switch_to_frame("frame1.0.frame2")
```


回到上一層
```python
driver.switch_to.parent_frame()
```

#### return frame
```python
driver.switch_to.default_content()#可以跳出frame
```

### go back and go forward

```python
driver.forward()
driver.back()
```

## Waits




