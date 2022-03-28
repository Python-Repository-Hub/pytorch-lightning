# Copyright The PyTorch Lightning team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from typing import Union

from pytorch_lightning.plugins.precision.precision_plugin import PrecisionPlugin
from pytorch_lightning.utilities import AMPType


class MixedPrecisionPlugin(PrecisionPlugin):
    """Base Class for mixed precision."""

    @property
    def backend(self) -> AMPType:
        """AMP-Backend used by this plugin.

        Typically one of AMPType.NATIVE | AMPType.APEX

        .. deprecated:: v1.6
            This property is deprecated in 1.6 and will be removed in 1.7.
            Please use instance checks against the plugin class instead.
        """

    precision: Union[str, int] = "mixed"
