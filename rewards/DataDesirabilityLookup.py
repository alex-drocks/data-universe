from common.data import DataLabel, DataSource
from rewards.data import DataSourceDesirability, DataDesirabilityLookup


# Pydantic can't serialize a model to json when it has dictionaries with
# non-primitive keys. There are probably ways to write a custom serializer/deserializer,
# but for now, we'll just write the model in code, because it's easy enough to read.

# The benefit of the extra validation and standardization provided by DataLabel outweighs
# the cost of not being able to serialize the model to json.

LOOKUP = DataDesirabilityLookup(
    distribution={
        DataSource.REDDIT: DataSourceDesirability(
            weight=0.5,
            default_scale_factor=0.5,
            # The following labels were pulled from the top 1XX subreddits relating to cryptocurrency.
            # We welcome feedback on this list. Please file an Issue on the github with your suggestions.
            label_scale_factors={
                DataLabel(value="Bitcoin"): 1.0,
                DataLabel(value="BitcoinCash"): 1.0,
                DataLabel(value="Bittensor_"): 1.0,
                DataLabel(value="Btc"): 1.0,
                DataLabel(value="Cryptocurrency"): 1.0,
                DataLabel(value="Cryptomarkets"): 1.0,
                DataLabel(value="EthereumClassic"): 1.0,
                DataLabel(value="Ethtrader"): 1.0,
                DataLabel(value="Filecoin"): 1.0,
                DataLabel(value="Monero"): 1.0,
                DataLabel(value="Polkadot"): 1.0,
                DataLabel(value="Solana"): 1.0,
                DataLabel(value="WallstreetBets"): 1.0,
            },
        ),
        DataSource.X: DataSourceDesirability(
            weight=0.5,
            default_scale_factor=0.5,
            label_scale_factors={
                DataLabel(value="#bitcoin"): 1.0,
                DataLabel(value="#bitcoincharts"): 1.0,
                DataLabel(value="#bitcoiner"): 1.0,
                DataLabel(value="#bitcoinexchange"): 1.0,
                DataLabel(value="#bitcoinmining"): 1.0,
                DataLabel(value="#bitcoinnews"): 1.0,
                DataLabel(value="#bitcoinprice"): 1.0,
                DataLabel(value="#bitcointechnology"): 1.0,
                DataLabel(value="#bitcointrading"): 1.0,
                DataLabel(value="#bittensor"): 1.0,
                DataLabel(value="#btc"): 1.0,
                DataLabel(value="#cryptocurrency"): 1.0,
                DataLabel(value="#crypto"): 1.0,
                DataLabel(value="#defi"): 1.0,
                DataLabel(value="#decentralizedfinance"): 1.0,
                DataLabel(value="#tao"): 1.0,
            },
        ),
    },
    max_age_in_hours=7 * 24,
)