# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#
# def flowFile = session.get();
# if (flowFile == null) {
# context?.yield();
# }
# else {
# // Try to parse a date here, will fail after Groovy 2.5.0 if groovy-dateutil is not included
# Date.parse('yyyyMMdd', '20190630')
#
# flowFile = session.putAttribute(flowFile, "from-content", "test content")
# session.transfer(flowFile, REL_SUCCESS)
# }