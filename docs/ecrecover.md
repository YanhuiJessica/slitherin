# Ecrecover

## Configuration

- Check: `pess-ecrecover`
- Severity: `High`
- Confidence: `Medium`

## Description

`ecrecover` functions returns `0` on error. It is important to check the result for `0`.

### Potential Improvement

As for now, the detector might not work on asm level.

## Vulnerable Scenario

[test scenarios](../tests/ecrecover.sol)

## Recommendation

Check the result of `ecrecover` or use OZ ECDSA library.
