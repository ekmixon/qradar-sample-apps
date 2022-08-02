# Copyright 2020 IBM Corporation
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

from qpylib import qpylib

qpylib.create_log()


# A function that uses qpylib REST function to get a list of available Ariel databases.
# The authentication entry in manifest.json will allow qpylib REST functions to handle the authentication for the app.
def get_ariel_databases():
    try:
        response = qpylib.REST('get', '/api/ariel/databases')
        qpylib.log(f'response={str(response.json())}')
        return response
    except Exception as ex:
        qpylib.log(
            f'Error calling REST api GET /api/ariel/databases: {str(ex)}',
            'ERROR',
        )

        raise
