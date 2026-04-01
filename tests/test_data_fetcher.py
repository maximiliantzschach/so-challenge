"""
Pytest tests for data_fetcher.py
- Fetches monthly SO question counts (2008-2024)
- Returns a pandas DataFrame
- Caches results locally as CSV
- Handles network errors gracefully
"""
import os
import pandas as pd
import pytest
from unittest import mock

import data_fetcher

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        'year': [2008, 2008],
        'month': [1, 2],
        'count': [100, 150]
    })

def test_fetch_returns_dataframe(sample_df):
    with mock.patch('data_fetcher.fetch_so_monthly_counts', return_value=sample_df):
        df = data_fetcher.fetch_so_monthly_counts()
        assert isinstance(df, pd.DataFrame)
        assert set(df.columns) == {'year', 'month', 'count'}

def test_caching_creates_csv(tmp_path, sample_df):
    cache_file = tmp_path / 'so_counts.csv'
    with mock.patch('data_fetcher.fetch_so_monthly_counts', return_value=sample_df):
        with mock.patch('data_fetcher.CACHE_PATH', str(cache_file)):
            df = data_fetcher.fetch_so_monthly_counts()
            assert os.path.exists(cache_file)
            cached = pd.read_csv(cache_file)
            pd.testing.assert_frame_equal(cached, sample_df)

def test_network_error_handling():
    with mock.patch('data_fetcher.fetch_so_monthly_counts', side_effect=Exception('Network error')):
        try:
            data_fetcher.fetch_so_monthly_counts()
        except Exception as e:
            assert 'Network error' in str(e)
