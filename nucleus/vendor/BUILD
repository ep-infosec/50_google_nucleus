package(
    default_visibility = [
        "//visibility:public",
    ],
)

licenses(["notice"])  # Apache License 2.0

exports_files(["message_module.cc"])

cc_library(
    name = "vendor_cpp",
    deps = [
        ":statusor",
        ":statusor_clif_converters",
        ":statusor_examples",
    ],
)

cc_library(
    name = "statusor",
    hdrs = [
        "statusor.h",
    ],
    deps = [
        "//nucleus/platform:types",
        "@org_tensorflow//tensorflow/core:lib",
    ],
)

cc_library(
    name = "status_matchers",
    testonly = True,
    hdrs = ["status_matchers.h"],
    deps = [
        ":statusor",
        "@com_google_googletest//:gtest_main",
        "@org_tensorflow//tensorflow/core:lib",
        "@org_tensorflow//tensorflow/core:test",
    ],
)

cc_test(
    name = "statusor_test",
    size = "small",
    srcs = ["statusor_test.cc"],
    deps = [
        ":status_matchers",
        ":statusor",
        "@com_google_googletest//:gtest_main",
        "@org_tensorflow//tensorflow/core:lib",
        "@org_tensorflow//tensorflow/core:test",
    ],
)

cc_library(
    name = "statusor_clif_converters",
    srcs = ["statusor_clif_converters.cc"],
    hdrs = ["statusor_clif_converters.h"],
    deps = [
        ":statusor",
        "@clif//:cpp_runtime",
        "@com_google_absl//absl/strings:cord",
        "@local_config_python//:python_headers",
    ],
)

cc_library(
    name = "statusor_examples",
    hdrs = ["statusor_examples.h"],
    deps = [
        ":statusor",
        "//nucleus/platform:types",
    ],
)
