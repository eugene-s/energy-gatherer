import os

import requests


class EnergyAssetsStat:
    @classmethod
    def store_stat(cls, **kwargs):
        energy_asset = EnergyAssetStat(
            consumption=kwargs.pop('consumption'),
            production=kwargs.pop('production'),
            timestamp=kwargs.pop('timestamp'),
        )
        db.session.add(energy_asset)
        db.session.commit()

    @classmethod
    def get_stats_for_last_min(cls):
        # using group by
        return {
            'consumption': None,
            'production': None,
            'timestamp': None,
        }


class CentralEnergyAsset:
    DOMAIN = None
    PROTOCOL = None
    MASTER_RECORD_ENDPOINT = None

    def send_master_record(self, consumption, production, timestamp):
        return requests.post(f'{self.PROTOCOL}://{self.DOMAIN}{self.MASTER_RECORD_ENDPOINT}', data={
            'consumption': consumption,
            'production': production,
            'timestamp': timestamp,
        })


class EnergyAsset:
    PROTOCOL = os.getenv('ENERGY_ASSETS_PROTOCOL')
    GET_ENDPOINT = os.getenv('ENERGY_ASSETS_ENDPOINT')

    def __init__(self, domain):
        self.domain = domain

    def get(self):
        return requests.get(  # todo serialize
            f'{self.PROTOCOL}://{self.domain}{self.GET_ENDPOINT}'
        )
