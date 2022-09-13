from slither_pess.detectors.double_entry_token_possibility import DoubleEntryTokenPossiblity
from slither_pess.detectors.unprotected_setter import UnprotectedSetter


def make_plugin():
    plugin_detectors = [DoubleEntryTokenPossiblity,UnprotectedSetter]
    plugin_printers = []

    return plugin_detectors, plugin_printers
