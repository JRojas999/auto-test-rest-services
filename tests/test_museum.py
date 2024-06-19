import pytest
import requests


def test_get_1():
    url = "https://www.metmuseum.org/es/met-publications?_gl=1*1rzbuh6*_gcl_au*MzY0NDIwNjA5LjE3MTg2Njc3ODQ.*_ga*NjQwMjM2NTgwLjE3MTg2Njc3ODQ.*_ga_Y0W8DGNBTB*MTcxODY2Nzc4My4xLjEuMTcxODY2ODgwNC4wLjAuMA.."
    response = requests.get(url)
    assert response.status_code == 200


def test_get_2():
    url = url = "https://www.metmuseum.org/es/about-the-met/collection-areas"
    response = requests.get(url)
    assert response.status_code == 200


def test_get_3():
    url = "https://www.metmuseum.org/es/plan-your-visit/group-visits"
    response = requests.get(url)
    assert response.status_code == 200
