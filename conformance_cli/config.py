import logging.config
from enum import Enum


def init_config():
    logging.config.fileConfig("logging.conf")


class TestType(str, Enum):
    COLLATION_SHORT = "collation_short"
    DATETIME_FMT = "datetime_fmt"
    LANG_NAMES = "lang_names"
    LIKELY_SUBTAGS = "likely_subtags"
    LIST_FMT = "list_fmt"
    MESSAGE_FMT2 = "message_fmt2"
    NUMBER_FMT = "number_fmt"
    PLURAL_RULES = "plural_rules"
    RELATIVE_DATETIME_FMT = "rdt_fmt"


test_types = [t.value for t in TestType]


class Executor(str, Enum):
    CPP = "cpp"
    DART_NATIVE = "dart_native"
    DART_WEB = "dart_web"
    ICU4J = "icu4j"
    NODE = "node"
    PYTHON = "python"
    RUST = "rust"


executors = [e.value for e in Executor]

paths = {
    "default_input": "DDT_DATA/testData",
    "default_output": "DDT_DATA/testOutput",
    "default_report": "DDT_DATA/testReports",
}
