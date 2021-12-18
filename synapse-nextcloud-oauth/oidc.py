# Copyright 2020 Quentin Gliech
# Copyright 2021 The Matrix.org Foundation C.I.C.
# Copyright 2021 Curtis Parfitt-Ford
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

import logging
from typing import Dict, List

from synapse.handlers.oidc import OidcMappingProvider, Token, UserAttributeDict
from synapse.types import JsonDict, map_username_to_mxid_localpart, UserInfo

logger = logging.getLogger(__name__)


class NextcloudOidcMappingProvider(OidcMappingProvider[None]):
    """An implementation of a mapping provider for Nextcloud OAuth.
    """

    @staticmethod
    def parse_config(config: dict):
        return None

    def get_remote_user_id(self, userinfo: UserInfo) -> str:
        return userinfo["ocs"]["data"]["nickname"]

    async def map_user_attributes(
            self, userinfo: UserInfo, token: Token, failures: int
    ) -> UserAttributeDict:
        data = userinfo["ocs"]["data"]

        localpart = data["nickname"]

        # Ensure only valid characters are included in the MXID.
        localpart = map_username_to_mxid_localpart(localpart)

        # Append suffix integer if last call to this function failed to produce
        # a usable mxid.
        localpart += str(failures) if failures else ""

        display_name = data["name"]
        if display_name == "":
            display_name = None

        emails: List[str] = []
        email = data["email"]
        if email:
            emails.append(email)

        return UserAttributeDict(
            localpart=localpart, display_name=display_name, emails=emails
        )

    async def get_extra_attributes(self, userinfo: UserInfo, token: Token) -> JsonDict:
        extras: Dict[str, str] = {}
        return extras
