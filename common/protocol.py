# The MIT License (MIT)
# Copyright © 2023 data-universe

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the “Software”), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of
# the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import typing
import bittensor as bt
import pydantic
from common.data import DataEntityBucket, DataEntity, DataEntityBucketId
from typing import List


class GetMinerIndex(bt.Synapse):
    """
    Protocol by which Validators can retrieve the Index from a Miner.

    Attributes:
    - data_entity_buckets: A list of DataEntityBucket objects that the Miner can serve.
    """

    # Required request output, filled by receiving axon.
    data_entity_buckets: List[DataEntityBucket] = pydantic.Field(
        title="data_entity_buckets",
        description="All of the data entity buckets that a Miner can serve.",
        frozen=False,
        repr=False,
    )

    def deserialize(self) -> int:
        """
        Deserialize the data_entity_buckets output. This method retrieves the response from
        the miner in the form of data_entity_buckets, deserializes it and returns it
        as the output of the dendrite.query() call.

        Returns:
        - List[DataEntityBucket]: The deserialized response, which in this case is the value of data_entity_buckets.
        """
        return self.data_entity_buckets


class GetDataEntityBucket(bt.Synapse):
    """
    Protocol by which Validators can retrieve the DataEntities of a Bucket from a Miner.

    Attributes:
    - bucket_id: The id of the bucket that the requester is asking for.
    - data_entities: A list of DataEntity objects that make up the requested DataEntityBucket.
    """

    # Required request input, filled by sending dendrite caller.
    data_entity_bucket_id: DataEntityBucketId = pydantic.Field(
        title="data_entity_bucket_id",
        description="The identifier for the requested DataEntityBucket.",
        frozen=True,
        repr=False,
    )

    # Required request output, filled by recieving axon.
    data_entities: List[DataEntity] = pydantic.Field(
        title="data_entities",
        description="All of the data that makes up the requested DataEntityBucket.",
        frozen=False,
        repr=False,
    )

    def deserialize(self) -> int:
        """
        Deserialize the data_entities output. This method retrieves the response from
        the miner in the form of data_entities, deserializes it and returns it
        as the output of the dendrite.query() call.

        Returns:
        - List[DataEntity]: The deserialized response, which in this case is the value of data_entities.
        """
        return self.data_entities


# TODO Protocol for Users to Query Data which will accept query parameters such as a startDatetime, endDatetime.
