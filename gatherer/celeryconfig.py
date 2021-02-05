import os

beat_schedule = {
    'check-15-sec-energy-asset': {
        'task': 'check_energy_asset'
    }
}


energy_assets = (
    os.getenv('ENERGY_ASSETS').split(',')
    if os.getenv('ENERGY_ASSETS', None) else []
)
