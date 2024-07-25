import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(list_of_dicts_to_filter, filtered_list_of_dicts):
    assert filter_by_state(list_of_dicts_to_filter) == filtered_list_of_dicts


def test_filter_by_state_():
    assert filter_by_state([]) == []


def test_filter_by_state_canceled(list_of_dicts_to_filter, filtered_list_of_dicts_canceled):
    assert filter_by_state(list_of_dicts_to_filter, state="CANCELED") == filtered_list_of_dicts_canceled


def test_sort_by_date(list_of_dicts_to_filter, sorted_by_date):
    assert sort_by_date(list_of_dicts_to_filter) == sorted_by_date


def test_sort_by_date_reverse(list_of_dicts_to_filter, sorted_by_date_reverse):
    assert sort_by_date(list_of_dicts_to_filter, reverse=False) == sorted_by_date_reverse


def test_sort_by_date_():
    assert sort_by_date([]) == []
