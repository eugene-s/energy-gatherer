from celery import current_app as app, group

from gatherer.backends import EnergyAsset, EnergyAssetsStat, CentralEnergyAsset


@app.task(name='check-energy-assets')
def check_energy_assets():
    energy_assets = app.conf.energy_assets
    group_assets = group(
        check_energy_asset.delay(asset)
        for asset in energy_assets
    )
    group_assets()


@app.task(name='check-energy-asset')
def check_energy_asset(domain):
    energy_asset = EnergyAsset(domain)
    res = energy_asset.get()
    EnergyAssetsStat.store_stat(
        consumption=res.consumption,
        production=res.production,
        timestamp=res.timestamp
    )


@app.task
def send_aggregated_result():
    central = CentralEnergyAsset()
    aggregated_stat = EnergyAssetsStat.get_stats_for_last_min()
    central.send_master_record(**aggregated_stat)
