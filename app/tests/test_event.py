import pytest
import requests


data = (
    ('http://localhost:8000/events', '[{"id":3,"photo":"static/drawio.png","title":"Масленица","small_text":"Февральская масленица"},{"id":2,"photo":"static/drawio.png","title":"Пасха","small_text":"Привет православные"},{"id":4,"photo":"static/drawio.png","title":"День Победы","small_text":"9 мая"},{"id":5,"photo":"static/drawio.png","title":"8 марта","small_text":"Женский день"},{"id":6,"photo":"static/2024-04-18_15-00-27.png","title":"День труда","small_text":"1 мая "}]')
,
("http://localhost:8000/events/6", '{"photo":"static/2024-04-18_15-00-27.png","title":"День труда","big_text":"1 мая - Труда в честь Ленина"}')
)


@pytest.mark.parametrize('url, result', data)
def test_api(url, result):
    res = requests.get(url)
    assert res.text == result

