from slitherin.detectors.arbitrary_call.arbitrary_call import ArbitraryCall
from slitherin.detectors.double_entry_token_possibility import (
    DoubleEntryTokenPossiblity,
)
from slitherin.detectors.dubious_typecast import DubiousTypecast
from slitherin.detectors.falsy_only_eoa_modifier import OnlyEOACheck
from slitherin.detectors.magic_number import MagicNumber
from slitherin.detectors.strange_setter import StrangeSetter
from slitherin.detectors.unprotected_setter import UnprotectedSetter
from slitherin.detectors.nft_approve_warning import NftApproveWarning
from slitherin.detectors.inconsistent_nonreentrant import InconsistentNonreentrant
from slitherin.detectors.call_forward_to_protected import CallForwardToProtected
from slitherin.detectors.multiple_storage_read import MultipleStorageRead
from slitherin.detectors.timelock_controller import TimelockController
from slitherin.detectors.tx_gasprice_warning import TxGaspriceWarning
from slitherin.detectors.unprotected_initialize import UnprotectedInitialize
from slitherin.detectors.read_only_reentrancy import ReadOnlyReentrancy
from slitherin.detectors.event_setter import EventSetter
from slitherin.detectors.before_token_transfer import BeforeTokenTransfer
from slitherin.detectors.uni_v2 import UniswapV2
from slitherin.detectors.token_fallback import TokenFallback
from slitherin.detectors.for_continue_increment import ForContinueIncrement
from slitherin.detectors.ecrecover import Ecrecover
from slitherin.detectors.public_vs_external import PublicVsExternal
from slitherin.detectors.aave.flashloan_callback import AAVEFlashloanCallbackDetector


plugin_detectors = [
    DoubleEntryTokenPossiblity,
    UnprotectedSetter,
    NftApproveWarning,
    InconsistentNonreentrant,
    StrangeSetter,
    OnlyEOACheck,
    MagicNumber,
    DubiousTypecast,
    CallForwardToProtected,
    MultipleStorageRead,
    TimelockController,
    TxGaspriceWarning,
    UnprotectedInitialize,
    ReadOnlyReentrancy,
    EventSetter,
    BeforeTokenTransfer,
    UniswapV2,
    TokenFallback,
    ForContinueIncrement,
    ArbitraryCall,
    Ecrecover,
    PublicVsExternal,
    AAVEFlashloanCallbackDetector,
]
plugin_printers = []


def make_plugin():
    return plugin_detectors, plugin_printers
