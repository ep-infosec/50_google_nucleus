# Code for reading and writing genomics data.

package(
    default_visibility = [
        "//visibility:public",
    ],
)

licenses(["notice"])  # Apache License 2.0

#
# Python API
#

py_library(
    name = "io_py",
    deps = [
        ":converter_lib",
        ":io_libs_py",
    ],
)

py_library(
    name = "io_libs_py",
    deps = [
        ":bed",
        ":bedgraph",
        ":clif_postproc",
        ":fasta",
        ":fastq",
        ":genomics_reader",
        ":genomics_writer",
        ":gff",
        ":sam",
        ":sharded_file_utils",
        ":tabix",
        ":tfrecord",
        ":vcf",
        "//nucleus/io/python:hts_verbose",
    ],
)

py_library(
    name = "genomics_reader",
    srcs = ["genomics_reader.py"],
    deps = [
        "//nucleus/io/python:tfrecord_reader",
        "@absl_py//absl/logging",
    ],
)

py_test(
    name = "genomics_reader_test",
    srcs = ["genomics_reader_test.py"],
    data = ["//nucleus/testdata"],
    python_version = "PY3",
    srcs_version = "PY3",
    deps = [
        ":genomics_reader",
        "//nucleus/protos:gff_py_pb2",
        "//nucleus/testing:py_test_utils",
        "@absl_py//absl/testing:absltest",
    ],
)

py_library(
    name = "genomics_writer",
    srcs = ["genomics_writer.py"],
    deps = [
        "//nucleus/io/python:tfrecord_writer",
        "@absl_py//absl/logging",
    ],
)

py_library(
    name = "vcf",
    srcs = ["vcf.py"],
    deps = [
        ":genomics_reader",
        ":genomics_writer",
        "//nucleus/io/python:vcf_reader",
        "//nucleus/io/python:vcf_writer",
        "//nucleus/protos:variants_py_pb2",
        "//nucleus/util:ranges",
        "//nucleus/util:variant_utils",
        "//nucleus/util:vcf_constants",
    ],
)

py_test(
    name = "vcf_test",
    size = "small",
    srcs = ["vcf_test.py"],
    data = ["//nucleus/testdata"],
    python_version = "PY3",
    srcs_version = "PY3",
    deps = [
        ":gfile",
        ":vcf",
        "//nucleus/protos:reference_py_pb2",
        "//nucleus/protos:struct_py_pb2",
        "//nucleus/protos:variants_py_pb2",
        "//nucleus/testing:py_test_utils",
        "//nucleus/util:ranges",
        "@absl_py//absl/testing:absltest",
        "@absl_py//absl/testing:parameterized",
    ],
)

py_library(
    name = "sam",
    srcs = ["sam.py"],
    deps = [
        ":genomics_reader",
        ":genomics_writer",
        "//nucleus/io/python:sam_reader",
        "//nucleus/io/python:sam_writer",
        "//nucleus/protos:reads_py_pb2",
        "//nucleus/util:py_utils",
        "//nucleus/util:ranges",
    ],
)

py_test(
    name = "sam_test",
    size = "small",
    srcs = ["sam_test.py"],
    data = ["//nucleus/testdata"],
    python_version = "PY3",
    srcs_version = "PY3",
    deps = [
        ":gfile",
        ":sam",
        ":tfrecord",
        "//nucleus/protos:reference_py_pb2",
        "//nucleus/protos:struct_py_pb2",
        "//nucleus/testing:py_test_utils",
        "//nucleus/util:ranges",
        "@absl_py//absl/testing:absltest",
        "@absl_py//absl/testing:parameterized",
    ],
)

py_library(
    name = "bed",
    srcs = ["bed.py"],
    deps = [
        ":genomics_reader",
        ":genomics_writer",
        "//nucleus/io/python:bed_reader",
        "//nucleus/io/python:bed_writer",
        "//nucleus/protos:bed_py_pb2",
    ],
)

py_test(
    name = "bed_test",
    size = "small",
    srcs = ["bed_test.py"],
    data = ["//nucleus/testdata"],
    python_version = "PY3",
    srcs_version = "PY3",
    deps = [
        ":bed",
        "//nucleus/protos:bed_py_pb2",
        "//nucleus/testing:py_test_utils",
        "@absl_py//absl/testing:absltest",
        "@absl_py//absl/testing:parameterized",
    ],
)

py_library(
    name = "bedgraph",
    srcs = ["bedgraph.py"],
    deps = [
        ":genomics_reader",
        ":genomics_writer",
        "//nucleus/io/python:bedgraph_reader",
        "//nucleus/io/python:bedgraph_writer",
        "//nucleus/protos:bedgraph_py_pb2",
    ],
)

py_test(
    name = "bedgraph_test",
    size = "small",
    srcs = ["bedgraph_test.py"],
    data = ["//nucleus/testdata"],
    python_version = "PY3",
    srcs_version = "PY3",
    deps = [
        ":bedgraph",
        "//nucleus/protos:bedgraph_py_pb2",
        "//nucleus/testing:py_test_utils",
        "@absl_py//absl/testing:absltest",
        "@absl_py//absl/testing:parameterized",
    ],
)

py_library(
    name = "fasta",
    srcs = ["fasta.py"],
    deps = [
        ":genomics_reader",
        ":gfile",
        "//nucleus/io/python:reference",
        "//nucleus/protos:fasta_py_pb2",
        "//nucleus/util:ranges",
    ],
)

py_test(
    name = "fasta_test",
    size = "small",
    srcs = ["fasta_test.py"],
    data = ["//nucleus/testdata"],
    python_version = "PY3",
    srcs_version = "PY3",
    deps = [
        ":fasta",
        "//nucleus/protos:struct_py_pb2",
        "//nucleus/testing:py_test_utils",
        "//nucleus/util:ranges",
        "@absl_py//absl/testing:absltest",
        "@absl_py//absl/testing:parameterized",
    ],
)

py_library(
    name = "fastq",
    srcs = ["fastq.py"],
    deps = [
        ":genomics_reader",
        ":genomics_writer",
        "//nucleus/io/python:fastq_reader",
        "//nucleus/io/python:fastq_writer",
        "//nucleus/protos:fastq_py_pb2",
    ],
)

py_test(
    name = "fastq_test",
    size = "small",
    srcs = ["fastq_test.py"],
    data = ["//nucleus/testdata"],
    python_version = "PY3",
    srcs_version = "PY3",
    deps = [
        ":fastq",
        "//nucleus/protos:fastq_py_pb2",
        "//nucleus/testing:py_test_utils",
        "@absl_py//absl/testing:absltest",
        "@absl_py//absl/testing:parameterized",
    ],
)

py_library(
    name = "gff",
    srcs = ["gff.py"],
    deps = [
        ":genomics_reader",
        ":genomics_writer",
        "//nucleus/io/python:gff_reader",
        "//nucleus/io/python:gff_writer",
        "//nucleus/protos:gff_py_pb2",
    ],
)

py_library(
    name = "clif_postproc",
    srcs = ["clif_postproc.py"],
    deps = [
        "//nucleus/protos:bed_py_pb2",
        "//nucleus/protos:bedgraph_py_pb2",
        "//nucleus/protos:fastq_py_pb2",
        "//nucleus/protos:gff_py_pb2",
        "//nucleus/protos:reads_py_pb2",
        "//nucleus/protos:variants_py_pb2",
    ],
)

py_library(
    name = "sharded_file_utils",
    srcs = ["sharded_file_utils.py"],
    deps = [":gfile"],
)

py_test(
    name = "sharded_file_utils_test",
    size = "small",
    srcs = ["sharded_file_utils_test.py"],
    data = ["//nucleus/testdata"],
    python_version = "PY3",
    srcs_version = "PY3",
    deps = [
        ":sharded_file_utils",
        "//nucleus/protos:reference_py_pb2",
        "//nucleus/testing:py_test_utils",
        "@absl_py//absl/testing:absltest",
        "@absl_py//absl/testing:parameterized",
    ],
)

py_library(
    name = "tfrecord",
    srcs = ["tfrecord.py"],
    deps = [
        ":genomics_reader",
        ":genomics_writer",
        ":sharded_file_utils",
        "//nucleus/protos:example_py_pb2",
    ],
)

py_test(
    name = "tfrecord_test",
    size = "small",
    srcs = ["tfrecord_test.py"],
    data = ["//nucleus/testdata"],
    python_version = "PY3",
    srcs_version = "PY3",
    deps = [
        ":tfrecord",
        "//nucleus/protos:reference_py_pb2",
        "//nucleus/testing:py_test_utils",
        "@absl_py//absl/testing:absltest",
        "@absl_py//absl/testing:parameterized",
    ],
)

py_library(
    name = "tabix",
    srcs = ["tabix.py"],
    deps = [
        "//nucleus/io/python:tabix_indexer",
    ],
)

py_test(
    name = "tabix_test",
    size = "small",
    srcs = ["tabix_test.py"],
    data = ["//nucleus/testdata"],
    python_version = "PY3",
    srcs_version = "PY3",
    deps = [
        ":gfile",
        ":tabix",
        ":vcf",
        "//nucleus/testing:py_test_utils",
        "//nucleus/util:ranges",
        "@absl_py//absl/testing:absltest",
    ],
)

#
# C++ API
#

NUCLEUS_COPTS = [
    "-Wsign-compare",
]

cc_library(
    name = "io_cpp",
    deps = [
        ":bed_reader",
        ":bed_writer",
        ":bedgraph_reader",
        ":bedgraph_writer",
        ":fastq_reader",
        ":fastq_writer",
        ":gff_reader",
        ":gff_writer",
        ":gfile_cc",
        ":hts_path",
        ":hts_verbose",
        ":reader_base",
        ":reference",
        ":sam_reader",
        ":sam_writer",
        ":tabix_indexer",
        ":text_reader",
        ":text_writer",
        ":vcf_conversion",
        ":vcf_reader",
        ":vcf_writer",
    ],
)

test_suite(
    name = "smoke_tests",
    tests = ["hts_test"],
)

cc_library(
    name = "bed_reader",
    srcs = ["bed_reader.cc"],
    hdrs = ["bed_reader.h"],
    deps = [
        ":reader_base",
        ":text_reader",
        "//nucleus/platform:types",
        "//nucleus/protos:bed_cc_pb2",
        "//nucleus/util:cpp_utils",
        "//nucleus/vendor:statusor",
        "@com_google_absl//absl/strings",
        "@org_tensorflow//tensorflow/core:lib",
    ],
)

cc_test(
    name = "bed_reader_test",
    size = "small",
    srcs = ["bed_reader_test.cc"],
    data = ["//nucleus/testdata"],
    deps = [
        ":bed_reader",
        "//nucleus/testing:cpp_test_utils",
        "//nucleus/testing:gunit_extras",
        "//nucleus/util:cpp_utils",
        "@com_google_googletest//:gtest_main",
        "@org_tensorflow//tensorflow/core:test",
    ],
)

cc_library(
    name = "bed_writer",
    srcs = ["bed_writer.cc"],
    hdrs = ["bed_writer.h"],
    deps = [
        ":text_writer",
        "//nucleus/platform:types",
        "//nucleus/protos:bed_cc_pb2",
        "//nucleus/util:cpp_utils",
        "//nucleus/util:proto_ptr",
        "//nucleus/vendor:statusor",
        "@com_google_absl//absl/memory",
        "@com_google_absl//absl/strings",
        "@org_tensorflow//tensorflow/core:lib",
    ],
)

cc_test(
    name = "bed_writer_test",
    size = "small",
    srcs = ["bed_writer_test.cc"],
    data = ["//nucleus/testdata"],
    deps = [
        ":bed_writer",
        "//nucleus/testing:cpp_test_utils",
        "//nucleus/util:cpp_utils",
        "//nucleus/vendor:status_matchers",
        "@com_google_googletest//:gtest_main",
        "@org_tensorflow//tensorflow/core:lib",
        "@org_tensorflow//tensorflow/core:test",
    ],
)

cc_library(
    name = "bedgraph_reader",
    srcs = ["bedgraph_reader.cc"],
    hdrs = ["bedgraph_reader.h"],
    copts = NUCLEUS_COPTS,
    deps = [
        ":reader_base",
        ":text_reader",
        "//nucleus/platform:types",
        "//nucleus/protos:bedgraph_cc_pb2",
        "//nucleus/util:cpp_utils",
        "//nucleus/vendor:statusor",
        "@com_google_absl//absl/strings",
        "@org_tensorflow//tensorflow/core:lib",
    ],
)

cc_test(
    name = "bedgraph_reader_test",
    size = "small",
    srcs = ["bedgraph_reader_test.cc"],
    data = ["//nucleus/testdata"],
    deps = [
        ":bedgraph_reader",
        "//nucleus/testing:cpp_test_utils",
        "//nucleus/testing:gunit_extras",
        "//nucleus/util:cpp_utils",
        "@com_google_googletest//:gtest_main",
        "@org_tensorflow//tensorflow/core:test",
    ],
)

cc_library(
    name = "bedgraph_writer",
    srcs = ["bedgraph_writer.cc"],
    hdrs = ["bedgraph_writer.h"],
    copts = NUCLEUS_COPTS,
    deps = [
        ":text_writer",
        "//nucleus/platform:types",
        "//nucleus/protos:bedgraph_cc_pb2",
        "//nucleus/util:cpp_utils",
        "//nucleus/util:proto_ptr",
        "//nucleus/vendor:statusor",
        "@com_google_absl//absl/memory",
        "@com_google_absl//absl/strings",
        "@org_tensorflow//tensorflow/core:lib",
    ],
)

cc_test(
    name = "bedgraph_writer_test",
    size = "small",
    srcs = ["bedgraph_writer_test.cc"],
    data = ["//nucleus/testdata"],
    deps = [
        ":bedgraph_reader",
        ":bedgraph_writer",
        "//nucleus/testing:cpp_test_utils",
        "//nucleus/testing:gunit_extras",
        "//nucleus/util:cpp_utils",
        "//nucleus/vendor:status_matchers",
        "@com_google_googletest//:gtest_main",
        "@org_tensorflow//tensorflow/core:lib",
        "@org_tensorflow//tensorflow/core:test",
    ],
)

cc_library(
    name = "fastq_reader",
    srcs = ["fastq_reader.cc"],
    hdrs = ["fastq_reader.h"],
    deps = [
        ":reader_base",
        ":text_reader",
        "//nucleus/platform:types",
        "//nucleus/protos:fastq_cc_pb2",
        "//nucleus/util:cpp_utils",
        "//nucleus/vendor:statusor",
        "@com_google_absl//absl/strings",
        "@org_tensorflow//tensorflow/core:lib",
    ],
)

cc_test(
    name = "fastq_reader_test",
    size = "small",
    srcs = ["fastq_reader_test.cc"],
    data = ["//nucleus/testdata"],
    deps = [
        ":fastq_reader",
        "//nucleus/testing:cpp_test_utils",
        "//nucleus/testing:gunit_extras",
        "//nucleus/util:cpp_utils",
        "@com_google_googletest//:gtest_main",
        "@org_tensorflow//tensorflow/core:test",
    ],
)

cc_library(
    name = "fastq_writer",
    srcs = ["fastq_writer.cc"],
    hdrs = ["fastq_writer.h"],
    deps = [
        ":text_writer",
        "//nucleus/platform:types",
        "//nucleus/protos:fastq_cc_pb2",
        "//nucleus/util:cpp_utils",
        "//nucleus/util:proto_ptr",
        "//nucleus/vendor:statusor",
        "@com_google_absl//absl/memory",
        "@com_google_absl//absl/strings",
        "@org_tensorflow//tensorflow/core:lib",
    ],
)

cc_test(
    name = "fastq_writer_test",
    size = "small",
    srcs = ["fastq_writer_test.cc"],
    data = ["//nucleus/testdata"],
    deps = [
        ":fastq_writer",
        "//nucleus/testing:cpp_test_utils",
        "//nucleus/util:cpp_utils",
        "//nucleus/vendor:status_matchers",
        "@com_google_googletest//:gtest_main",
        "@org_tensorflow//tensorflow/core:lib",
        "@org_tensorflow//tensorflow/core:test",
    ],
)

cc_library(
    name = "sam_utils",
    srcs = ["sam_utils.cc"],
    hdrs = ["sam_utils.h"],
    copts = NUCLEUS_COPTS,
    deps = [
        ":hts_path",
        "//nucleus/platform:types",
        "//nucleus/protos:cigar_cc_pb2",
        "@htslib",
    ],
)

cc_test(
    name = "sam_utils_test",
    size = "small",
    srcs = ["sam_utils_test.cc"],
    copts = NUCLEUS_COPTS,
    deps = [
        ":sam_utils",
        "//nucleus/protos:cigar_cc_pb2",
        "@com_google_googletest//:gtest_main",
        "@htslib",
        "@org_tensorflow//tensorflow/core:test",
    ],
)

cc_library(
    name = "sam_reader",
    srcs = ["sam_reader.cc"],
    hdrs = ["sam_reader.h"],
    deps = [
        ":hts_path",
        ":reader_base",
        ":sam_utils",
        "//nucleus/platform:types",
        "//nucleus/protos:cigar_cc_pb2",
        "//nucleus/protos:position_cc_pb2",
        "//nucleus/protos:range_cc_pb2",
        "//nucleus/protos:reads_cc_pb2",
        "//nucleus/protos:reference_cc_pb2",
        "//nucleus/util:cpp_utils",
        "//nucleus/util:samplers",
        "//nucleus/vendor:statusor",
        "@com_google_absl//absl/strings",
        "@com_google_protobuf//:protobuf",
        "@htslib",
        "@org_tensorflow//tensorflow/core:lib",
    ],
)

cc_test(
    name = "sam_reader_test",
    size = "small",
    srcs = ["sam_reader_test.cc"],
    data = ["//nucleus/testdata"],
    deps = [
        ":sam_reader",
        ":sam_writer",
        "//nucleus/testing:cpp_test_utils",
        "//nucleus/testing:gunit_extras",
        "//nucleus/util:cpp_utils",
        "//nucleus/vendor:status_matchers",
        "@com_google_googletest//:gtest_main",
        "@org_tensorflow//tensorflow/core:lib",
        "@org_tensorflow//tensorflow/core:test",
    ],
)

cc_library(
    name = "sam_writer",
    srcs = ["sam_writer.cc"],
    hdrs = ["sam_writer.h"],
    copts = NUCLEUS_COPTS,
    deps = [
        ":hts_path",
        ":sam_utils",
        "//nucleus/platform:types",
        "//nucleus/protos:cigar_cc_pb2",
        "//nucleus/protos:position_cc_pb2",
        "//nucleus/protos:reads_cc_pb2",
        "//nucleus/protos:reference_cc_pb2",
        "//nucleus/protos:struct_cc_pb2",
        "//nucleus/util:proto_ptr",
        "//nucleus/vendor:statusor",
        "@com_google_absl//absl/memory",
        "@com_google_absl//absl/strings",
        "@com_google_protobuf//:protobuf",
        "@htslib",
        "@org_tensorflow//tensorflow/core:lib",
    ],
)

cc_test(
    name = "sam_writer_test",
    size = "small",
    srcs = ["sam_writer_test.cc"],
    copts = NUCLEUS_COPTS,
    data = ["//nucleus/testdata"],
    deps = [
        ":sam_reader",
        ":sam_writer",
        "//nucleus/testing:cpp_test_utils",
        "//nucleus/testing:gunit_extras",
        "//nucleus/util:cpp_utils",
        "//nucleus/vendor:status_matchers",
        "//nucleus/vendor:statusor",
        "@com_google_absl//absl/base:core_headers",
        "@com_google_absl//absl/strings",
        "@com_google_googletest//:gtest_main",
        "@org_tensorflow//tensorflow/core:lib",
        "@org_tensorflow//tensorflow/core:test",
    ],
)

cc_library(
    name = "vcf_reader",
    srcs = ["vcf_reader.cc"],
    hdrs = ["vcf_reader.h"],
    deps = [
        ":hts_path",
        ":reader_base",
        ":vcf_conversion",
        "//nucleus/platform:types",
        "//nucleus/protos:range_cc_pb2",
        "//nucleus/protos:reference_cc_pb2",
        "//nucleus/protos:variants_cc_pb2",
        "//nucleus/util:cpp_math",
        "//nucleus/util:cpp_utils",
        "//nucleus/vendor:statusor",
        "@com_google_absl//absl/memory",
        "@com_google_absl//absl/strings",
        "@com_google_protobuf//:protobuf",
        "@htslib",
        "@org_tensorflow//tensorflow/core:lib",
    ],
)

cc_test(
    name = "vcf_reader_test",
    size = "medium",
    srcs = ["vcf_reader_test.cc"],
    data = ["//nucleus/testdata"],
    deps = [
        ":vcf_reader",
        "//nucleus/protos:struct_cc_pb2",
        "//nucleus/protos:variants_cc_pb2",
        "//nucleus/testing:cpp_test_utils",
        "//nucleus/testing:gunit_extras",
        "//nucleus/util:cpp_utils",
        "//nucleus/vendor:status_matchers",
        "@com_google_googletest//:gtest_main",
        "@com_google_protobuf//:protobuf",
        "@org_tensorflow//tensorflow/core:lib",
        "@org_tensorflow//tensorflow/core:test",
    ],
)

cc_library(
    name = "vcf_writer",
    srcs = ["vcf_writer.cc"],
    hdrs = ["vcf_writer.h"],
    deps = [
        ":hts_path",
        ":vcf_conversion",
        "//nucleus/platform:types",
        "//nucleus/protos:range_cc_pb2",
        "//nucleus/protos:reference_cc_pb2",
        "//nucleus/protos:variants_cc_pb2",
        "//nucleus/util:cpp_utils",
        "//nucleus/util:proto_ptr",
        "//nucleus/vendor:statusor",
        "@com_google_absl//absl/memory",
        "@com_google_absl//absl/strings",
        "@com_google_protobuf//:protobuf",
        "@htslib",
        "@org_tensorflow//tensorflow/core:lib",
    ],
)

cc_test(
    name = "vcf_writer_test",
    size = "small",
    srcs = ["vcf_writer_test.cc"],
    data = ["//nucleus/testdata"],
    deps = [
        ":vcf_writer",
        "//nucleus/platform:types",
        "//nucleus/protos:reference_cc_pb2",
        "//nucleus/protos:variants_cc_pb2",
        "//nucleus/testing:cpp_test_utils",
        "//nucleus/util:cpp_utils",
        "//nucleus/vendor:status_matchers",
        "@com_google_googletest//:gtest_main",
        "@com_google_protobuf//:protobuf",
        "@org_tensorflow//tensorflow/core:lib",
        "@org_tensorflow//tensorflow/core:test",
    ],
)

cc_test(
    name = "vcf_roundtrip_test",
    size = "small",
    srcs = ["vcf_roundtrip_test.cc"],
    data = ["//nucleus/testdata"],
    deps = [
        ":vcf_reader",
        ":vcf_writer",
        "//nucleus/platform:types",
        "//nucleus/protos:variants_cc_pb2",
        "//nucleus/testing:cpp_test_utils",
        "//nucleus/testing:gunit_extras",
        "//nucleus/vendor:status_matchers",
        "@com_google_googletest//:gtest_main",
        "@org_tensorflow//tensorflow/core:test",
    ],
)

cc_library(
    name = "reference",
    srcs = ["reference.cc"],
    hdrs = ["reference.h"],
    deps = [
        ":hts_path",
        ":reader_base",
        ":text_reader",
        "//nucleus/platform:types",
        "//nucleus/protos:fasta_cc_pb2",
        "//nucleus/protos:range_cc_pb2",
        "//nucleus/protos:reference_cc_pb2",
        "//nucleus/util:cpp_utils",
        "//nucleus/vendor:statusor",
        "@com_google_absl//absl/strings",
        "@com_google_absl//absl/types:optional",
        "@htslib",
        "@org_tensorflow//tensorflow/core:lib",
    ],
)

# Abstract value-parameterized tests:
# https://github.com/google/googletest/blob/master/googletest/docs/AdvancedGuide.md#creating-value-parameterized-abstract-tests
cc_test(
    name = "reference_test",
    size = "small",
    srcs = ["reference_test.cc"],
    data = ["//nucleus/testdata"],
    deps = [
        ":reader_base",
        ":reference",
        "//nucleus/platform:types",
        "//nucleus/protos:fasta_cc_pb2",
        "//nucleus/protos:range_cc_pb2",
        "//nucleus/protos:reference_cc_pb2",
        "//nucleus/testing:cpp_test_utils",
        "//nucleus/util:cpp_utils",
        "//nucleus/vendor:status_matchers",
        "@com_google_absl//absl/strings",
        "@com_google_googletest//:gtest_main",
        "@org_tensorflow//tensorflow/core:lib",
    ],
)

cc_library(
    name = "reader_base",
    srcs = ["reader_base.cc"],
    hdrs = ["reader_base.h"],
    deps = [
        "//nucleus/util:proto_ptr",
        "//nucleus/vendor:statusor",
        "@com_google_absl//absl/synchronization",
        "@org_tensorflow//tensorflow/core:lib",
    ],
)

cc_test(
    name = "reader_base_test",
    size = "small",
    srcs = ["reader_base_test.cc"],
    deps = [
        ":reader_base",
        "//nucleus/platform:types",
        "//nucleus/vendor:status_matchers",
        "//nucleus/vendor:statusor",
        "@com_google_googletest//:gtest_main",
        "@org_tensorflow//tensorflow/core:lib",
        "@org_tensorflow//tensorflow/core:test",
    ],
)

cc_library(
    name = "vcf_conversion",
    srcs = ["vcf_conversion.cc"],
    hdrs = ["vcf_conversion.h"],
    copts = NUCLEUS_COPTS,
    deps = [
        "//nucleus/platform:types",
        "//nucleus/protos:variants_cc_pb2",
        "//nucleus/util:cpp_math",
        "//nucleus/util:cpp_utils",
        "//nucleus/vendor:statusor",
        "@com_google_absl//absl/memory",
        "@com_google_absl//absl/strings",
        "@com_google_protobuf//:protobuf",
        "@htslib",
        "@org_tensorflow//tensorflow/core:lib",
    ],
)

cc_library(
    name = "hts_path",
    srcs = ["hts_path.cc"],
    hdrs = ["hts_path.h"],
    deps = [
        "//nucleus/platform:types",
        "@com_google_absl//absl/strings",
        "@htslib",
    ],
)

cc_library(
    name = "hts_verbose",
    srcs = ["hts_verbose.cc"],
    hdrs = ["hts_verbose.h"],
    deps = ["@htslib"],
)

cc_test(
    name = "hts_verbose_test",
    size = "small",
    srcs = ["hts_verbose_test.cc"],
    deps = [
        ":hts_verbose",
        "@com_google_googletest//:gtest_main",
        "@org_tensorflow//tensorflow/core:test",
    ],
)

cc_test(
    name = "hts_test",
    size = "small",
    srcs = ["hts_test.cc"],
    data = ["//nucleus/testdata"],
    deps = [
        ":hts_path",
        "//nucleus/platform:types",
        "//nucleus/testing:cpp_test_utils",
        "//nucleus/util:port",
        "@com_google_absl//absl/strings",
        "@com_google_googletest//:gtest_main",
        "@htslib",
        "@org_tensorflow//tensorflow/core:test",
    ],
)

cc_library(
    name = "tabix_indexer",
    srcs = ["tabix_indexer.cc"],
    hdrs = ["tabix_indexer.h"],
    deps = [
        ":hts_path",
        "//nucleus/platform:types",
        "@org_tensorflow//tensorflow/core:lib",
    ],
)

cc_test(
    name = "tabix_indexer_test",
    srcs = ["tabix_indexer_test.cc"],
    data = ["//nucleus/testdata"],
    deps = [
        ":tabix_indexer",
        ":vcf_reader",
        ":vcf_writer",
        "//nucleus/testing:cpp_test_utils",
        "//nucleus/util:cpp_utils",
        "//nucleus/vendor:status_matchers",
        "@com_google_googletest//:gtest_main",
        "@org_tensorflow//tensorflow/core:lib",
    ],
)

cc_library(
    name = "text_writer",
    srcs = ["text_writer.cc"],
    hdrs = ["text_writer.h"],
    copts = NUCLEUS_COPTS,
    deps = [
        ":hts_path",
        "//nucleus/platform:types",
        "//nucleus/vendor:statusor",
        "@com_google_absl//absl/memory",
        "@com_google_absl//absl/strings",
        "@htslib",
        "@org_tensorflow//tensorflow/core:lib",
    ],
)

cc_library(
    name = "text_reader",
    srcs = ["text_reader.cc"],
    hdrs = ["text_reader.h"],
    deps = [
        ":hts_path",
        "//nucleus/platform:types",
        "//nucleus/vendor:statusor",
        "@com_google_absl//absl/memory",
        "@htslib",
        "@org_tensorflow//tensorflow/core:lib",
    ],
)

cc_test(
    name = "text_io_test",
    srcs = ["text_io_test.cc"],
    deps = [
        ":text_reader",
        ":text_writer",
        "//nucleus/platform:types",
        "//nucleus/testing:cpp_test_utils",
        "//nucleus/vendor:statusor",
        "@com_google_googletest//:gtest_main",
        "@org_tensorflow//tensorflow/core:lib",
    ],
)

cc_library(
    name = "tfrecord_reader",
    srcs = ["tfrecord_reader.cc"],
    hdrs = ["tfrecord_reader.h"],
    deps = [
        "//nucleus/platform:types",
        "@com_google_absl//absl/memory",
        "@com_google_absl//absl/strings:cord",
        "@org_tensorflow//tensorflow/core:lib",
        "@org_tensorflow//tensorflow/core/platform/cloud:gcs_file_system",
    ],
)

cc_test(
    name = "tfrecord_reader_test",
    srcs = ["tfrecord_reader_test.cc"],
    data = ["//nucleus/testdata"],
    deps = [
        ":tfrecord_reader",
        "//nucleus/protos:variants_cc_pb2",
        "//nucleus/testing:cpp_test_utils",
        "@com_google_googletest//:gtest_main",
    ],
)

cc_library(
    name = "tfrecord_writer",
    srcs = ["tfrecord_writer.cc"],
    hdrs = ["tfrecord_writer.h"],
    deps = [
        "@com_google_absl//absl/memory",
        "@com_google_absl//absl/strings:cord",
        "@org_tensorflow//tensorflow/core:lib",
        "@org_tensorflow//tensorflow/core/platform/cloud:gcs_file_system",
    ],
)

cc_library(
    name = "gfile_cc",
    srcs = ["gfile.cc"],
    hdrs = ["gfile.h"],
    deps = [
        "@com_google_absl//absl/memory",
        "@com_google_absl//absl/strings:cord",
        "@org_tensorflow//tensorflow/core:lib",
    ],
)

#
# Misc
#

py_test(
    name = "genomics_io_noplugin_test",
    size = "small",
    srcs = ["genomics_io_noplugin_test.py"],
    python_version = "PY3",
    srcs_version = "PY3",
    deps = [
        "//nucleus/io:sam",
        "//nucleus/testing:py_test_utils",
        "@absl_py//absl/testing:absltest",
    ],
)

cc_library(
    name = "gff_reader",
    srcs = ["gff_reader.cc"],
    hdrs = ["gff_reader.h"],
    deps = [
        ":reader_base",
        ":text_reader",
        "//nucleus/platform:types",
        "//nucleus/protos:gff_cc_pb2",
        "//nucleus/protos:range_cc_pb2",
        "//nucleus/vendor:statusor",
        "@com_google_absl//absl/strings",
        "@com_google_absl//absl/types:optional",
        "@com_google_protobuf//:protobuf",
        "@org_tensorflow//tensorflow/core:lib",
    ],
)

cc_test(
    name = "gff_reader_test",
    srcs = ["gff_reader_test.cc"],
    data = ["//nucleus/testdata"],
    deps = [
        ":gff_reader",
        "//nucleus/protos:gff_cc_pb2",
        "//nucleus/protos:range_cc_pb2",
        "//nucleus/testing:cpp_test_utils",
        "//nucleus/testing:gunit_extras",
        "@com_google_googletest//:gtest_main",
    ],
)

cc_library(
    name = "gff_writer",
    srcs = ["gff_writer.cc"],
    hdrs = ["gff_writer.h"],
    deps = [
        ":text_writer",
        "//nucleus/platform:types",
        "//nucleus/protos:gff_cc_pb2",
        "//nucleus/protos:range_cc_pb2",
        "//nucleus/util:cpp_utils",
        "//nucleus/util:proto_ptr",
        "//nucleus/vendor:statusor",
        "@com_google_absl//absl/memory",
        "@com_google_absl//absl/strings",
        "@com_google_protobuf//:protobuf",
        "@org_tensorflow//tensorflow/core:lib",
    ],
)

cc_test(
    name = "gff_writer_test",
    srcs = ["gff_writer_test.cc"],
    deps = [
        ":gff_writer",
        "//nucleus/platform:types",
        "//nucleus/protos:gff_cc_pb2",
        "//nucleus/testing:cpp_test_utils",
        "//nucleus/vendor:status_matchers",
        "//nucleus/vendor:statusor",
        "@com_google_googletest//:gtest_main",
        "@com_google_protobuf//:protobuf",
        "@org_tensorflow//tensorflow/core:lib",
    ],
)

py_test(
    name = "gff_test",
    srcs = ["gff_test.py"],
    data = ["//nucleus/testdata"],
    python_version = "PY3",
    srcs_version = "PY3",
    deps = [
        ":gff",
        ":tfrecord",
        "//nucleus/protos:gff_py_pb2",
        "//nucleus/testing:py_test_utils",
        "//nucleus/util:ranges",
        "@absl_py//absl/testing:absltest",
        "@absl_py//absl/testing:parameterized",
    ],
)

py_binary(
    name = "converter",
    srcs = ["converter.py"],
    python_version = "PY3",
    deps = [":converter_lib"],
)

py_library(
    name = "converter_lib",
    srcs = ["converter.py"],
    deps = [
        "//nucleus/io:io_libs_py",
        "@absl_py//absl:app",
        "@absl_py//absl/logging",
    ],
)

py_test(
    name = "converter_test",
    srcs = ["converter_test.py"],
    data = ["//nucleus/testdata"],
    python_version = "PY3",
    srcs_version = "PY3",
    deps = [
        ":converter_lib",
        "//nucleus/testing:py_test_utils",
        "@absl_py//absl/logging",
        "@absl_py//absl/testing:absltest",
        "@absl_py//absl/testing:parameterized",
    ],
)

py_library(
    name = "gfile",
    srcs = ["gfile.py"],
    srcs_version = "PY3",
    deps = ["//nucleus/io/python:gfile"],
)

py_test(
    name = "gfile_test",
    srcs = ["gfile_test.py"],
    data = ["//nucleus/testdata"],
    python_version = "PY3",
    srcs_version = "PY3",
    deps = [
        ":gfile",
        "//nucleus/testing:py_test_utils",
        "@absl_py//absl/testing:absltest",
    ],
)
