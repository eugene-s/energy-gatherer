class EnergyAssetStat(Model):
    consumption = db.Column(Integer)
    production = db.Column(Integer)
    timestamp = db.Column(DateTime)
