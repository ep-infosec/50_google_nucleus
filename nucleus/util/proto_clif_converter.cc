/*
 * Copyright 2018 Google LLC.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 */
#include "google/protobuf/message.h"
#include "python/google/protobuf/proto_api.h"
#include "clif/python/types.h"
#include "nucleus/util/proto_clif_converter.h"

namespace nucleus {

static const proto2::python::PyProto_API* py_proto_api = nullptr;

const proto2::python::PyProto_API* GetPyProtoApi(PyObject* py) {
  if (py_proto_api == nullptr) {
    py_proto_api = static_cast<const proto2::python::PyProto_API*>(
        PyCapsule_Import(proto2::python::PyProtoAPICapsuleName(), 0));
  }
  return py_proto_api;
}

}  // namespace nucleus
