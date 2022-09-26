#!/bin/sh
# SPDX-FileCopyrightText: 2020-present Open Networking Foundation <info@opennetworking.org>
#
# SPDX-License-Identifier: Apache-2.0

# remove the old code and regenerate,
# if we don't remove the old code it is possible that removed protos are left behind
grep -lnrw python/ -e "Generated by the protocol buffer compiler" | xargs rm -f
find ./go/onos -name "*.pb.go" -type f -delete

proto_path="./proto:${GOPATH}/src/github.com/gogo/protobuf/protobuf:${GOPATH}/src/github.com/gogo/protobuf:${GOPATH}/src:/go/src/github.com/gogo/protobuf:${GOPATH}/src/github.com/p4lang/p4runtime/proto"

### Documentation generation

# e2t
protoc --proto_path=$proto_path \
    --doc_out=docs/onos/e2t \
    --doc_opt=markdown,admin.md \
    proto/onos/e2t/admin/admin.proto
protoc --proto_path=$proto_path \
    --doc_out=docs/onos/e2t \
    --doc_opt=markdown,e2.md \
    proto/onos/e2t/e2/v1beta1/*.proto

# a1t
protoc --proto_path=$proto_path \
    --doc_out=docs/onos/a1t \
    --doc_opt=markdown,a1.md \
    proto/onos/a1t/a1/*.proto
protoc --proto_path=$proto_path \
    --doc_out=docs/onos/a1t \
    --doc_opt=markdown,a1.md \
    proto/onos/a1t/admin/*.proto

# topo
protoc --proto_path=$proto_path \
    --doc_out=docs/onos/topo \
    --doc_opt=markdown,topo.md \
    proto/onos/topo/topo.proto

# config
protoc --proto_path=$proto_path \
    --doc_out=docs/onos/config \
    --doc_opt=markdown,admin.md \
    proto/onos/config/admin/admin.proto

## onos-config v2 API

protoc --proto_path=$proto_path \
    --doc_out=docs/onos/config/v2 \
    --doc_opt=markdown,value.md \
    proto/onos/config/v2/value.proto

protoc --proto_path=$proto_path \
    --doc_out=docs/onos/config/v2 \
    --doc_opt=markdown,transaction.md \
    proto/onos/config/v2/transaction.proto

protoc --proto_path=$proto_path \
    --doc_out=docs/onos/config/v2 \
    --doc_opt=markdown,proposal.md \
    proto/onos/config/v2/proposal.proto

protoc --proto_path=$proto_path \
    --doc_out=docs/onos/config/v2 \
    --doc_opt=markdown,configuration.md \
    proto/onos/config/v2/configuration.proto



# fabric-sim
protoc --proto_path=$proto_path \
    --doc_out=docs/onos/fabricsim \
    --doc_opt=markdown,devices.md \
    proto/onos/fabricsim/devices.proto

protoc --proto_path=$proto_path \
    --doc_out=docs/onos/fabricsim \
    --doc_opt=markdown,links.md \
    proto/onos/fabricsim/links.proto

protoc --proto_path=$proto_path \
    --doc_out=docs/onos/fabricsim \
    --doc_opt=markdown,hosts.md \
    proto/onos/fabricsim/hosts.proto


# kpimon
protoc --proto_path=$proto_path \
    --doc_out=docs/onos/kpimon \
    --doc_opt=markdown,kpimon.md \
    proto/onos/kpimon/kpimon.proto

# pci
protoc --proto_path=$proto_path \
    --doc_out=docs/onos/pci \
    --doc_opt=markdown,pci.md \
    proto/onos/pci/pci.proto

# mlb
protoc --proto_path=$proto_path \
    --doc_out=docs/onos/mlb \
    --doc_opt=markdown,mlb.md \
    proto/onos/mlb/mlb.proto

# rsm
protoc --proto_path=$proto_path \
    --doc_out=docs/onos/rsm \
    --doc_opt=markdown,rsm.md \
    proto/onos/rsm/rsm.proto

# ransim
protoc --proto_path=$proto_path \
    --doc_out=docs/onos/ransim \
    --doc_opt=markdown,metrics.md \
    proto/onos/ransim/metrics/metrics.proto


protoc --proto_path=$proto_path \
    --doc_out=docs/onos/ransim \
    --doc_opt=markdown,model.md \
    proto/onos/ransim/model/model.proto

protoc --proto_path=$proto_path \
    --doc_out=docs/onos/ransim \
    --doc_opt=markdown,trafficsim.md \
    proto/onos/ransim/trafficsim/trafficsim.proto

protoc --proto_path=$proto_path \
    --doc_out=docs/onos/ransim \
    --doc_opt=markdown,types.md \
    proto/onos/ransim/types/types.proto


# p4rt
protoc --proto_path=$proto_path \
    --doc_out=docs/onos/p4rt \
    --doc_opt=markdown,pipeline_config.md \
    proto/onos/p4rt/v1/pipeline_config.proto

# device-provisioner
protoc --proto_path=$proto_path \
    --doc_out=docs/onos/device-provisioner \
    --doc_opt=markdown,admin.md \
    proto/onos/device-provisioner/admin/admin.proto


### Go Protobuf code generation
go_import_paths="Mgoogle/protobuf/any.proto=github.com/gogo/protobuf/types"
go_import_paths="${go_import_paths},Mgoogle/protobuf/timestamp.proto=github.com/gogo/protobuf/types"
go_import_paths="${go_import_paths},Mgoogle/protobuf/duration.proto=github.com/gogo/protobuf/types"
go_import_paths="${go_import_paths},Mgoogle/protobuf/empty.proto=github.com/gogo/protobuf/types"
go_import_paths="${go_import_paths},Monos/config/device/types.proto=github.com/onosproject/onos-api/go/onos/config/device"
go_import_paths="${go_import_paths},Monos/config/admin/admin.proto=github.com/onosproject/onos-api/go/onos/config/admin"
go_import_paths="${go_import_paths},Monos/ransim/types/types.proto=github.com/onosproject/onos-api/go/onos/ransim/types"
go_import_paths="${go_import_paths},Monos/config/v2/object.proto=github.com/onosproject/onos-api/go/onos/config/v2"
go_import_paths="${go_import_paths},Monos/config/v2/failure.proto=github.com/onosproject/onos-api/go/onos/config/v2"
go_import_paths="${go_import_paths},Monos/config/v2/value.proto=github.com/onosproject/onos-api/go/onos/config/v2"
go_import_paths="${go_import_paths},Monos/config/v2/transaction.proto=github.com/onosproject/onos-api/go/onos/config/v2"
go_import_paths="${go_import_paths},Monos/config/v2/proposal.proto=github.com/onosproject/onos-api/go/onos/config/v2"
go_import_paths="${go_import_paths},Monos/config/v2/configuration.proto=github.com/onosproject/onos-api/go/onos/config/v2"
go_import_paths="${go_import_paths},Monos/p4rt/v1/pipeline_config.proto=github.com/onosproject/onos-api/go/onos/p4rt/v1"
go_import_paths="${go_import_paths},Monos/p4rt/v1/object.proto=github.com/onosproject/onos-api/go/onos/p4rt/v1"
go_import_paths="${go_import_paths},Monos/device-provisioner/admin/admin.proto=github.com/onosproject/onos-api/go/onos/device-provisioner/admin"




# topo and UE-NIB
protoc --proto_path=$proto_path \
    --gogofaster_out=$go_import_paths,import_path=onos/topo,plugins=grpc:./go \
    proto/onos/topo/*.proto
protoc --proto_path=$proto_path \
    --gogofaster_out=$go_import_paths,import_path=onos/uenib,plugins=grpc:./go \
    proto/onos/uenib/*.proto

# e2t
protoc --proto_path=$proto_path \
    --gogofaster_out=$go_import_paths,import_path=onos/e2t/admin,plugins=grpc:./go \
    proto/onos/e2t/admin/*.proto
protoc --proto_path=$proto_path \
    --gogofaster_out=$go_import_paths,import_path=onos/e2t/e2,plugins=grpc:./go \
    proto/onos/e2t/e2/*.proto
protoc --proto_path=$proto_path \
    --gogofaster_out=$go_import_paths,import_path=onos/e2t/e2/v1beta1,plugins=grpc:./go \
    proto/onos/e2t/e2/v1beta1/*.proto

# a1t
protoc --proto_path=$proto_path \
    --gogofaster_out=$go_import_paths,import_path=onos/a1t/a1,plugins=grpc:./go \
    proto/onos/a1t/a1/*.proto
protoc --proto_path=$proto_path \
    --gogofaster_out=$go_import_paths,import_path=onos/a1t/a1,plugins=grpc:./go \
    proto/onos/a1t/admin/*.proto

# o1t
protoc --proto_path=$proto_path \
    --gogofaster_out=$go_import_paths,import_path=onos/o1t,plugins=grpc:./go \
    proto/onos/o1t/*.proto

# onos-config v2 API

protoc --proto_path=$proto_path \
    --gogofaster_out=$go_import_paths,import_path=onos/config/v2,plugins=grpc:./go \
    proto/onos/config/v2/*.proto

# admin.proto cannot be generated with fast marshaler/unmarshaler because it uses gnmi.ModelData
protoc --proto_path=$proto_path \
    --gogo_out=$go_import_paths,import_path=onos/config/admin,plugins=grpc:./go \
    proto/onos/config/admin/*.proto

# fabricsim
protoc --proto_path=$proto_path \
    --gogofaster_out=$go_import_paths,import_path=onos/fabricsim,plugins=grpc:./go \
    proto/onos/fabricsim/*.proto

# p4rt
protoc --proto_path=$proto_path \
    --gogofaster_out=$go_import_paths,import_path=onos/p4rt,plugins=grpc:./go \
    proto/onos/p4rt/v1/*.proto

# device-provisioner
protoc --proto_path=$proto_path \
    --gogofaster_out=$go_import_paths,import_path=onos/device-provisioner/admin,plugins=grpc:./go \
    proto/onos/device-provisioner/admin/*.proto

# kpimon
protoc --proto_path=$proto_path \
    --gogofaster_out=$go_import_paths,import_path=onos/kpimon,plugins=grpc:./go \
    proto/onos/kpimon/*.proto

# pci
protoc --proto_path=$proto_path \
    --gogofaster_out=$go_import_paths,import_path=onos/pci,plugins=grpc:./go \
    proto/onos/pci/*.proto

# mlb
protoc --proto_path=$proto_path \
    --gogofaster_out=$go_import_paths,import_path=onos/mlb,plugins=grpc:./go \
    proto/onos/mlb/*.proto

# rsm
protoc --proto_path=$proto_path \
    --gogofaster_out=$go_import_paths,import_path=onos/rsm,plugins=grpc:./go \
    proto/onos/rsm/*.proto

# mho
protoc --proto_path=$proto_path \
    --gogofaster_out=$go_import_paths,import_path=onos/mho,plugins=grpc:./go \
    proto/onos/mho/*.proto

# ransim
protoc --proto_path=$proto_path \
    --gogofaster_out=$go_import_paths,import_path=onos/ransim/metrics,plugins=grpc:./go \
    proto/onos/ransim/metrics/*.proto

protoc --proto_path=$proto_path \
    --gogofaster_out=$go_import_paths,import_path=onos/ransim/model,plugins=grpc:./go \
    proto/onos/ransim/model/*.proto

protoc --proto_path=$proto_path \
    --gogofaster_out=$go_import_paths,import_path=onos/ransim/trafficsim,plugins=grpc:./go \
    proto/onos/ransim/trafficsim/*.proto

protoc --proto_path=$proto_path \
    --gogofaster_out=$go_import_paths,import_path=onos/ransim/types,plugins=grpc:./go \
    proto/onos/ransim/types/*.proto

# perf
protoc --proto_path=$proto_path \
    --gogofaster_out=$go_import_paths,import_path=onos/topo,plugins=grpc:./go \
    proto/onos/perf/perf.proto


## Protoset generation to allow use of grpcurl

protoc --proto_path=$proto_path \
    --descriptor_set_out=protoset/onos-topo.protoset \
    --include_imports \
    proto/onos/topo/*.proto

protoc --proto_path=$proto_path \
    --descriptor_set_out=protoset/onos-uenib.protoset \
    --include_imports \
    proto/onos/uenib/*.proto

protoc --proto_path=$proto_path \
    --descriptor_set_out=protoset/onos-config.protoset \
    --include_imports \
    proto/onos/config/v2/*.proto

protoc --proto_path=$proto_path \
    --descriptor_set_out=protoset/onos-config-admin.protoset \
    --include_imports \
    proto/onos/config/admin/*.proto

protoc --proto_path=$proto_path \
    --descriptor_set_out=protoset/fabricsim.protoset \
    --include_imports \
    proto/onos/fabricsim/*.proto


### Python Protobuf code generation
mkdir -p ./python
protoc --proto_path=$proto_path \
    --python_betterproto_out=./python \
    $(find proto -name "*.proto" | sort)

# FIXME: come up with a better way to patch python files; this is too brittle
# git apply ./build/bin/patches/*.patch


